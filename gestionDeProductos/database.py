import mysql.connector as mysql

db = mysql.connect(
    user='root',
    password='marlyn2010',
    host='localhost'
)

cursor = db.cursor()

class Database:
    
    def init():
        # Creating db if not exists
        cursor.execute('CREATE DATABASE IF NOT EXISTS products;')
        # Using database
        cursor.execute('USE products;')
        # Creating categories table
        cursor.execute("""CREATE TABLE IF NOT EXISTS categories(
        id              int(25) auto_increment,
        category        varchar(255),

        CONSTRAINT      pk_categories PRIMARY KEY(id),
        CONSTRAINT      uk_categories UNIQUE(category)
        ) ENGINE=InnoDb;
        """)


    def getProducts(tv, category):
        tv.delete(*tv.get_children())
        cursor.execute(f'SELECT * FROM categories WHERE category = "{category}"')
        data = cursor.fetchall()
        if len(data) <= 0:
            print('No hay datos')
        else:
            for i in data:
                print(f'Categoría: {i}' )
                tv.insert('', 'end', values=i)

        print('terminó')
    
    def getCategories():
        cursor.execute('SELECT * FROM categories;')
        data = cursor.fetchall()

        return data

    def addCategory(category):
        print(category)
    
    def addProdcut(category, product, value, quantity):
        print(category, product, value, quantity)