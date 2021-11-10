from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Ejercicio Interfaz Grafica")
window.geometry("750x650")
#messagebox

# -------------------------FUNCIONES--------------------------------------
def send_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()
    manga = nombreData + " " + precioData + " " + generoData + "\n"

    newFile = open("manga.txt", "a")

    newFile.write(manga)

    newFile.close()


def delete_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()
    manga = nombreData + " " + precioData + " " + generoData + "\n"

    newFile = open("manga.txt", "r")
    lineas = newFile.readlines()
    newFile.close()

    newFile = open("manga.txt", "w")
    for linea in lineas:
        if linea != manga:
            newFile.write(linea)
    newFile.close()


def modify_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()

    newFile = open("manga.txt", "w")

    newFile.write(nombreData)
    newFile.write(precioData)
    newFile.write(generoData)


# -------------------------TREEVIEW--------------------------------------
arbol = ttk.Treeview(window, columns=("precio", "genero"))
arbol.heading("#0", text="Titulo")
arbol.heading("precio", text="Precio")
arbol.heading("genero", text="Género")
menu1 = arbol.insert("", END, text="One Piece", values=("1000", "shonen"))
menu2 = arbol.insert("", END, text="Dragon Ball", values=("88", "shonen"))
arbol.place(x=65, y=40)

# ---------------------------LABELS---------------------------------------
nombreLabel = Label(text="Nombre Manga")
nombreLabel.place(x=65, y=300)
precioLabel = Label(text="Precio Manga")
precioLabel.place(x=65, y=350)
generoLabel = Label(text="Genero Manga")
generoLabel.place(x=65, y=400)

# ---------------------------ENTRYS---------------------------------------
nombre = StringVar()
precio = StringVar()
genero = StringVar()

nombreEntry = Entry(textvariable=nombre, width=77)
precioEntry = Entry(textvariable=precio, width=77)
generoEntry = Entry(textvariable=genero, width=77)

nombreEntry.place(x=200, y=300)
precioEntry.place(x=200, y=350)
generoEntry.place(x=200, y=400)

# ---------------------------BUTTONS---------------------------------------
crearBtn = Button(window, text="CREAR", command=send_data, width="84", height="1",
                  bg="#757474", borderwidth=5, activebackground="#757474")
crearBtn.place(x=65, y=450)

borrarBtn = Button(window, text="BORRAR", command=delete_data, width="84", height="1",
                  bg="#757474", borderwidth=5, activebackground="#757474")
borrarBtn.place(x=65, y=500)

modificarBtn = Button(window, text="MODIFICAR", command=modify_data(), width="84", height="1",
                  bg="#757474", borderwidth=5, activebackground="#757474")
modificarBtn.place(x=65, y=550)
window.mainloop()
