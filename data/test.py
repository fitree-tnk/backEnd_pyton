import databases

mycursor = databases.mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print("--------------------------------------------------------------------------------")
    print("ตารางข้อมูลทั้งหมด")
    for i in table:
        print(i)
    print("--------------------------------------------------------------------------------")

def select_all():
    while True:
        show_table()
        table = input("ตารางที่ต้องการค้นหา : ")
        if table == '0':
            break
        print("--------------------------------------------------------------------------------")
        mycursor.execute(f"SELECT * FROM {table}")
        myresulf = mycursor.fetchall()
        for i in myresulf :
            print(i)

def select_table_user():
    while True:
        #show_table()
        #table = input("ตารางที่ต้องการค้นหา : ")
        name = input("ป้อน username(กด 0 เพื่อกลับไปหน้าหลัก) : ")
        if name == '0':
            break
        #mycursor.execute(f"SELECT * FROM {table} where username like '%{name}%'")
        mycursor.execute(f"SELECT * FROM users where username like '%{name}%'")
        myresulf = mycursor.fetchall()
        for i in myresulf :
            print(i)

def select_table_product():
    while True:
        #show_table()
        #table = input("ตารางที่ต้องการค้นหา : ")
        name = input("ป้อน product_name(กด 0 เพื่อกลับไปหน้าหลัก) : ")
        if name == '0':
            break
        mycursor.execute(f"SELECT * FROM products where product_name like '%{name}%'")
        myresulf = mycursor.fetchall()
        for i in myresulf :
            print(i)

def select_table_categories():
    while True:
        #show_table()
        #table = input("ตารางที่ต้องการค้นหา : ")
        name = input("ป้อน category_name(กด 0 เพื่อกลับไปหน้าหลัก) : ")
        if name == '0':
            break
        mycursor.execute(f"SELECT * FROM categories where category_name like '%{name}%'")
        myresulf = mycursor.fetchall()
        for i in myresulf :
            print(i)

def select_table_orders():
    while True:
        #show_table()
        #table = input("ตารางที่ต้องการค้นหา : ")
        name = input("ป้อน order_id(กด 0 เพื่อกลับไปหน้าหลัก) : ")
        if name == '0':
            break
        mycursor.execute(f"SELECT * FROM orders where order_id like '%{name}%'")
        myresulf = mycursor.fetchall()
        for i in myresulf :
            print(i)

while True:
    print("--------------------------------------------------------------------------------")
    print("ดูข้อมูลทั้งหมดพิมพ์ all")
    print("ดูข้อมูลของตารางพิมพ์ user")
    print("ดูข้อมูลของตารางพิมพ์ product")
    print("ดูข้อมูลของตารางพิมพ์ categories")
    print("ดูข้อมูลของตารางพิมพ์ orders")
    print("--------------------------------------------------------------------------------")
    a = str(input('กรอกข้อมูลที่ต้องการหา : '))
    if a == 'all':
        select_all()
    elif a == 'user':
        select_table_user()
    elif a == 'product':
        select_table_product()
    elif a == 'categories':
        select_table_categories()
    elif a == 'orders':
        select_table_orders()
    elif a == '0':
        break
    else:
        print('ไม่ถูก')