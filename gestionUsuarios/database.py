from logging import exception
import mysql.connector as mysql

db = mysql.connect(
    user='root',
    password='marlyn2010',
    host='localhost'
)

cursor = db.cursor()

class Database:
    
    def init():
        cursor.execute('CREATE DATABASE IF NOT EXISTS usrsDB;')
        cursor.execute('USE usrsDB;')
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        ID              INT(20) NOT NULL AUTO_INCREMENT,
        name            VARCHAR(25) NOT NULL,
        phone           VARCHAR(10) NOT NULL,

        CONSTRAINT      pk_id PRIMARY KEY(ID),
        CONSTRAINT      uk_phone UNIQUE(phone)
        ) ENGINE=InnoDb;""")
        print('base de datos conectada')


    def getData(tv):
        tv.delete(*tv.get_children())
        cursor.execute('SELECT * FROM usuarios;')
        data = cursor.fetchall()
        for i in data:
            tv.insert('', 'end', values=i)

    def addUser(user, phone):
        if user != '' or phone != '':
            cursor.execute(f"""INSERT INTO usuarios(name, phone) VALUES('{user}', '{phone}')""")
            db.commit()

            
    def deleteUser(id=None):
        
        cursor.execute(f"DELETE FROM usuarios WHERE ID = {id}")
       
        
    def updateUser(id=None, newName='bryan', newPhone=112):
        try:
            print(f'id: {id}')
            cursor.execute(f"UPDATE usuarios SET name = '{newName}', phone = '{newPhone}' WHERE ID = {id}")
            db.commit()
        except:
            print('no se puede')