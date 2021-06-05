from tkinter import Tk
from tkinter import *
from tkinter.ttk import Treeview
from types import FrameType
from Database import Database

# ----------- DB -------------
# Database configuration
db = Database
db.init()


# ----------- Tkinter -------------
# Tkinter initialization
root = Tk()
root.title('Gestión de productos')

# ----------- Layout -------------
# Main layout
frame = Frame(root, padx=10, pady=10)
frame.pack(anchor=CENTER)


# ----------- MENU -------------
# Menu settings
frameMenu = Frame(frame)
frameMenu.pack(anchor=CENTER)
Label(frameMenu, text='Gesetión de productos').pack(anchor=CENTER)

# Dropdown
categoriesList = db.getCategories()
CATEGORIES = []
for i in categoriesList:
    CATEGORIES.append(i[1])

variable = StringVar(root)
variable.set(CATEGORIES[0])

w = OptionMenu(frameMenu, variable, *CATEGORIES)
w.pack()

buttonsFrame = Frame(frameMenu)
buttonsFrame.pack()

def addCategoryWindow():
    print('Ventana de agregar categoría')

buttonAddCategory = Button(buttonsFrame,
text='Agregar categoría',
command=addCategoryWindow)
buttonAddCategory.pack(side=LEFT)

buttonObtion = Button(buttonsFrame, 
text='Buscar productos', 
command=lambda:db.getProducts(table, variable.get())
)
buttonObtion.pack(side=LEFT)


# ----------- TREEVIEW -------------
frameTable = Frame(root, padx=10, pady=10)
frameTable.pack()

table = Treeview(frameTable, show="headings", columns=(0,1, 2), height=10)
table.heading(0, text='ID')
table.heading(1, text='Product')
table.heading(2, text='Quantity')
table.pack()
# ----------- finishing -------------
# Main loop tkinter
root.mainloop()