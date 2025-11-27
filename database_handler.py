def create_database():
    con = sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE customer(AccountNumber, CustomerName, Address, Type, Discount, Usage)")

def create_account():
    pass
