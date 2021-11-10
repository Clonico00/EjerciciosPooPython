from tkinter import *


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


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
    nombreData2 = nombre2.get()
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


def list_data():
    nombreData = nombre.get()
    precioData = str(precio.get())
    generoData = genero.get()

    newFile = open("manga.txt", "w")

    newFile.write(nombreData)
    newFile.write(precioData)
    newFile.write(generoData)


window = Tk()
window.title("Ejercicio Interfaz Grafica")
app = FullScreenApp(window)

# window.attributes("-fullscreen", False)
# --------------AÑADIR-------------------------------------------
nombreLabel = Label(text="Nombre Manga")
nombreLabel.place(x=25, y=50)
precioLabel = Label(text="Precio Manga")
precioLabel.place(x=25, y=100)
generoLabel = Label(text="Genero Manga")
generoLabel.place(x=25, y=150)

nombre = StringVar()
precio = StringVar()
genero = StringVar()

nombreEntry = Entry(textvariable=nombre, width=50)
precioEntry = Entry(textvariable=precio, width=50)
generoEntry = Entry(textvariable=genero, width=50)

nombreEntry.place(x=200, y=50)
precioEntry.place(x=200, y=100)
generoEntry.place(x=200, y=150)

crearBtn = Button(window, text="CREAR", command=send_data, width="40", height="1",
                  bg="#757474", borderwidth=5, activebackground="#757474")
crearBtn.place(x=150, y=240)

# --------------BORRAR-------------------------------------------
nombreLabel2 = Label(text="Nombre Manga")
nombreLabel2.place(x=800, y=50)

nombre2 = StringVar()

nombreEntry2 = Entry(textvariable=nombre2, width=50)

nombreEntry2.place(x=975, y=50)

crearBtn2 = Button(window, text="BORRAR", command=delete_data, width="40", height="1",
                   bg="#757474", borderwidth=5, activebackground="#757474")
crearBtn2.place(x=925, y=240)

# --------------MODIFICAR-------------------------------------------
nombreLabel3 = Label(text="Nombre Manga")
nombreLabel3.place(x=25, y=500)
precioLabel3 = Label(text="Precio Manga")
precioLabel3.place(x=25, y=550)
generoLabeL3 = Label(text="Genero Manga")
generoLabeL3.place(x=25, y=600)

nombre3 = StringVar()
precio3 = StringVar()
genero3 = StringVar()

nombreEntry3 = Entry(textvariable=nombre3, width=50)
precioEntry3 = Entry(textvariable=precio3, width=50)
generoEntry3 = Entry(textvariable=genero3, width=50)

nombreEntry3.place(x=200, y=500)
precioEntry3.place(x=200, y=550)
generoEntry3.place(x=200, y=600)

crearBtn3 = Button(window, text="MODIFICAR", command=modify_data, width="40", height="1",
                   bg="#757474", borderwidth=5, activebackground="#757474")
crearBtn3.place(x=150, y=680)
# --------------LISTAR-------------------------------------------

window.mainloop()