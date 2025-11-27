import database_handler

#required fuctions
def get_customer_info():
    pass

def compute_bill(kwh_used):
    """
    Computes the electric bill based on tiered rates.
    computation of bill = ((kWh * Tiered_rate) + enviromental_fee) * (1 + vat)
    
    Parameters:
        kwh_used (float): Total kWh consumed
        
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
    vat = subtotal * 0.12
    total_amount_due = subtotal + vat
    
    # Return breakdown as dictionary
    return {
        'base_charge': base_charge,
        'environmental_fee': environmental_fee,
        'vat': vat,
        'total_amount_due': total_amount_due
    }

def display_bill():
    pass

if __name__ == "__main__":
    print(compute_bill(145))
