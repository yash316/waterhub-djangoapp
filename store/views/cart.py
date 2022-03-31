from django.shortcuts import render, redirect
from store.models import Product, Category, Customer, Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
import razorpay
from django.views.decorators.csrf import csrf_exempt
# html required modules
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        print("Customer ID", request.session.get('customer'))
        # cust_id = request.session.get('customer')
        # name = Customer.objects.get(id=cust_id)
        # print("Customer Name :", name)
        # data={}
        # data['products'] = products
        # data['name'] = name
        return render(request, 'cart.html', {'products': products})


def checkout(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    cust_id = request.session.get('customer')
    name = Customer.objects.get(id=cust_id)
    print("Customer Name :", name)
    data = {}
    data['products'] = products
    data['name'] = name

    if request.method == 'POST':
        # customer = request.session.get('customer')
        customer_id = request.POST.get('customer_id')
        name = request.POST.get('name'),
        product_list = request.POST.get('product_list')
        p_list = product_list.strip()
        quantity = request.POST.get('quantity')
        price = int(request.POST.get('price')) * 100
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('phone')
        client = razorpay.Client(auth=('rzp_test_udHvAtideokL3X', 'Al7YVT6NQBIfK0JBGDXjJv9N'))
        payment = client.order.create({'amount': price, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        print("Customer:", customer_id, p_list, quantity, price)
        conf_order = Order(customer_id=customer_id,
                           name=name,
                           product_list=p_list,
                           quantity=quantity,
                           price=price,
                           email=email,
                           phone=phone,
                           address=address,
                           payment_id=payment['id'])
        conf_order.save()
        # request.session['cart'] = {}
        return render(request, 'checkout.html', {'payment': payment})
    # request.session['cart'] = {}

    return render(request, 'checkout.html', data)


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        print(order_id)
        user = Order.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        amt = int(user.price) / 100
        if user.paid == True:
            html_content = render_to_string("email.html",
                                            {'title': 'WaterHub', 'address': user.address, 'date': user.date,
                                             'phone': user.phone,
                                             'payment_id': user.payment_id, 'amount': amt}, )
            text_content = strip_tags(html_content)
            email_msg = EmailMultiAlternatives(
                # subject
                "Order Confirmation - WaterHub",
                # content
                text_content,
                # from email,
                settings.EMAIL_HOST_USER,
                # rec list
                [user.email]
            )
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()
    request.session['cart'] = {}
    return render(request, 'success.html')
    # request.session['cart'] = {}


def clearCart(request):
    request.session['cart'] = {}

    return redirect('Cart')


def welemail(request):
    a = 1000
    amt = a / 100
    return render(request, 'welcome_email.html', {'price': amt})
