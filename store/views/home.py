from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models.customer import Contact
from django.contrib import messages


def index(request):
    print('user email', request.session.get('email'))
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_req = Contact(name=name,
                              email=email,
                              phone=phone,
                              message=message)
        contact_req.save()
        messages.success(request, 'Your message has been send successfully. We will get in touch with you very soon!')
    return render(request, 'contactus.html')