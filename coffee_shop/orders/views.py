from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeType, Order

def coffee_list(request):
    coffees = CoffeeType.objects.all()
    return render(request, 'orders/coffee_list.html', {'coffees': coffees})

def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(CoffeeType, id=coffee_id)
    
    if request.method == "POST":
        customer_name = request.POST.get('customer_name', 'Guest')  # Get customer name from form
        quantity = int(request.POST['quantity'])
        total_price = quantity * coffee.price

        # Save the order with customer name
        Order.objects.create(
            coffee=coffee, 
            customer_name=customer_name, 
            quantity=quantity, 
            total_price=total_price
        )

        return redirect('cart')  # Redirect to cart page

    return render(request, 'orders/add_to_cart.html', {'coffee': coffee})

def cart(request):
    orders = Order.objects.all()
    total = sum(order.total_price for order in orders)
    return render(request, 'orders/cart.html', {'orders': orders, 'total': total})

def clear_cart(request):
    Order.objects.all().delete()
    return redirect('cart')

def generate_bill(request):
    orders = Order.objects.all()
    total = sum(order.total_price for order in orders)
    return render(request, 'orders/bill.html', {'orders': orders, 'total': total})
