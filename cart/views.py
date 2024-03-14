from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_details(request, tot=0, count=0, cart_items=None):
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        cart_items = Items.objects.filter(cart=ct, active=True)
        for i in cart_items:
            tot += (i.product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ci': cart_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = Products.objects.get(id=product_id)
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = Items.objects.get(product=prod, cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(product=prod, cart=ct, quantity=1)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(product=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(product=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')
