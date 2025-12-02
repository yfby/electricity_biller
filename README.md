## **Minimum Viable Product (MVP)**
**✅ Customer Database
✅ Calculate Function
✅ UI
✅ Input validation
✅ Comments and Documentation**

## **Bonus Features**
**✅ GUI using Tkinter
✅ Save bill to a text file
✅ Load previous bills
✅ Multiple customers
✅ Generate receipt as a PDF
✅ Discount options (senior citizen, PWD, etc.)**

install missing module

```
function test() {
  console.log("pip install -r requirements.txt");
}
```

***The Electricity Billing System is a user-friendly desktop application designed to streamline electricity billing operations. It provides complete customer account management, automated bill calculation with tiered pricing, and comprehensive record-keeping capabilities.***

┌─────────────────────────────────────┐
│    ⚡ ELECTRICITY BILLING SYSTEM    │
├─────────────────────────────────────┤
│  ➕ Create New Account              │
│  👤 Get Customer Information        │
│  💰 Bill Customer                   │
│  📋 List All Customers              │
│  📄 Load Previous Bills             │
│  ❌ Exit                            │
└─────────────────────────────────────┘

┌─────────────────────┐
│   User Input        │
│   - Account Number  │
│   - kWh Used        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Fetch Customer     │
│  Data from DB       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Calculate Rates    │
│  (Tiered Pricing)   │
│  0-50:    ₱5.00     │
│  51-100:  ₱6.50     │
│  101-200: ₱8.00     │
│  201+:    ₱10.00    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Apply Charges      │
│  Base + Env Fee     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Apply Discount     │
│  (if applicable)    │
│  Senior: 5%         │
│  PWD: 5%            │
│  Low-income: 10%    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Calculate VAT      │
│  (12% of subtotal)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Generate Bill      │
│  Display & Save     │
└─────────────────────┘
