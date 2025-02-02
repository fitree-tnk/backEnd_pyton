import databases
import select01

mycursor = databases.mydb.cursor()

def delete():
    print("หน้าเมนูการลบข้อมูล")
    select01.show_table()
    table = input("ใส่ : ")
    if table == "categories":
        select01.select_all(table)
        delete_categories(table)
    elif table == "orders":
        select01.select_all(table)
        delete_order(table)
    elif table == "products":
        select01.select_all(table)
        delete_product(table)
    elif table == "users":
        select01.select_all(table)
        delete_user(table)

def delete_categories(table):
    a = int(input("Enter category_id to delete : "))  # รับค่า category_id ที่ต้องการลบ
    sql = "DELETE FROM categories WHERE category_id = %s"  # คำสั่ง SQL ลบข้อมูล
    val = (a,)  # ค่าที่จะใช้ในการแทนที่ %s (ใช้ tuple)
    mycursor.execute(sql, val)  # รันคำสั่ง SQL
    databases.mydb.commit()  # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    select01.select_all(table)
    print("\nลบข้อมูลสำเร็จ\n")
    #print(f"Category with id {a} has been deleted.")

def delete_order(table):
    a = int(input("Enter order_id to delete : "))
    sql = "DELETE FROM orders WHERE order_id = %s"
    val = (a,)
    mycursor.execute(sql, val)
    databases.mydb.commit()
    select01.select_all(table)

def delete_product(table):
    a = int(input("Enter product_id to delete : "))
    sql = "DELETE FROM products WHERE product_id = %s"
    val = (a,)
    mycursor.execute(sql, val)
    databases.mydb.commit()
    select01.select_all(table)

def delete_user(table):
    a = int(input("Enter user_id to delete : "))
    sql = "DELETE FROM users WHERE user_id = %s"
    val = (a,)
    mycursor.execute(sql, val)
    databases.mydb.commit()
    select01.select_all(table)
delete()