# Electricity Billing System

***A user-friendly desktop application for electricity billing operations with customer management, automated bill calculation, and comprehensive record-keeping.***

## Project Status

### **MVP Features** ✅
- ✅ Customer Database
- ✅ Calculate Function
- ✅ UI & Input validation
- ✅ Comments and Documentation

### **Bonus Features** ✅
- ✅ GUI using Tkinter
- ✅ Save bills (TXT & PDF)
- ✅ Load previous bills
- ✅ Multiple customers
- ✅ Discount options (Senior Citizen, PWD, Low-income)

---

## Installation

### Requirements
- Python 3.7 or higher

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## Features

### 1. **Create New Account**
Register customers with name, address, type (Residential/Commercial/Industrial), and discount eligibility.

### 2. **Customer Information**
Search and view customer details by account number.

### 3. **Bill Generation**
- Input electricity usage (kWh)
- Automatic tiered pricing calculation
- Apply discounts and taxes
- Save as TXT or PDF

### 4. **View All Customers**
Browse all customers in a table. Click any row to copy the account number.

### 5. **Previous Bills**
View saved bills sorted by date. Double-click to open.

---

## How to Use

### Creating an Account
1. Click "Create New Account"
2. Fill in customer details
3. Select customer type and discount
4. Click "Create Account"

### Generating a Bill
1. Click "Bill Customer"
2. Enter account number and kWh used
3. Click "Generate Bill"
4. Save as TXT or PDF (optional)

### Viewing Bills
1. Click "Load Previous Bills"
2. Double-click any file to open

---

## Billing Calculation

### Tiered Rates
| Usage (kWh) | Rate (₱/kWh) |
|-------------|--------------|
| 0 - 50      | ₱5.00        |
| 51 - 100    | ₱6.50        |
| 101 - 200   | ₱8.00        |
| 201+        | ₱10.00       |

### Calculation Formula
```
1. Base Charge = kWh × Rate
2. Environmental Fee = ₱50.00
3. Subtotal = Base Charge + Environmental Fee
4. Discount = Subtotal × Discount Rate (0%, 5%, or 10%)
5. Subtotal After Discount = Subtotal - Discount
6. VAT = Subtotal After Discount × 12%
7. Total = Subtotal After Discount + VAT
```

### Example
**Usage:** 150 kWh | **Discount:** Senior Citizen (5%)

- Base: 150 × ₱8.00 = ₱1,200.00
- Environmental Fee: ₱50.00
- Subtotal: ₱1,250.00
- Discount: ₱62.50
- After Discount: ₱1,187.50
- VAT: ₱142.50
- **Total: ₱1,330.00**

---

## Project Structure

```
electricity-billing-system/
├── main.py                 # Main application
├── database_handler.py     # Database operations
├── requirements.txt        # Dependencies
├── customer.db            # Database (auto-created)
└── bills/                 # Saved bills (auto-created)
```

---

## Troubleshooting

### Module Not Found
```bash
pip install -r requirements.txt
```

### Database Error
- Check write permissions
- Delete `customer.db` and restart

### PDF Won't Generate
- Verify ReportLab is installed
- Check `bills/` folder exists

### Files Won't Open
- Set default programs for .txt and .pdf files
- Or open files manually from `bills/` folder

---

## Tech Stack
- **Language:** Python 3.7+
- **GUI:** Tkinter
- **Database:** SQLite
- **PDF:** ReportLab

---

**Version:** 1.0 | **Last Updated:** December 2024
