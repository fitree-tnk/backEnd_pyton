import tkinter
import apidb
import databases

mycursor = databases.mydb.cursor()

'''def show_table():
    mycursor.execute("SHOW TABLES") #คำสั่งดึงข้อมูล
    table = mycursor.fetchall() #แสดงผล 
    for i in table:
        print(i)'''

'''def show_table():
    mycursor.execute("SHOW TABLES")  # คำสั่งดึงข้อมูล
    table = mycursor.fetchall()  # ดึงข้อมูลทั้งหมด
    table_listbox.delete(0, tkinter.END)
    return [i[0] for i in table]  # คืนค่าเป็นรายการชื่อของตาราง'''

def show_tables():
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    tables = mycursor.fetchall()
        # เคลียร์ข้อมูลใน Listbox ก่อนแสดงผลใหม่
    table_listbox.delete(0, tkinter.END)
    
    if not tables:
        table_listbox.insert(tkinter.END, "ไม่พบตารางใด ๆ")
    else:
        for table in tables:
            table_listbox.insert(tkinter.END, table[0])  # เพิ่มชื่อตารางลงใน Listbox
'''    if not tables:
        return False, None
    else:
        return True, [table[0] for table in tables]  # คืนค่ารายการตารางเป็น list'''
    

def selectdb():
    table =table_input.get()
    mycursor.execute(f"SELECT * FROM {table}")
    show = mycursor.fetchall()
    if len(show) <= 0 :
        return False,None
    else:
        return True,output_lable.configure(text=show)

def deletedb():
    table = table_input.get()
    id = del_input.get()
    sql = f'DELETE FROM {table} WHERE id = %s'
    val = (id,)
    mycursor.execute(sql,val)
    databases.mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,None
   
program = tkinter.Tk()
program.title('โปรแกรมจัดการข้อมูล')
program.minsize(width=400,height=400)



program_lable = tkinter.Label(master=program , text="เลือกหัวข้อที่ต้องการ")
program_lable.pack()

table_input = tkinter.Entry(master=program)
table_input.pack()

search_button = tkinter.Button(master=program,text="ค้นหา",command=selectdb)
search_button.pack()

del_lable = tkinter.Label(master=program, text="ใส่ ID ที่ต้องการที่จะลบ")
del_lable.pack()

del_input = tkinter.Entry(master=program)
del_input.pack()

delete_button = tkinter.Button(master=program,text="ลบข้อมูล",command=deletedb)
delete_button.pack()

output_lable = tkinter.Label(master=program,text="ผลการค้นหา")
output_lable.pack()

# 🔹 เพิ่มปุ่มแสดงตาราง
show_tables_button = tkinter.Button(program, text="แสดงตาราง", command=show_tables)
show_tables_button.pack()

# 🔹 เพิ่ม Listbox สำหรับแสดงรายการตาราง
table_listbox = tkinter.Listbox(program, height=5)
table_listbox.pack()

program.mainloop()