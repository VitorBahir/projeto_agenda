from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            return redirect('contact:contact', contact_id=new_contact.id)

        context = {'form': form}
        return render(request, 'contact/create.html', context)

    context = {'form': ContactForm()}
    return render(request, 'contact/create.html', context)
