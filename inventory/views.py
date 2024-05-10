from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Service, Order

from django.utils import timezone

def home(request):
    return render(request, 'inventory/home.html')
    templates = loader.get_templates('base.html')
    return HttpResponse(templates.render(request)) 

def service_list(request):
    """
    View function to display a list of available services.
    """
    services = Service.objects.all()
    return render(request, 'inventory/service_list.html', {'services': services})

def clients(request):
    """
    View function to handle clients page.
    """
    # Your view logic here
    return render(request, 'inventory/clients.html')

def suppliers(request):
    """
    View function to handle suppliers page.
    """
    # Your view logic here
    return render(request, 'inventory/suppliers.html')

def materials(request):
    """
    View function to handle materials page.
    """
    # Your view logic here
    return render(request, 'inventory/materials.html')

def place_order(request):
    """
    View function to place a new order.
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_date = timezone.now()
            fulfill_order(order)
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'inventory/place_order.html', {'form': form})

def order_success(request):
    """
    View function to display a success message after placing an order.
    """
    return HttpResponse("Your order has been placed successfully.")

def inventory(request):
    """
    View function to handle inventory page.
    """
    # Your view logic here
    return render(request, 'inventory/inventory.html')

def fulfill_order(order):
    """
    Function to fulfill an order based on the provided order details.
    This function implements the order fulfillment logic as per the procedural design provided.
    It updates the inventory levels, calculates total amount, and processes the order.
    """
    # Get the service related to the order
    service = order.service
    # Calculate the total amount based on the quantity and service price
    total_amount = order.quantity * service.price
    # Update the order with the calculated total amount
    order.total_amount = total_amount
    # Save the order
    order.save()
    # Update the inventory level of the service (assuming it decreases after an order)
    service.inventory_level -= order.quantity
    service.save()

def notify_supplier(material_id, quantity):
    """
    Function to notify the supplier about low stock levels of a particular material.
    This function should implement the supplier notification logic.
    """
    # Assuming this function sends a notification to the supplier when material stock is low
    pass

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in successfully"))
            return redirect('home')
        else:
            messages.success(request, ("Incorrect username/password"))
            return redirect('login')

    else:

        return render(request, 'user/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')