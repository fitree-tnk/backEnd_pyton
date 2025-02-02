import databases
import datetime
import select01
mycursor = databases.mydb.cursor()

def insert_all():
    while True:
        print("หน้าเมนูการเพิ่มข้อมูล")
        select01.show_table()
        table = input("ใส่ : ")
        if table == "categories":
            select01.select_all(table)
            insert_categories(table)
        elif table == "orders":
            select01.select_all(table)
            insert_orders(table)
        elif table == "products":
            select01.select_all(table)
            insert_products(table)
        elif table == "users":
            select01.select_all(table)
            insert_users(table)
        elif table == "0":
            break

def insert_categories(table):
    a = int(input("category_id : "))
    b = str(input("category_name : "))
    val = (a, b)
    sql = "INSERT INTO categories VALUES (%s , %s)"
    mycursor.execute(sql,val) 
    #test.select_all("categories")
    #("INSERT INTO categories VALUES (%s , %s)")
    #a = mycursor.fetchall()
    databases.mydb.commit()
    select01.select_all(table)
    print("\nเพิ่มข้อมูลสำเร็จ\n")

def insert_orders(table):
    a = int(input("order_id : "))
    b = str(input("user_id : "))
    c = datetime.datetime.today()
    print (c.strftime("%d/%m/%y %H:%M:%S"))
    d = float(input("total_amount : "))
    e = str(input("status(รอดําเนินการ,กำลังจัดส่ง,จัดส่งสําเร็จ,ยกเลิกรายการ) : "))
    f = str(input("product_id : "))
    sql = "INSERT INTO orders VALUES (%s , %s , %s , %s , %s , %s)"
    val = (a, b ,c ,d ,e ,f)
    mycursor.execute(sql,val)
    #test.select_all("orders")
    databases.mydb.commit()
    select01.select_all(table)

def insert_products(table): 
    a = int(input("product_id : "))
    b = str(input("product_name : "))
    c = str(input("description : "))
    d = float(input("price : "))
    e = int(input("stock : "))
    f = int(input("category_id : "))
    val = (a, b ,c ,d ,e ,f)
    sql = "INSERT INTO products VALUES (%s , %s , %s , %s , %s , %s)"
    mycursor.execute(sql,val)
    #test.select_all("products")
    databases.mydb.commit()
    select01.select_all(table)

def insert_users(table):
    a = int(input("user_id : "))
    b = str(input("username : "))
    c = str(input("password : "))
    d = str(input("email : "))
    e = str(input("user_role = admin,customer : "))
    val = (a, b ,c ,d ,e)
    sql = "INSERT INTO users VALUES (%s , %s , %s , %s , %s)"
    mycursor.execute(sql,val)
    #test.select_all("users")
    databases.mydb.commit()
    select01.select_all(table)

