import tkinter as tk
from tkinter import messagebox

class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.points = 10  # Starting points
        self.purchase_history = []
    
    def add_purchase(self, amount):
        points_earned = amount  # 1 point per dollar spent
        self.points += points_earned
        self.purchase_history.append(amount)
    
    def redeem_points(self, points_to_redeem):
        if self.points >= points_to_redeem:
            self.points -= points_to_redeem
            return True
        return False

class RewardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blue Moose Coffee Lounge Rewards Program")
        
        self.customers = {}
        
        # Main Menu
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20, padx=20)
        
        tk.Label(self.main_frame, text="Input Customer Phone Number").grid(row=0, column=0, columnspan=2)
        self.input_entry = tk.Entry(self.main_frame)
        self.input_entry.grid(row=1, column=0, columnspan=2)
        
        self.check_button = tk.Button(self.main_frame, text="Check Account", command=self.check_account)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.register_button = tk.Button(self.main_frame, text="Register New Customer", command=self.open_registration_window)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def open_registration_window(self):
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title("Register New Customer")
        
        tk.Label(self.registration_window, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.registration_window)
        self.name_entry.grid(row=0, column=1)
        
        tk.Label(self.registration_window, text="Phone Number").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.registration_window)
        self.phone_entry.grid(row=1, column=1)
        
        self.register_button = tk.Button(self.registration_window, text="Register", command=self.register_customer)
        self.register_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def register_customer(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        
        if not name or not phone_number:
            messagebox.showerror("Error", "Please fill out all fields.")
            return
        
        if phone_number in self.customers:
            messagebox.showerror("Error", "Customer already registered.")
        else:
            self.customers[phone_number] = Customer(name, phone_number)
            messagebox.showinfo("Success", f"Customer {name} registered successfully!")
            self.registration_window.destroy()
    
    def check_account(self):
        phone_number = self.input_entry.get()
        
        if phone_number not in self.customers:
            messagebox.showerror("Error", "Customer not found.")
        else:
            self.open_account_window(self.customers[phone_number])
    
    def open_account_window(self, customer):
        self.account_window = tk.Toplevel(self.root)
        self.account_window.title("Customer Account")
        
        # Display Customer Info
        tk.Label(self.account_window, text=f"Customer: {customer.name}").grid(row=0, column=0, columnspan=2)
        tk.Label(self.account_window, text=f"Points Balance: {customer.points}").grid(row=1, column=0, columnspan=2)
        
        tk.Label(self.account_window, text="Amount Spent:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.account_window)
        self.amount_entry.grid(row=2, column=1)
        
        self.add_points_button = tk.Button(self.account_window, text="Add Points", command=lambda: self.add_points(customer))
        self.add_points_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.withdraw_rewards_button = tk.Button(self.account_window, text="Withdraw Rewards", command=lambda: self.withdraw_rewards(customer))
        self.withdraw_rewards_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.rewards_label = tk.Label(self.account_window, text="Rewards:\n1. Free Coffee - 10 points\n2. Discounted Pastry - 20 points")
        self.rewards_label.grid(row=5, column=0, columnspan=2)
    
    def add_points(self, customer):
        try:
            amount_spent = float(self.amount_entry.get())
            if amount_spent <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return
        
        customer.add_purchase(amount_spent)
        messagebox.showinfo("Success", f"Added points for ${amount_spent:.2f}. Total Points: {customer.points}")
    
    def withdraw_rewards(self, customer):
        rewards = {
            "Free Coffee": 10,
            "Discounted Pastry": 20
        }
        
        reward_menu = "\n".join([f"{reward}: {points} points" for reward, points in rewards.items()])
        
        self.withdraw_window = tk.Toplevel(self.root)
        self.withdraw_window.title("Withdraw Rewards")
        
        tk.Label(self.withdraw_window, text=f"Available Rewards:\n{reward_menu}").grid(row=0, column=0, columnspan=2)
        
        tk.Label(self.withdraw_window, text="Enter Reward Name:").grid(row=1, column=0)
        self.reward_entry = tk.Entry(self.withdraw_window)
        self.reward_entry.grid(row=1, column=1)
        
        self.withdraw_button = tk.Button(self.withdraw_window, text="Withdraw", command=lambda: self.process_withdraw(customer))
        self.withdraw_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def process_withdraw(self, customer):
        rewards = {
            "Free Coffee": 10,
            "Discounted Pastry": 20
        }
        
        reward_name = self.reward_entry.get()
        
        if reward_name not in rewards:
            messagebox.showerror("Error", "Invalid reward name.")
            return
        
        points_required = rewards[reward_name]
        
        if customer.redeem_points(points_required):
            messagebox.showinfo("Success", f"Reward '{reward_name}' redeemed. Remaining Points: {customer.points}")
            self.withdraw_window.destroy()
        else:
            messagebox.showerror("Error", "Insufficient points.")

def run_tkinter_gui():
    root = tk.Tk()
    app = RewardsApp(root)
    root.mainloop()

run_tkinter_gui()
