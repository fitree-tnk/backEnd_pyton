import databases
import select01
import insert
import delete

while True:
    print ("\nโปรแกรมการดูข้อมูล การเพิ่มข้อมูล การลบข้อมูล")
    print ("กด 1 = ดูข้อมูลทั้งหมด")
    print ("กด 2 = เพิ่มข้อมูล")
    print ("กด 3 = ลบข้อมูล")

    a = int(input('เมนูที่ต้องการเลือก : '))
    if a == 0:
        break
    elif a == 1:
        select01.select_table()
    elif a == 2:
        insert.insert_all()
    elif a == 3:
        delete.delete()
    else:
        print("กรุณาใส่ตัวเลขให้ถูกต้อง!!!")


