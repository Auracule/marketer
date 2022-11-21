import requests
import json
import uuid

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.db.models import Q
from userprofile.models import *
from userprofile.forms import *
from store.models import *
from store.forms import *
from . models import *
from . forms import *

# Create your views here.

def index(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }
    return render(request, 'index.html', context)

def categories(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return render(request, 'categories.html', context)

def category(request,id,slug):
    single = Category.objects.get(slug = slug)
    category = Product.objects.filter(category_id=id)

    context = {
        'category':category,
        'single':single,
    }
    return render(request, 'category.html', context)


def product(request):
    # single = Category.objects.filter()
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request , 'product.html', context)

@login_required(login_url='signin')
def single_prod(request, id):
    prods = Product.objects.get(pk = id)

    context = {
        'prods':prods,
    }
    return render(request, 'single_prod.html',context)

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for contacting us, Your Message sent successfully!')
            return redirect('index')
        else:
            messages.error(request, form.error)
            return redirect('index')
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in {user.username}')
            return redirect('index')
        else:
            messages.info(request, 'invalid username/password. Check, and login again')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        state = request.POST['state']
        address = request.POST['address']
        pix = request.POST['pix']
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newprofile = Profile(user=user)
            newprofile.username = user.username
            newprofile.first_name = user.first_name
            newprofile.last_name = user.last_name
            newprofile.email = user.email
            newprofile.phone = phone
            newprofile.state = state
            newprofile.address = address
            newprofile.pix = pix
            newprofile.save()
            login(request, user)
            messages.success(request, f'Congratulations{user.username}, Your Registration was Successful!...')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')



@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')



@login_required(login_url='signin')
def profile(request):
  profile = Profile.objects.get(user__username = request.user.username)

  context = {
    'profile':profile,
  }

  return render(request, 'profile.html', context)

@login_required(login_url='signin')
def profile_update(request):
  profile = Profile.objects.get(user__username = request.user.username)
  update = ProfileUpdate(instance=request.user.profile)
  if request.method == 'POST':
    update = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
    if update.is_valid():
      update.save()
      messages.success(request, 'update successful')
      return redirect('profile')
    else:
      messages.error(request, update.errors)
      return redirect('profile_update')
  context = {
    'profile':profile,
    'update':update,
  }
  return render(request, 'profile_update.html', context)

@login_required(login_url='signin')
def password(request):
    profile = Profile.objects.get(user__username = request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            update_session_auth_hash(request, user)
            form.save()
            messages.success(request, 'password change successful!...')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('password')
    context = {
        'form':form,
        'profile':profile,
    }
    return render(request, 'password.html', context)



@login_required(login_url='signin')
def cart(request):
    if request.method == 'POST':
        quant = int(request.POST['quantity'])
        item_id = request.POST['product_id']
        product = Product.objects.get(pk=item_id)
        order_num = Profile.objects.get(user__username = request.user.username)
        cart_no = order_num.id

        cart = Cart.objects.filter(user__username = request.user.username, paid=False)
        if cart:
            basket = Cart.objects.filter(product_id=product.id, user__username = request.user.username).first()
            if basket:
                basket.quantity += quant
                basket.amount = basket.quantity * basket.price
                basket.save()
                messages.success(request, 'added to cart')
                return redirect('product')
            else:
                newitem = Cart()
                newitem.user = request.user
                newitem.product = product
                newitem.price = product.price
                newitem.quantity = quant
                newitem.amount = product.price *quant
                newitem.title_g = product.name
                newitem.order_no = cart_no
                newitem.paid = False
                newitem.save()
                messages.success(request, 'added successfully')
                return redirect('product')
        else:
            newcart = Cart()
            newcart.user = request.user
            newcart.product = product
            newcart.price = product.price
            newcart.amount = product.price * quant
            newcart.quantity = quant
            newcart.order_no = cart_no
            newcart.paid = False
            newcart.title_g = product.name
            newcart.save()
            messages.success(request, 'success')
            return redirect('product')
    return redirect('product')


@login_required(login_url='signin')
def shopcart(request):
    trolley = Cart.objects.filter(user__username = request.user.username, paid = False)
    profile = Profile.objects.get(user__username=request.user.username)

    subtotal = 0
    total = 0
    vat = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'trolley':trolley,
        'profile':profile,
        'subtotal':subtotal,
        'total':total,
        'vat':vat,
    }
    return render(request, 'displaycart.html', context)


@login_required(login_url='signin')
def delete_item(request):
    item_id = request.POST['item_id']
    item_delete = Cart.objects.get(pk= item_id)
    item_delete.delete()
    messages.success(request, 'cart deleted successfully!....')
    return redirect('shopcart')


@login_required(login_url='signin')
def increase(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        quant = int(request.POST['quant'])
        modify = Cart.objects.get(pk = item_id)
        modify.quantity += quant
        modify.amount = modify.price * modify.quantity
        modify.save()
        messages.success(request, 'Modified successfully!......')
    return redirect('shopcart')


@login_required(login_url='signin')
def checkout(request):
    profile = Profile.objects.get(user__username=request.user.username)
    trolley = Cart.objects.filter(user__username = request.user.username, paid = False)

    subtotal = 0
    total = 0
    vat = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'trolley':trolley,
        'profile':profile,
        'total':total,
    }
    return render(request, 'checkout.html', context)



@login_required(login_url='signin')
def pay(request):
    if request.method == 'POST':
        api_key = 'sk_test_43762140e809dbc5ffee4d9c1e84d8c72afd6b9d'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://127.0.0.1:8000/callback/'
        ref = str(uuid.uuid4())
        profile = Profile.objects.get(user__username = request.user.username)
        shop_code = profile.id
        total = float(request.POST['total']) * 100
        user = User.objects.get(username = request.user.username)
        email = user.email
        first_name = user.first_name
        last_name = user.last_name
        phone = request.POST['phone']
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref, 'callback_url':cburl, 'amount':int(total), 'email':user.email, 'order_number':shop_code,'currency':'NGN'}

        try:
            r = requests.post(curl, headers= headers, json=data)
        except Exception:
            messages.error(request, 'Network Busy, Try again later')
        else:
            transback = json.loads(r.text)
            rdurl = transback['data']['authorization_url']

            account = Payment()
            account.user = user
            account.first_name = user.first_name
            account.last_name = user.last_name
            account.phone = phone
            account.amount = total/100
            account.paid = True
            account.pay_code = ref
            account.shop_code = shop_code
            account.save()
            return redirect(rdurl)
    return redirect('checkout')

@login_required(login_url='signin')
def callback(request):
    profile = Profile.objects.get(user__username = request.user.username)
    trolley = Cart.objects.filter(user__username = request.user.username, paid = False)
    payment = Payment.objects.filter(user__username = request.user.username, paid=True)

    for items in trolley:
        items.paid = True
        items.save()

        stock = Product.objects.get(pk = items.product_id)
        stock.max_quantity -= items.quantity
        stock.save()
    context = {
        'profile':profile,
    }

    return render(request, 'callback.html', context)


def search(request):
    if request.method == 'POST':
        items = request.POST['search']
        searched = Q(Q(name__icontains=items)|Q(price__icontains=items)|Q(slug__icontains=items))
        searched_items = Product.objects.filter(searched)

        context = {
            'items':items,
            'searched_items':searched_items,
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

@login_required(login_url='signin')
def history(request):
    profile = Profile.objects.get(user__username=request.user.username)
    bought = Cart.objects.filter(user__username=request.user.username, paid=True)

    subtotal = 0
    total = 0
    vat = 0

    for cart in bought:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'profile':profile,
        'bought':bought,
        'total':total,
    }
    return render(request, 'history.html', context)

@login_required(login_url='signin')
def del_history(request):
    history = request.POST['history']
    del_hist = Product.objects.filter(pk=history)
    del_hist.delete()
    messages.success(request, 'Del successfully')
    return redirect('history')