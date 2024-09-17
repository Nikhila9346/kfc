from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Menu, Cart

# Create your views here.

def home(request):
    m = Category.objects.all()

    context = {
        'category': m,
        'count': count_cart()
    }
    return render(request, 'home.html', context)

def add_to_cart(request,id):
    food = Menu.objects.get(id=id)
    #if the item is already present simply increase the quantity(qty) by one
    try:
        c = Cart.objects.get(item = food.item)
        c.qty += 1
        c.total = c.qty * c.price
        c.save()
    #if not add the item to the table
    except:
        Cart.objects.create(
        item = food.item,
        qty = 1,
        price = food.price,
        total = food.price,
        )
    return redirect('home')

def food_item(request, id):
    return render(request, 'food_item.html')


def cart(request):
    c = Cart.objects.all()
    
    total = 0
    for i in c:
        total += i.total
    context ={
        'cart':c,
        'final_total': total
    }
    return render(request, 'cart.html', context)

def count_cart():
    count = Cart.objects.all().count()
    return count

def delete_from_cart(request, id):
    c = Cart.objects.get(id=id)
    c.delete()
    return redirect('cart')

def remove_qty(request, id):
    c =  Cart.objects.get(id=id)
    if c.qty!=1:
        c.qty -= 1
        c.total -= c.price
        c.save()
    else:
        c.delete()
    return redirect('cart')

def add_qty(request, id):
    c =  Cart.objects.get(id=id)
    c.qty += 1
    c.total += c.price
    c.save()
    return redirect('cart')

