from tkinter import Tk
from tkinter import *
from database.database import Database

# ----------- DB -------------
# Database configuration



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





# ----------- Tkinter -------------
# Main loop tkinter
root.mainloop()