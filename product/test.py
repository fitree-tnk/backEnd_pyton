import tkinter
import databases

mycursor = databases.mydb.cursor()

# ฟังก์ชันแสดงรายการตาราง
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

# ฟังก์ชันเปิดหน้าต่างสำหรับแสดงข้อมูลจากตาราง
def open_table_window():
    selected_table = table_listbox.get(tkinter.ACTIVE)  # เลือกตารางจาก Listbox
    if selected_table:
        table_window = tkinter.Toplevel(program)
        table_window.title(f"ข้อมูลจากตาราง {selected_table}")

        # กำหนดขนาดหน้าต่างใหม่
        table_window.geometry("400x400")

        # กล่องป้อนข้อมูล
        table_label = tkinter.Label(table_window, text=f"ข้อมูลจากตาราง: {selected_table}")
        table_label.pack()

        # ฟังก์ชันแสดงข้อมูลจากตาราง
        def show_table_data():
            mycursor.execute(f"SELECT * FROM {selected_table}")
            rows = mycursor.fetchall()
            result_text = "\n".join(str(row) for row in rows)
            data_label.configure(text=result_text if result_text else "ไม่พบข้อมูล")
        
        data_label = tkinter.Label(table_window, text="ข้อมูลจะโชว์ที่นี่")
        data_label.pack()

        show_button = tkinter.Button(table_window, text="แสดงข้อมูล", command=show_table_data)
        show_button.pack()

# สร้างหน้าต่างหลัก
program = tkinter.Tk()
program.title('โปรแกรมจัดการข้อมูล')

# กำหนดขนาดหน้าต่างหลัก
program.geometry("400x400")

# ป้ายข้อความหลัก
program_label = tkinter.Label(program, text="แสดงรายการตาราง")
program_label.pack()

# 🔹 เพิ่มปุ่มแสดงตาราง
show_tables_button = tkinter.Button(program, text="แสดงตาราง", command=show_tables)
show_tables_button.pack()

# 🔹 เพิ่ม Listbox สำหรับแสดงรายการตาราง
table_listbox = tkinter.Listbox(program, height=10)
table_listbox.pack()

# 🔹 ปุ่มสำหรับเปิดหน้าต่างที่เลือกข้อมูลจากตาราง
open_table_button = tkinter.Button(program, text="ดูข้อมูลตาราง", command=open_table_window)
open_table_button.pack()

# เรียกใช้งาน GUI
program.mainloop()