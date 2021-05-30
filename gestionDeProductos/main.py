from tkinter import Tk
from tkinter import *
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
CATEGORIES = (
    'computers',
    'phones',
    'HDD'
)
variable = StringVar(root)
variable.set(CATEGORIES[0])

w = OptionMenu(frameMenu, variable, *CATEGORIES)
w.pack()


# ----------- finishing -------------
# Main loop tkinter
root.mainloop()