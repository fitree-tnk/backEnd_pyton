import databases
mycursor = databases.mydb.cursor()

def selectdb(table):
    mycursor.execute(f"SELECT * FROM {table}")
    show = mycursor.fetchall()
    if len(show) <= 0 :
        return False,None
    else:
        return True,show

def deletedb(table,id_name,id):
    sql = f'DELETE FROM {table} WHERE {id_name} = %s'
    val = (id,)
    mycursor.execute(sql,val)
    databases.mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,None
    
def updetedb(table,colum,a,id_name,b):
    sql = f'UPDATE {table} SET {colum} = %s WHERE {id_name} = %s'
    val = (a,b)
    mycursor.execute(sql,val)
    databases.mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,None
    
def insert_categories(table,category_name):
    sql = f"INSERT INTO {table} VALUES ( %s)"
    val = (category_name,)
    mycursor.execute(sql,val)
    databases.mydb.commit()
    if mycursor.rowcount <= 0:
        return False,None
    else:
        return True,val
    
