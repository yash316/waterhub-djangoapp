from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Shop(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        print("Cart", request.session['cart'])
        return redirect('Shop')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        # request.session.get('cart').claer()
        categories = Category.objects.all()
        # print(products)
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('user email', request.session.get('email'))
        return render(request, 'shop.html', data)
