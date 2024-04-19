from django.contrib import messages
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank you!')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
