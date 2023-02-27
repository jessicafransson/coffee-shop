from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .models import Review
from .forms import ReviewForm


@login_required
def edit_review(request, review_id):
    """ Edit a review for a product """
    review = get_object_or_404(Review, pk=review_id)
    if request.user.id != review.user.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(
            reverse('product_detail', args=[review.product.id])
            )
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            product = review.product
            reviews = Review.objects.all().filter(product=product)
            rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = rating
            product.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(
                reverse('product_detail', args=[review.product.id])
                )
        else:
            messages.error(
                request,
                'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {review.product.name}'
            )

    template = 'review/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a users review from product details page """
    review = get_object_or_404(Review, pk=review_id)
    if request.user.id != review.user.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(
            reverse('product_detail', args=[review.product.id])
            )
    review.delete()
    product = review.product
    reviews = Review.objects.all().filter(product=product)
    rating = reviews.aggregate(Avg('rating'))['rating__avg']
    product.rating = rating
    product.review_count -= 1
    product.save()
    messages.success(request, 'Review successfully deleted!')
    return redirect(reverse('product_detail', args=[review.product.id]))
