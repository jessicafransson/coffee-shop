from django.shortcuts import render, redirect
from .forms import ContactForm
from profiles.models import UserProfile

from django.contrib import messages


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message was sent successfully. \
                Please give us up to 2 working days for a response.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'Your request could not be processed. \
            Please make sure all fields are correct and try again.')
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'contact_name': user.default_full_name,
                    'contact_email': user.user.email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
