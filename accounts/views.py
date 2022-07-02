from django.shortcuts import render, redirect
from . import models
from . import forms

# DASHBOARD/ HOME PAGE VIEW

def home(request):
    # Status
    orders = models.Order.objects.all()
    total_order = (len(orders))
    pending = 0
    delivered = 0
    for item in orders:
        if item.status =='Pending':
            pending +=1
        if item.status =='Delivered':
            delivered +=1   
    
    # Dashboard
    customers = models.Customer.objects.all()

    context = { 'orders':orders, 
                'total_order': total_order, 
                'pending': pending, 
                'delivered': delivered, 
                'customers': customers
               }             
    return render(request, 'accounts/dashboard.html', context=context)

# PRODUCTS PAGE VIEW

def products(request):
    products = models.Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

# CUSTOMERS PAGE VIEW

def customers(request, pk):
    customer = models.Customer.objects.get(id = pk)
    order = customer.order_set.all()

    context = {'customer': customer,
               'order': order     
              }
    return render(request, 'accounts/customers.html', context)


# CRUD OPERATIONS

def create_order(request):
    form = forms.OrderForm()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)  
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')  
    context = {
        'form': form
    }
    return render(request, 'accounts/create_order.html', context)


def update(request, pk):
    info = models.Order.objects.get(id=pk)
    form = forms.OrderForm(instance=info) 
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=info)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/dashboard/')  
    context = {
        'form': form,
        'info':info
    }
    return render(request, 'accounts/update.html',context)