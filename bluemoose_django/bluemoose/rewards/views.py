from django.shortcuts import render, redirect
from .models import Customer

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']  # Add this line

        if first_name and last_name and phone_number:  # Include phone_number in the check
            customer = Customer(first_name=first_name, last_name=last_name, phone_number=phone_number)  # Add phone_number here
            customer.save()
            return redirect('success_page')  # Redirect to a success page or the main page

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        try:
            customer = Customer.objects.get(first_name=full_name.split()[0], last_name=full_name.split()[1])
            return render(request, 'member_data.html', {'customer': customer})
        except Customer.DoesNotExist:
            return render(request, 'login.html', {'error': "Member not found."})
    return render(request, 'login.html')

def success_page(request):
    return render(request, 'success.html')

def index(request):
    return render(request, 'index.html')