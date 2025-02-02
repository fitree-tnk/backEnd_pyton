import databases

mycursor = databases.mydb.cursor()


def update_category():
    category_id = int(input("Enter category_id to update: "))  # รับค่า category_id ที่ต้องการแก้ไข
    new_name = input("Enter new category name: ")  # รับค่า category_name ใหม่
    
    sql = "UPDATE categories SET category_name = %s WHERE category_id = %s"  # คำสั่ง SQL แก้ไขข้อมูล
    val = (new_name, category_id)  # ค่าที่จะใช้ในการแทนที่ %s
    
    mycursor.execute(sql, val)  # รันคำสั่ง SQL
    
    databases.mydb.commit()  # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    
    mycursor.execute("SELECT * FROM categories")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)
    #print(f"Category with id {category_id} has been updated to '{new_name}'")
    
    # แสดงข้อมูลทั้งหมดเพื่อยืนยันการแก้ไข
update_category()  
