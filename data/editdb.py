import databases
mycursor = databases.mydb.cursor()

def edit(table):
    if table == 'categories':
        a = input('เลือกคอลัม : ')
        b = input('ข้อมูลที่ต้องการเปลี่ยน : ')
        c = int(input('id มี่ต้องการจะเปลี่ยน : '))
        sql = f'UPDATE categories SET {a} = %s WHERE category_id = %s'
        val = (b,c)
        mycursor.execute(sql,val)
        databases.mydb.commit()
    elif table == 'orders':
        a = input('เลือกคอลัม : ')
        b = input('ข้อมูลที่ต้องการเปลี่ยน : ')
        c = int(input('id มี่ต้องการจะเปลี่ยน : '))
        sql = f'UPDATE orders SET {a} = %s WHERE order_id = %s'
        val = (b,c)
        mycursor.execute(sql,val)
        databases.mydb.commit()
