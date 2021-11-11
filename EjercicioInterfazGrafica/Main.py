from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Ejercicio Interfaz Grafica")
window.geometry("750x650")

window.configure(bg='#525174')


# messagebox

# -------------------------FUNCIONES--------------------------------------
def send_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()
    manga = nombreData + " " + precioData + " " + generoData + "\n"

    arbol.insert("", END, text=nombreData, values=(precioData, generoData))

    newFile = open("manga.txt", "a")
    newFile.write(manga)
    newFile.close()


def delete_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()
    manga = nombreData + " " + precioData + " " + generoData + "\n"
    if nombreData == "":
        messagebox.showerror(message="Rellene el nombre del manga que desea borrar", title="ERROR")
        pass
    else:
        newFile = open("manga.txt", "r")
        lineas = newFile.readlines()
        newFile.close()

        newFile = open("manga.txt", "w")
        for linea in lineas:
            if linea != manga:
                newFile.write(linea)
        newFile.close()

        print(arbol.selection()[0])
        selected_item = arbol.selection()[0]
        arbol.delete(selected_item)


def modify_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()
    manga = nombreData + " " + precioData + " " + generoData + "\n"

    if nombreData == "":
        messagebox.showerror(message="Rellene el nombre del manga que desea modificar", title="ERROR")
        pass
    else:
        selected_item = arbol.selection()[0]
        arbol.item(selected_item, text=nombreData, values=(precioData, generoData))
        newFile = open("manga.txt", "r")
        lineas = newFile.readlines()
        newFile.close()

        newFile = open("manga.txt", "w+")
        for linea in lineas:
            if nombreData in linea:
                newFile.write(manga)
            else:
                newFile.write(linea)
        newFile.close()


# -------------------------TREEVIEW--------------------------------------
estilo = ttk.Style()

estilo.configure("mystyle.Treeview", highlightthickness=0,bd=0, font=('Lucida Console', 9))

arbol = ttk.Treeview(window, columns=("precio", "genero"),style="mystyle.Treeview")
arbol.heading("#0", text="Titulo")
arbol.heading("precio", text="Precio")
arbol.heading("genero", text="Género")
arbol.place(x=65, y=40)


# ---------------------------LABELS---------------------------------------
nombreLabel = Label(text="Nombre Manga", font=('Helvetica', 10))
nombreLabel.place(x=65, y=300)
nombreLabel.configure(bg="#FCD3DE",foreground="#000000")
precioLabel = Label(text="Precio Manga", font=('Helvetica', 10))
precioLabel.place(x=65, y=350)
precioLabel.configure(bg="#FCD3DE",foreground="#000000")
generoLabel = Label(text="Genero Manga", font=('Helvetica', 10))
generoLabel.place(x=65, y=400)
generoLabel.configure(bg="#FCD3DE",foreground="#000000")


# ---------------------------ENTRYS---------------------------------------
nombre = StringVar()
precio = StringVar()
genero = StringVar()

nombreEntry = Entry(textvariable=nombre, width=77)
precioEntry = Entry(textvariable=precio, width=77)
generoEntry = Entry(textvariable=genero, width=77)

nombreEntry.place(x=200, y=300)
nombreEntry.configure(bg="#FCD3DE",foreground="#000000")

precioEntry.place(x=200, y=350)
precioEntry.configure(bg="#FCD3DE",foreground="#000000")

generoEntry.place(x=200, y=400)
generoEntry.configure(bg="#FCD3DE",foreground="#000000")


# ---------------------------BUTTONS---------------------------------------
crearBtn = Button(window, text="CREAR", command=send_data, width="74", height="1",
                  bg="#72A1E5", borderwidth=3,foreground="#000000", font=('Helvetica', 10))
crearBtn.place(x=65, y=450)

borrarBtn = Button(window, text="BORRAR", command=delete_data, width="74", height="1",
                   bg="#72A1E5", borderwidth=3,foreground="#000000", font=('Helvetica', 10))
borrarBtn.place(x=65, y=500)

modificarBtn = Button(window, text="MODIFICAR", command=modify_data, width="74", height="1",
                      bg="#72A1E5", borderwidth=3,foreground="#000000", font=('Helvetica', 10))
modificarBtn.place(x=65, y=550)
window.mainloop()
