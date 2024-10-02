from django.shortcuts import render, redirect
from .models import Customer
from .forms import RegistrationForm, LoginForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            # Create a new customer and hash their password
            customer = Customer(first_name=first_name, last_name=last_name, phone_number=phone_number)
            customer.set_password(password)  # Hashing the password
            customer.save()
            
            return redirect('success_page')  # Redirect to a success page or the main page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(phone_number=phone_number)
                if customer.check_password(password):  # Check the password
                    return redirect('thank_you')  # Redirect to a successful login page
                else:
                    form.add_error(None, "Incorrect password.")
            except Customer.DoesNotExist:
                form.add_error(None, "No account found with that phone number.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    
def success_page(request):
    return render(request, 'success.html')

def index(request):
    return render(request, 'index.html')
