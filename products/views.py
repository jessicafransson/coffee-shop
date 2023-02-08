from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg
from django.conf import settings

from .models import Product, Category
from review.models import Review
from .forms import ProductForm
from review.forms import ReviewForm
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter anything!!"
                    )
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Detailed view of the products in the shop """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(
        product=product).order_by('-created_on')
    review_count = len(reviews)

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews.create(
                user=user_profile,
                product=product,
                rating=request.POST.get('rating'),
                body=request.POST.get('body')
            )
            reviews = Review.objects.all().filter(product=product)
            rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = rating
            product.review_count = review_count + 1
            product.save()
            messages.success(request, 'Review added sucessfully')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            print(form.errors.as_data())
            messages.error(
                request,
                'Review Failed. \
                    Please check for issues and try again.'
                )
            return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()
        if request.user.is_authenticated:
            reviewed = Review.objects.all().filter(
                product=product).filter(user=user_profile.id)
        else:
            reviewed = False

        liked = False
        if product.likes.filter(id=request.user.id).exists():
            liked = True


        context = {
            'product': product,
            'form': form,
            'reviews': reviews,
            'review_count': review_count,
            'reviewed': reviewed,
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Adding a product to the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can be here.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Could not add your product,\
                    please make sure the form is valid!'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can be here.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Could not update the product. \
                Please make sure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete an item from the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can be here.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product is now deleted!')
    return redirect(reverse('products'))
