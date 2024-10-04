from django.shortcuts import render, redirect
from .models import Customer,RedeemableItem, PurchasableItem, Order
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import logout

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
                    request.session['customer_id'] = customer.id  # Store customer ID in session
                    return redirect('member_data')  # Redirect to member data page
                else:
                    form.add_error(None, "Incorrect password.")
            except Customer.DoesNotExist:
                form.add_error(None, "No account found with that phone number.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def member_data(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')  # Redirect to login if not logged in

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return redirect('login')  # Redirect to login if customer not found

    redeemable_items = RedeemableItem.objects.all()
    purchasable_items = PurchasableItem.objects.all()

    if request.method == 'POST':
        message = ""
        # Redeem item logic
        if 'redeem_item' in request.POST:
            item_id = request.POST.get('item_id')
            try:
                item = RedeemableItem.objects.get(id=item_id)
                if customer.reward_balance >= item.points_required:
                    customer.reward_balance -= item.points_required
                    customer.save()
                    message = f"You have successfully redeemed {item.name}!"
                else:
                    message = "You do not have enough points to redeem this item."
            except RedeemableItem.DoesNotExist:
                message = "The redeemable item does not exist."

        # Purchase item logic
        elif 'purchase_item' in request.POST:
            item_id = request.POST.get('item_id')
            try:
                item = PurchasableItem.objects.get(id=item_id)
                quantity = int(request.POST.get('quantity', 1))
                total_price = item.price * quantity
                points_earned = item.points_earned * quantity

                # Create an order
                order = Order(customer=customer, item=item, quantity=quantity, total_price=total_price, points_earned=points_earned)
                order.save()

                # Add points to the customer's reward balance
                customer.reward_balance += points_earned
                customer.save()

                message = f"You have successfully purchased {quantity}x {item.name}! You earned {points_earned} points."
            except PurchasableItem.DoesNotExist:
                message = "The purchasable item does not exist."

        return render(request, 'member_data.html', {
            'customer': customer,
            'redeemable_items': redeemable_items,
            'purchasable_items': purchasable_items,
            'message': message
        })

    return render(request, 'member_data.html', {
        'customer': customer,
        'redeemable_items': redeemable_items,
        'purchasable_items': purchasable_items
    })
    
def purchase_item(request, item_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')  # Redirect to login if not logged in

    try:
        customer = Customer.objects.get(id=customer_id)
        item = PurchasableItem.objects.get(id=item_id)
        
        # Create an order
        order = Order(customer=customer, item=item)
        order.save()

        # Update the customer's reward points
        customer.reward_balance += item.reward_points
        customer.save()

        return redirect('member_data')  # Redirect back to member data after purchase
        
    except PurchasableItem.DoesNotExist:
        return redirect('member_data')  # Item doesn't exist, redirect back

    except Customer.DoesNotExist:
        return redirect('login')
    
def redeem_item(request, item_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')  # Redirect to login if not logged in

    try:
        customer = Customer.objects.get(id=customer_id)
        item = RedeemableItem.objects.get(id=item_id)
        
        if customer.reward_balance >= item.point_cost:
            customer.reward_balance -= item.point_cost
            customer.save()
            # Optionally: Log the redemption (e.g. in past purchases or an order history)
            return redirect('member_data')  # Redirect to member_data after redeeming
        else:
            # Insufficient points
            return render(request, 'insufficient_points.html', {'customer': customer, 'item': item})
        
    except RedeemableItem.DoesNotExist:
        return redirect('member_data')  # Item doesn't exist, redirect back

    except Customer.DoesNotExist:
        return redirect('login')
    
def success_page(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the index page after logging out

