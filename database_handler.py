import sqlite3
from random import randint

class data_handler:
    def __init__(self, data_file):
        self.con = sqlite3.connect(data_file)
        self.cur = self.con.cursor()
        
        # Create customer table if it doesn't exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS customer(
                AccountNumber INTEGER PRIMARY KEY NOT NULL, 
                CustomerName TEXT NOT NULL, 
                Address CHAR(50), 
                Type TEXT NOT NULL, 
                Discount TEXT NOT NULL, 
                Usage INT DEFAULT 0, 
                AllTimeUsage INT DEFAULT 0
            )
        """)
        self.con.commit()
    
    def create_account(self, name, address, type, discount):
        """Create a new customer account with a unique account number"""
        # Generate unique account number
        while True:
            account_number = randint(100000, 999999)
            # Check if account number already exists
            self.cur.execute("SELECT AccountNumber FROM customer WHERE AccountNumber = ?", (account_number,))
            if self.cur.fetchone() is None:
                break
        
        try:
            self.cur.execute("""
                INSERT INTO customer (AccountNumber, CustomerName, Address, Type, Discount, Usage, AllTimeUsage)
                VALUES (?, ?, ?, ?, ?, 0, 0)
            """, (account_number, name, address, type, discount))
            self.con.commit()
            print(f"✓ Account created successfully! Account Number: {account_number}")
            return account_number
        except sqlite3.Error as e:
            print(f"✗ Error creating account: {e}")
            return None
    
    def get_customer(self, account_number):
        """Get customer information by account number"""
        self.cur.execute("SELECT * FROM customer WHERE AccountNumber = ?", (account_number,))
        customer = self.cur.fetchone()
        
        if customer:
            return {
                'account_number': customer[0],
                'name': customer[1],
                'address': customer[2],
                'type': customer[3],
                'discount': customer[4],
                'usage': customer[5],
                'all_time_usage': customer[6]
            }
        else:
            return None
    
    def update_usage(self, account_number, kwh_used):
        """Update customer usage"""
        customer = self.get_customer(account_number)
        if not customer:
            return False
        
        new_usage = kwh_used
        new_all_time_usage = customer['all_time_usage'] + kwh_used
        
        try:
            self.cur.execute("""
                UPDATE customer 
                SET Usage = ?, AllTimeUsage = ?
                WHERE AccountNumber = ?
            """, (new_usage, new_all_time_usage, account_number))
            self.con.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating usage: {e}")
            return False
    
    def get_all_customers(self):
        """Get all customers"""
        self.cur.execute("SELECT * FROM customer")
        customers = self.cur.fetchall()
        
        result = []
        for customer in customers:
            result.append({
                'account_number': customer[0],
                'name': customer[1],
                'address': customer[2],
                'type': customer[3],
                'discount': customer[4],
                'usage': customer[5],
                'all_time_usage': customer[6]
            })
        return result
    
    def update_customer(self, account_number, **kwargs):
        """Update customer information"""
        valid_fields = {'CustomerName': 'name', 'Address': 'address', 
                       'Type': 'type', 'Discount': 'discount'}
        updates = []
        values = []
        
        for key, value in kwargs.items():
            db_field = None
            for db_key, py_key in valid_fields.items():
                if py_key == key:
                    db_field = db_key
                    break
            
            if db_field:
                updates.append(f"{db_field} = ?")
                values.append(value)
        
        if not updates:
            return False
        
        values.append(account_number)
        query = f"UPDATE customer SET {', '.join(updates)} WHERE AccountNumber = ?"
        
        try:
            self.cur.execute(query, values)
            self.con.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating account: {e}")
            return False
    
    def delete_account(self, account_number):
        """Delete a customer account"""
        try:
            self.cur.execute("DELETE FROM customer WHERE AccountNumber = ?", (account_number,))
            self.con.commit()
            return self.cur.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting account: {e}")
            return False
    
    def search_customers(self, name):
        """Search customers by name"""
        self.cur.execute("SELECT * FROM customer WHERE CustomerName LIKE ?", (f"%{name}%",))
        customers = self.cur.fetchall()
        
        result = []
        for customer in customers:
            result.append({
                'account_number': customer[0],
                'name': customer[1],
                'address': customer[2],
                'type': customer[3],
                'discount': customer[4],
                'usage': customer[5],
                'all_time_usage': customer[6]
            })
        return result
    
    def close(self):
        """Close database connection"""
        self.con.close()
