from django.shortcuts import render, redirect
from store.models import Product, Category, Customer, Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        # order = Order.get_orders_by_customer(customer)
        # print(order)
        orders = Order.objects.filter(customer_id__icontains=customer)
        print("Customer Orders", orders)
        return render(request, 'order.html', {'orders': orders})
