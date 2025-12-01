import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import database_handler

class ElectricityBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Billing System")
        self.root.geometry("900x600")
        self.root.minsize(900, 600)
        self.root.resizable(True, True)
        
        # Initialize database
        self.db = database_handler.data_handler("customer.db")
        
        # Configure colors
        self.bg_color = "#eff1f5"
        self.primary_color = "#df8e1d"
        self.secondary_color = "#04a5e5"
        self.accent_color = "#40a02b"
        
        self.root.configure(bg=self.bg_color)
        
        # Create main container
        self.create_header()
        self.create_main_menu()
        
    def create_header(self):
        """Create header section"""
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="⚡ ELECTRICITY BILLING SYSTEM",
            font=("Georgia", 24, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=20)
        
    def create_main_menu(self):
        """Create main menu with buttons"""
        # Clear previous content
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()
            
        menu_frame = tk.Frame(self.root, bg=self.bg_color)
        menu_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        buttons_info = [
            ("➕ Create New Account", self.show_create_account, self.accent_color),
            ("👤 Get Customer Information", self.show_get_customer_info, self.secondary_color),
            ("💰 Bill Customer", self.show_bill_customer, self.secondary_color),
            ("📋 List All Customers", self.show_all_customers, self.secondary_color),
            ("❌ Exit", self.exit_app, "#e74c3c")
        ]
        
        for i, (text, command, color) in enumerate(buttons_info):
            btn = tk.Button(
                menu_frame,
                text=text,
                font=("Arial", 14, "bold"),
                bg=color,
                fg="white",
                width=30,
                height=2,
                cursor="hand2",
                command=command,
                relief=tk.FLAT
            )
            btn.pack(pady=10)
     
    #         # Hover effects (not very useful)
    #         btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self._darken_color(b.cget("bg"))))
    #         btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))
    # 
    # def _darken_color(self, color):
    #     """Darken a color for hover effect"""
    #     color_map = {
    #         "#27ae60": "#229954",
    #         "#3498db": "#2980b9",
    #         "#e74c3c": "#c0392b"
    #     }
    #     return color_map.get(color, color)
    
    def create_back_button(self, parent):
        """Create back button"""
        back_btn = tk.Button(
            parent,
            text="← Back to Menu",
            font=("Arial", 10),
            bg=self.primary_color,
            fg="white",
            cursor="hand2",
            command=self.create_main_menu,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        back_btn.pack(anchor=tk.W, padx=20, pady=10)
        
    def show_create_account(self):
        """Show create account form"""
        # Clear previous content
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()
            
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        self.create_back_button(main_frame)
        
        # Form container
        form_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        form_frame.pack(padx=100, pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            form_frame,
            text="Create New Account",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Input fields
        fields_frame = tk.Frame(form_frame, bg="white")
        fields_frame.pack(pady=10)
        
        # Name
        tk.Label(fields_frame, text="Customer Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)
        name_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        name_entry.grid(row=0, column=1, padx=20, pady=10)
        
        # Address
        tk.Label(fields_frame, text="Address:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky=tk.W, padx=20, pady=10)
        address_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        address_entry.grid(row=1, column=1, padx=20, pady=10)
        
        # Customer Type
        tk.Label(fields_frame, text="Customer Type:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky=tk.W, padx=20, pady=10)
        type_var = tk.StringVar(value="Residential")
        type_combo = ttk.Combobox(fields_frame, textvariable=type_var, font=("Arial", 12), width=28, state="readonly")
        type_combo['values'] = ("Residential", "Commercial", "Industrial")
        type_combo.grid(row=2, column=1, padx=20, pady=10)
        
        # Discount
        tk.Label(fields_frame, text="Discount Type:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky=tk.W, padx=20, pady=10)
        discount_var = tk.StringVar(value="None")
        discount_combo = ttk.Combobox(fields_frame, textvariable=discount_var, font=("Arial", 12), width=28, state="readonly")
        discount_combo['values'] = ("None", "Senior Citizen", "PWD", "Low-income")
        discount_combo.grid(row=3, column=1, padx=20, pady=10)
        
        # Submit button
        def submit_account():
            name = name_entry.get().strip()
            address = address_entry.get().strip()
            cust_type = type_var.get()
            discount = discount_var.get()
            
            if not name or not address:
                messagebox.showerror("Error", "Please fill in all fields!")
                return
            
            account_number = self.db.create_account(name, address, cust_type, discount)
            if account_number:
                messagebox.showinfo(
                    "Success",
                    f"Account created successfully!\n\nAccount Number: {account_number}\nCustomer: {name}"
                )
                self.create_main_menu()
        
        submit_btn = tk.Button(
            form_frame,
            text="Create Account",
            font=("Arial", 14, "bold"),
            bg=self.accent_color,
            fg="white",
            cursor="hand2",
            command=submit_account,
            relief=tk.FLAT,
            padx=30,
            pady=10
        )
        submit_btn.pack(pady=20)
    
    def show_get_customer_info(self):
        """Show customer information lookup"""
        # Clear previous content
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()
            
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        self.create_back_button(main_frame)
        
        # Form container
        form_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        form_frame.pack(padx=100, pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            form_frame,
            text="Get Customer Information",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Account number input
        input_frame = tk.Frame(form_frame, bg="white")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Account Number:", font=("Arial", 12), bg="white").pack(side=tk.LEFT, padx=10)
        account_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        account_entry.pack(side=tk.LEFT, padx=10)
        
        # Result display
        result_text = scrolledtext.ScrolledText(form_frame, font=("Courier", 11), height=15, width=60)
        result_text.pack(pady=20, padx=20)
        result_text.config(state=tk.DISABLED)
        
        def search_customer():
            account_num = account_entry.get().strip()
            
            if not account_num.isdigit():
                messagebox.showerror("Error", "Invalid account number!")
                return
            
            customer = self.db.get_customer(int(account_num))
            
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            
            if customer:
                info = f"""
{'='*50}
CUSTOMER INFORMATION
{'='*50}

Account Number:    {customer['account_number']}
Customer Name:     {customer['name']}
Address:           {customer['address']}
Customer Type:     {customer['type']}
Discount:          {customer['discount']}
Current Usage:     {customer['usage']} kWh
All-Time Usage:    {customer['all_time_usage']} kWh

{'='*50}
"""
                result_text.insert(1.0, info)
            else:
                result_text.insert(1.0, f"\n❌ Account number {account_num} not found!")
            
            result_text.config(state=tk.DISABLED)
        
        search_btn = tk.Button(
            input_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg=self.secondary_color,
            fg="white",
            cursor="hand2",
            command=search_customer,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        search_btn.pack(side=tk.LEFT, padx=10)
    
    def show_bill_customer(self):
        """Show billing form"""
        # Clear previous content
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()
            
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        self.create_back_button(main_frame)
        
        # Form container
        form_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        form_frame.pack(padx=100, pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            form_frame,
            text="Bill Customer",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Input fields
        input_frame = tk.Frame(form_frame, bg="white")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Account Number:", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)
        account_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        account_entry.grid(row=0, column=1, padx=20, pady=10)
        
        tk.Label(input_frame, text="kWh Used:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky=tk.W, padx=20, pady=10)
        kwh_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        kwh_entry.grid(row=1, column=1, padx=20, pady=10)
        
        # Bill display
        bill_text = scrolledtext.ScrolledText(form_frame, font=("Courier", 10), height=20, width=70)
        bill_text.pack(pady=20, padx=20)
        bill_text.config(state=tk.DISABLED)
        
        def generate_bill():
            account_num = account_entry.get().strip()
            kwh_str = kwh_entry.get().strip()
            
            if not account_num.isdigit():
                messagebox.showerror("Error", "Invalid account number!")
                return
            
            try:
                kwh_used = float(kwh_str)
                if kwh_used < 0:
                    messagebox.showerror("Error", "Usage cannot be negative!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid kWh value!")
                return
            
            customer = self.db.get_customer(int(account_num))
            
            if not customer:
                messagebox.showerror("Error", f"Account number {account_num} not found!")
                return
            
            # Compute bill
            bill_info = self.compute_bill(kwh_used, customer['discount'])
            
            # Update database
            self.db.update_usage(int(account_num), kwh_used)
            
            # Display bill
            bill_text.config(state=tk.NORMAL)
            bill_text.delete(1.0, tk.END)
            
            bill_display = f"""
{'='*60}
{'ELECTRICITY BILL'.center(60)}
{'='*60}

Account Number: {customer['account_number']}
Customer Name:  {customer['name']}
Address:        {customer['address']}
Customer Type:  {customer['type']}
Discount Type:  {customer['discount']}

{'-'*60}
CONSUMPTION DETAILS
{'-'*60}
kWh Used:       {bill_info['kwh_used']:.2f} kWh
Rate:           ₱{bill_info['rate']:.2f} per kWh

{'-'*60}
CHARGES BREAKDOWN
{'-'*60}
Base Charge:             ₱{bill_info['base_charge']:>10.2f}
Environmental Fee:       ₱{bill_info['environmental_fee']:>10.2f}
Subtotal:                ₱{bill_info['subtotal']:>10.2f}"""

            if bill_info['discount_amount'] > 0:
                discount_percent = int(bill_info['discount_rate'] * 100)
                bill_display += f"""
Discount ({bill_info['discount_type']} {discount_percent}%): -₱{bill_info['discount_amount']:>10.2f}
Subtotal after discount: ₱{bill_info['subtotal_after_discount']:>10.2f}"""
            
            bill_display += f"""
VAT (12%):               ₱{bill_info['vat']:>10.2f}
{'-'*60}
TOTAL AMOUNT DUE:        ₱{bill_info['total_amount_due']:>10.2f}
{'='*60}
"""
            
            bill_text.insert(1.0, bill_display)
            bill_text.config(state=tk.DISABLED)
            
            messagebox.showinfo("Success", "Bill generated successfully!")
        
        submit_btn = tk.Button(
            input_frame,
            text="Generate Bill",
            font=("Arial", 12, "bold"),
            bg=self.accent_color,
            fg="white",
            cursor="hand2",
            command=generate_bill,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        submit_btn.grid(row=2, column=0, columnspan=2, pady=20)
    
    def compute_bill(self, kwh_used, discount_type="None"):
        """Compute bill with discount"""
        if kwh_used <= 50:
            rate = 5.00
        elif kwh_used <= 100:
            rate = 6.50
        elif kwh_used <= 200:
            rate = 8.00
        else:
            rate = 10.00
        
        base_charge = kwh_used * rate
        environmental_fee = 50.00
        subtotal = base_charge + environmental_fee
        
        discount_rates = {
            "None": 0.0,
            "Senior Citizen": 0.05,
            "PWD": 0.05,
            "Low-income": 0.10
        }
        
        discount_rate = discount_rates.get(discount_type, 0.0)
        discount_amount = subtotal * discount_rate
        subtotal_after_discount = subtotal - discount_amount
        
        vat = subtotal_after_discount * 0.12
        total_amount_due = subtotal_after_discount + vat
        
        return {
            'kwh_used': kwh_used,
            'rate': rate,
            'base_charge': base_charge,
            'environmental_fee': environmental_fee,
            'subtotal': subtotal,
            'discount_type': discount_type,
            'discount_rate': discount_rate,
            'discount_amount': discount_amount,
            'subtotal_after_discount': subtotal_after_discount,
            'vat': vat,
            'total_amount_due': total_amount_due
        }
    
    def show_all_customers(self):
        """Show all customers in a table"""
        # Clear previous content
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()
            
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        self.create_back_button(main_frame)
        
        # Table container
        table_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        table_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(
            table_frame,
            text="All Customers",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # Create Treeview
        tree_frame = tk.Frame(table_frame, bg="white")
        tree_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Treeview
        tree = ttk.Treeview(
            tree_frame,
            columns=("Account", "Name", "Type", "Discount", "Usage", "Total Usage"),
            show="headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            height=15
        )
        
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        
        # Configure columns
        tree.heading("Account", text="Account #")
        tree.heading("Name", text="Customer Name")
        tree.heading("Type", text="Type")
        tree.heading("Discount", text="Discount")
        tree.heading("Usage", text="Usage (kWh)")
        tree.heading("Total Usage", text="Total Usage (kWh)")
        
        tree.column("Account", width=100, anchor=tk.CENTER)
        tree.column("Name", width=200)
        tree.column("Type", width=120)
        tree.column("Discount", width=120)
        tree.column("Usage", width=100, anchor=tk.CENTER)
        tree.column("Total Usage", width=130, anchor=tk.CENTER)
        
        # Get all customers
        customers = self.db.get_all_customers()
        
        for customer in customers:
            tree.insert("", tk.END, values=(
                customer['account_number'],
                customer['name'],
                customer['type'],
                customer['discount'],
                customer['usage'],
                customer['all_time_usage']
            ))
        
        # Pack scrollbars and tree
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Total count
        count_label = tk.Label(
            table_frame,
            text=f"Total Customers: {len(customers)}",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        count_label.pack(pady=10)
    
    def exit_app(self):
        """Exit application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.db.close()
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricityBillingApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    root.mainloop()
