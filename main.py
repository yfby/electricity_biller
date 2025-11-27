import database_handler

# Initialize database
db = database_handler.data_handler("customer.db")

def get_customer_info():
    """Get customer information from database"""
    print("\n" + "="*50)
    print("GET CUSTOMER INFORMATION")
    print("="*50)
    
    account_number = input("Enter account number: ").strip()
    
    if not account_number.isdigit():
        print("✗ Invalid account number!")
        return None
    
    customer = db.get_customer(int(account_number))
    
    if customer:
        print(f"\n{'Account Number:':<20} {customer['account_number']}")
        print(f"{'Customer Name:':<20} {customer['name']}")
        print(f"{'Address:':<20} {customer['address']}")
        print(f"{'Customer Type:':<20} {customer['type']}")
        print(f"{'Discount:':<20} {customer['discount']}")
        print(f"{'Current Usage:':<20} {customer['usage']} kWh")
        print(f"{'All-Time Usage:':<20} {customer['all_time_usage']} kWh")
        print()
        return customer
    else:
        print(f"✗ Account number {account_number} not found!")
        return None

def compute_bill(kwh_used, discount_type="None"):
    """
    Computes the electric bill based on tiered rates with discount.
    bill = (((kWh * Tiered_rate) + environmental_fee) - discount) * (1 + vat)
    
    Parameters:
        kwh_used (float): Total kWh consumed
        discount_type (str): Type of discount (None, Senior Citizen, PWD, Low-income)
        
    Returns:
        dict: Dictionary containing bill breakdown
    """
    base_charge = 0.0
    rate = 0.0
    """
    # Tiered rate calculation
    Consumption (kWh) Rate (₱ per kWh)
    0–50                5.00
    51–100              6.50
    101–200             8.00
    201 and above       10.00
    
    # Discount rates
    Senior Citizen: 5% off subtotal
    PWD: 5% off subtotal
    Low-income: 10% off subtotal
    """
    if kwh_used <= 50:      # 0-50 kWh
        rate = 5.00
    elif kwh_used <= 100:   # 51-100 kWh
        rate = 6.50
    elif kwh_used <= 200:   # 101-200 kWh
        rate = 8.00
    else:                   # 201 kWh and above
        rate = 10.00
    
    # Computation
    # Base Charge
    base_charge = kwh_used * rate
    
    # Additional charges
    environmental_fee = 50.00
    subtotal = base_charge + environmental_fee
    
    # Apply discount
    discount_rates = {
        "None": 0.0,
        "Senior Citizen": 0.05,  # 5% discount
        "PWD": 0.05,             # 5% discount
        "Low-income": 0.10       # 10% discount
    }
    
    discount_rate = discount_rates.get(discount_type, 0.0)
    discount_amount = subtotal * discount_rate
    subtotal_after_discount = subtotal - discount_amount
    
    # VAT
    vat = subtotal_after_discount * 0.12
    total_amount_due = subtotal_after_discount + vat
    
    # Return breakdown as dictionary
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

def display_bill(customer, bill_info):
    """Display formatted bill"""
    print("\n" + "="*60)
    print("ELECTRICITY BILL".center(60))
    print("="*60)
    print(f"\nAccount Number: {customer['account_number']}")
    print(f"Customer Name:  {customer['name']}")
    print(f"Address:        {customer['address']}")
    print(f"Customer Type:  {customer['type']}")
    print(f"Discount Type:  {customer['discount']}")
    print("\n" + "-"*60)
    print("CONSUMPTION DETAILS")
    print("-"*60)
    print(f"kWh Used:       {bill_info['kwh_used']:.2f} kWh")
    print(f"Rate:           ₱{bill_info['rate']:.2f} per kWh")
    print()
    print("-"*60)
    print("CHARGES BREAKDOWN")
    print("-"*60)
    print(f"Base Charge:             ₱{bill_info['base_charge']:>10.2f}")
    print(f"Environmental Fee:       ₱{bill_info['environmental_fee']:>10.2f}")
    print(f"Subtotal:                ₱{bill_info['subtotal']:>10.2f}")
    
    # Show discount if applicable
    if bill_info['discount_amount'] > 0:
        discount_percent = int(bill_info['discount_rate'] * 100)
        print(f"Discount ({bill_info['discount_type']} {discount_percent}%): -₱{bill_info['discount_amount']:>10.2f}")
        print(f"Subtotal after discount: ₱{bill_info['subtotal_after_discount']:>10.2f}")
    
    print(f"VAT (12%):               ₱{bill_info['vat']:>10.2f}")
    print("-"*60)
    print(f"TOTAL AMOUNT DUE:        ₱{bill_info['total_amount_due']:>10.2f}")
    print("="*60 + "\n")

def create_new_account():
    """Create a new customer account"""
    print("\n" + "="*50)
    print("CREATE NEW ACCOUNT")
    print("="*50)
    
    name = input("Customer Name: ").strip()
    address = input("Address: ").strip()
    
    print("\nCustomer Types:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    type_choice = input("Select type (1-3): ").strip()
    
    types = {"1": "Residential", "2": "Commercial", "3": "Industrial"}
    cust_type = types.get(type_choice, "Residential")
    
    print("\nDiscount Types:")
    print("1. None")
    print("2. Senior Citizen")
    print("3. PWD")
    print("4. Low-income")
    discount_choice = input("Select discount (1-4): ").strip()
    
    discounts = {"1": "None", "2": "Senior Citizen", "3": "PWD", "4": "Low-income"}
    discount = discounts.get(discount_choice, "None")
    
    account_number = db.create_account(name, address, cust_type, discount)
    return account_number

def bill_customer():
    """Bill a customer and display their bill"""
    print("\n" + "="*50)
    print("BILL CUSTOMER")
    print("="*50)
    
    account_number = input("Enter account number: ").strip()
    
    if not account_number.isdigit():
        print("✗ Invalid account number!")
        return
    
    customer = db.get_customer(int(account_number))
    
    if not customer:
        print(f"✗ Account number {account_number} not found!")
        return
    
    try:
        kwh_used = float(input("Enter kWh used: "))
        if kwh_used < 0:
            print("✗ Usage cannot be negative!")
            return
    except ValueError:
        print("✗ Invalid usage value!")
        return
    
    # Compute bill with customer's discount
    bill_info = compute_bill(kwh_used, customer['discount'])
    
    # Update usage in database
    db.update_usage(int(account_number), kwh_used)
    
    # Display bill
    display_bill(customer, bill_info)

def list_all_customers():
    """List all customers"""
    print("\n" + "="*90)
    print("ALL CUSTOMERS")
    print("="*90)
    
    customers = db.get_all_customers()
    
    if not customers:
        print("No customers found!")
        return
    
    print(f"{'Account':<10} {'Name':<25} {'Type':<15} {'Usage':<10} {'Total Usage':<12}")
    print("-"*90)
    
    for customer in customers:
        print(f"{customer['account_number']:<10} {customer['name']:<25} "
              f"{customer['type']:<15} {customer['usage']:<10} {customer['all_time_usage']:<12}")
    
    print("="*90 + "\n")

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*50)
        print("ELECTRICITY BILLING SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Get Customer Information")
        print("3. Bill Customer")
        print("4. List All Customers")
        print("5. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            create_new_account()
        elif choice == "2":
            get_customer_info()
        elif choice == "3":
            bill_customer()
        elif choice == "4":
            list_all_customers()
        elif choice == "5":
            print("\nThank you for using the Electricity Billing System!")
            db.close()
            break
        else:
            print("✗ Invalid choice! Please try again.")

if __name__ == "__main__":
    # You can run the menu system
    main_menu()
    
    # Or test individual functions with discount:
    # print(compute_bill(145, "Senior Citizen"))  # With 5% discount
    # print(compute_bill(145, "Low-income"))      # With 10% discount
    # print(compute_bill(145))                     # No discount
