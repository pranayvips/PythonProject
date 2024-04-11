from mysql.connector import connect

db = connect(host="localhost",user="root",password="1234",database="seat")
cursor = db.cursor()


# cursor.execute("CREATE DATABASE seat")
# cursor.execute("create table main(name varchar(30) PRIMARY KEY,age int,gender varchar(10),seat varchar(5),fare int)")
# db.commit()

def create_new_data(name,age,gender,seat,fare):
    cd = "insert into table MAIN values(%s,%d,%s,%s,%s)"%(name,age,gender,seat,fare)
    cursor.execute(cd)
def remove_data(name):
    cd = "select * from MAIN where name='%s'"%name
    cursor.execute(cd)
    h = cursor.fetchone()
    if h == None:
        return 0
    else:
        return h

