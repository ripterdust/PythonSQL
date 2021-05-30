from logging import error
import tkinter
from database import Database
from tkinter import *
from tkinter import ttk

# Database
db = Database
db.init()


# Tkinter config
root = Tk()
root.title('Gestión de usuarios')
text = Label(root, text='Gestión de usuarios', pady=10)
text.pack()

# Agregar nuevo usuario

addFrame = Frame(root, pady=10)
addFrame.pack(anchor=CENTER)
Label(addFrame, text='Agregar nuevo usuarios').pack()

# User Data
usrF = Frame(addFrame, pady=3)
usrF.pack()
usr = Entry(usrF)
Label(usrF, text='Usuario: ').pack(side=LEFT)
usr.pack(side=LEFT)

# Phone data
phoneF = Frame(addFrame, pady=3)
phoneF.pack()
Label(phoneF, text='Teléfono: ').pack(side=LEFT)
phone = Entry(phoneF)
phone.pack(side=LEFT)

# Add user btn
def add(name, phone):
    db.addUser(name, phone)
    db.getData(tv)
addBtn = Button(addFrame, text="Add user", command=lambda:add(usr.get(), phone.get()))
addBtn.pack()

# Treeview
# Frame to contain the treeview
frame = Frame(root, padx=20)
frame.pack()

tv = ttk.Treeview(frame, show="headings", columns=(0,1,2), height=10)
tv.heading(0, text='ID')
tv.heading(1, text='NAME')
tv.heading(2, text='PHONE')
tv.pack()

# Obteniendo datos para insertar en la tabla
db.getData(tv)



# Action buttons
frameButton = Frame(frame, pady=10)
frameButton.pack(anchor=CENTER)

# Error function

def errorWindow(err='Por favor selecciona un registro'):
    root.withdraw()
    deleteBtn['state'] = 'disabled'
    editBtn['state'] = 'disabled'
    addBtn['state'] = 'disabled'
    newWindow = Toplevel(root)
    newWindow.title('Ha ocurrido un error')
    newWindow.geometry('300x50')
    f = Frame(newWindow, padx=15, pady=15)
    f.pack()
    Label(f, text=err).pack()
    def onClose():
        deleteBtn['state'] = 'active'
        editBtn['state'] = 'active'
        addBtn['state'] = 'active'
        newWindow.destroy()
        print('cerrada')
        root.deiconify()
    newWindow.protocol("WM_DELETE_WINDOW", onClose)

# select field funct

def select():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    return temp

# Delete button

def deleteRecord():
    try:
        item = select()
        print(item[0])
        db.deleteUser(item[0])
        db.getData(tv)
    except:
        errorWindow()
    
deleteBtn = Button(frameButton, text='Eliminar registro seleccionado', command=deleteRecord)
deleteBtn.pack(side=LEFT)

# Edit Button
def update():
    try:
        deleteBtn['state'] = 'disabled'
        editBtn['state'] = 'disabled'
        addBtn['state'] = 'disabled'
        updateW = Toplevel(root)
        updateW.title('Editar usuario')

        # Selecting element
        item = select()


        # Full frame
        tf = Frame(updateW, pady=10, padx=10)
        tf.pack(anchor=CENTER)
        Label(tf, text='Si no se quiere editar, dejar en blanco').pack(anchor=CENTER)
        # name settings
        nF = Frame(tf, padx=5, pady=5)
        nF.pack()
        Label(nF, text='Nombre: ').pack(side=LEFT)
        name = Entry(nF)
        name.pack(side=LEFT)
        

        pF = Frame(tf, padx=5, pady=5)
        pF.pack()
        Label(pF, text='Teléfono: ').pack(side=LEFT)
        phone = Entry(pF, text=item[2])
        phone.pack(side=LEFT)

        # action buttons

        bF = Frame(tf)
        bF.pack(anchor=CENTER)
        # onclose function
        def onClose():
            deleteBtn['state'] = 'active'
            editBtn['state'] = 'active'
            addBtn['state'] = 'active'
            updateW.destroy()

        # Save button
        def save(id ,name, phone):
            if name == '':
                name = item[1]
            if phone == '':
                phone = item[2]
        
            db.updateUser(id, name, phone)

            db.getData(tv)

            onClose()
        
        btnS = Button(bF, text='Gardar cambios', command=lambda:save(item[0], name.get(), phone.get()))
        btnS.pack()

        # Cancel button
        def cancel():
            onClose()
        
        btnC = Button(bF, text='Cancelar', command=cancel)
        btnC.pack()
        updateW.protocol("WM_DELETE_WINDOW", onClose)
    except:
        errorWindow()



editBtn = Button(frameButton, text='Editar registro seleccionado', command=update)
editBtn.pack(side=LEFT)



# main loop
root.mainloop()


