import tkinter as tk
from tkinter import ttk

# Class to store customer information
class Customers:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reward_balance = 0
        self.past_purchases = []

# Class to display redemption messages
class RedeemPoints(tk.Toplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Redemption Message")
        self.geometry("400x250")
        # Set background color
        self.configure(bg='#81bbff')  
        # Customize message label
        self.message_label = tk.Label(self, text=message, font= ("Helvetica", 16), bg="#f2ee29")
        self.message_label.pack(pady=20)
        self.ok_button = tk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=10)

# Main Screen Window Set up into a class:
class MainScreen(tk.Tk):
    def __init__(self, title, size):
        # Main Screen Setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        
        # Configure the main grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        
        # Create Widgets
        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, sticky='nswe')
        
        # Store customers
        self.customers = {}
        
        # Run the MainScreen 
        self.mainloop()

class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg='#81bbff')
        
        # Configure the grid for the menu
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2), weight=1)
        
        self.customer_widgets()
    
    def customer_widgets(self):
        self.button1 = tk.Button(self, text='New Member', width=10, bg='#2936f2', fg='black', activebackground='yellow', activeforeground='black', font=("Helvetica", 14, "bold"), command=self.open_new_window)
        self.button2 = tk.Button(self, text='Existing Member', width=10, bg='#a715b5', fg='black', activebackground='yellow', activeforeground='black', font=("Helvetica", 14, "bold"), command=self.existing_member_window)
        self.button3 = tk.Button(self, text='Exit', width=10, bg='#f22943', fg='black', activebackground='yellow', activeforeground='black', font=("Helvetica", 14, "bold"), command=self.quit)
        
        # Place the widgets within the Menu with padding
        self.button1.grid(row=0, column=0, sticky='nswe', padx=20, pady=20)
        self.button2.grid(row=1, column=0, sticky='nswe', padx=20, pady=20)
        self.button3.grid(row=2, column=0, sticky='nswe', padx=20, pady=20)
        
    # Define functionalities of the new window that is opened upon click:    
    def open_new_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("New Member Registration")
        new_window.geometry("400x300")
        
        
        label = tk.Label(new_window, text="Enter your first and last name:")
        label.pack(pady=10)
        
        self.first_name_entry = tk.Entry(new_window)
        self.first_name_entry.pack(pady=5)
        
        self.last_name_entry = tk.Entry(new_window)
        self.last_name_entry.pack(pady=5)
        
        submit_button = tk.Button(new_window, text="Submit", command=lambda: self.submit_info(new_window))
        submit_button.pack(pady=10)
        
    # Define functionalities of the existing member window that is opened upon click:     
    def existing_member_window(self):
        self.existing_window = tk.Toplevel(self)
        self.existing_window.title("Existing Member Login")
        self.existing_window.geometry("600x625")
        self.existing_window.configure(bg='#81bbff')   # Set background color
        
        label = tk.Label(self.existing_window, text="Enter your first and last name:")
        label.pack(pady=10)
        
        self.text_box = tk.Text(self.existing_window, height=2, width=30)
        self.text_box.pack(pady=10)
        
        submit_button = tk.Button(self.existing_window, text="Submit", command=self.fetch_member_data)
        submit_button.pack(pady=10)
    
    def fetch_member_data(self):
        full_name = self.text_box.get("1.0", tk.END).strip()
        print("Existing member name:", full_name)
        
        if full_name in self.parent.customers:
            customer = self.parent.customers[full_name]
            self.reward_balance = customer.reward_balance
            self.past_purchases = customer.past_purchases
            self.display_member_data(customer)
        else:
            self.show_error("Member not found.", self.existing_window)
    
    def display_member_data(self, customer):
        for widget in self.existing_window.winfo_children():
            widget.destroy()
        
        name_label = tk.Label(self.existing_window, text=f"Welcome, {customer.first_name} {customer.last_name}!")
        name_label.pack(pady=10)
        
        reward_label = tk.Label(self.existing_window, text=f"Reward Balance: {customer.reward_balance} points")
        reward_label.pack(pady=10)
        
        purchases_label = tk.Label(self.existing_window, text="Past Purchases:")
        purchases_label.pack(pady=10)
        
        self.purchases_list = tk.Listbox(self.existing_window, height=10, width=30)
        for purchase in customer.past_purchases:
            self.purchases_list.insert(tk.END, purchase)
        self.purchases_list.pack(pady=10)
        
        self.add_items_to_purchase(customer)
        self.display_redeemable_items(customer)
        self.existing_window.update_idletasks()
    
    def add_items_to_purchase(self, customer):
        items = [("Latte", 10), ("Cappuccino", 8), ("Espresso", 5)]
        
        items_label = tk.Label(self.existing_window, text="Add Items to Purchase:")
        items_label.pack(pady=10)
        
        for item, points in items:
            button = tk.Button(self.existing_window, text=f"{item} - {points} points", command=lambda i=item, p=points: self.add_purchase(customer, i, p))
            button.pack(pady=5)
    
    def display_redeemable_items(self, customer):
        redeemable_items = [("Free Coffee", 50), ("Free Muffin", 30), ("Free Sandwich", 70)]
        
        redeem_label = tk.Label(self.existing_window, text="Redeem Rewards:")
        redeem_label.pack(pady=10)
        
        for item, points in redeemable_items:
            button = tk.Button(self.existing_window, text=f"{item} - {points} points", command=lambda i=item, p=points: self.redeem_rewards(customer, i, p))
            button.pack(pady=5)
    
    def add_purchase(self, customer, item, points):
        customer.past_purchases.append(item)
        customer.reward_balance += points
        self.display_member_data(customer)
    
    def redeem_rewards(self, customer, item, points_required):
        if customer.reward_balance >= points_required:
            customer.reward_balance -= points_required
            customer.past_purchases.append(f"Redeemed: {item}")
            self.display_member_data(customer)
            RedeemPoints(self, "Redemption successful!")
        else:
            RedeemPoints(self, "Insufficient reward points.")
    
    def submit_info(self, new_window):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        full_name = f"{first_name} {last_name}"
        
        if first_name and last_name:
            self.parent.customers[full_name] = Customers(first_name, last_name)
            thank_you_label = tk.Label(new_window, text="Thank you for joining Blue Moose Rewards!")
            thank_you_label.pack(pady=10)
            self.first_name_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
        else:
            self.show_error("Please enter both first and last names.", new_window)
    
    def show_error(self, message, window):
        error_label = tk.Label(window, text=message)
        error_label.pack(pady=10)
    
    def show_message(self, message, window):
        message_label = tk.Label(window, text=message)
        message_label.pack(pady=10)

# Example usage
if __name__ == "__main__":
    app = MainScreen("Blue Moose Coffee Rewards", (700, 700))
        



        

    
  
   
   



