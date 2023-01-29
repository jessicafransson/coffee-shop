from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Coupon
from .forms import CouponApplyForm, CouponForm


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
                )
            request.session['coupon_id'] = coupon.id
            messages.success(request, (
                        f"Success! {coupon} coupon applied")
                    )
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(
                request,
                "Sorry, that coupon does not exist or is no longer valid"
                )
    return redirect('view_bag')


@login_required
def add_coupon(request):
    """ Add a coupon to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added coupon!')
            return redirect('add_coupon')
        else:
            messages.error(
                request,
                'Failed to add coupon. Please ensure the form is valid.'
                )
    else:
        form = CouponForm()

    coupons = Coupon.objects.all()
    template = 'coupons/add_coupon.html'
    context = {
        'form': form,
        'coupons': coupons,
    }

    return render(request, template, context)


@login_required
def edit_coupon(request, coupon_id):
    """ Edit a coupon in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    coupon = get_object_or_404(Coupon, pk=coupon_id)
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated coupon!')
            return redirect('add_coupon')
        else:
            messages.error(
                request,
                'Failed to update coupon. Please ensure the form is valid.')
    else:
        form = CouponForm(instance=coupon)
        messages.info(request, f'You are editing {coupon}')

    template = 'coupons/edit_coupon.html'
    context = {
        'form': form,
        'coupon': coupon,
    }

    return render(request, template, context)


@login_required
def delete_coupon(request, coupon_id):
    """ Delete a coupon from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    coupon = get_object_or_404(Coupon, pk=coupon_id)
    coupon.delete()
    messages.success(request, 'Coupon deleted!')
    return redirect(reverse('add_coupon'))
