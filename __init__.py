from tkinter import *
from tkinter import messagebox
from funciones_numero_a_letras import *

#for i in range(101):
#    print(str(i) + " --> " + str(numero_a_letras(i)))

def leerNumero():
    dato_capturado = txt_entrada.get()
    try:
        dato_entero = int(dato_capturado)
        resultado_texto = numero_a_letras(dato_entero)
        lbl_resultado.configure(text=resultado_texto)
    except ValueError:
        messagebox.showinfo('Mensaje', 'Por favor ingrese un dato numerico entero.')
        lbl_resultado.configure(text="")
    except:
        messagebox.showinfo('Mensaje', 'Ha ocurrido un error.')
        lbl_resultado.configure(text="")
    #finally:
    #    txt_entrada = ""

ventana = Tk()
#ventana.configure(background="#0FB0AB")
ventana.title("Numero a letras")

lbl_mensaje = Label(ventana, text="Ingrese un numero: ", font=("Arial Bold", 15))
txt_entrada = Entry(ventana, width=10)
btn_leer = Button(ventana, text="Leer número", command=leerNumero)
lbl_resultado = Label(ventana, text="", font=("Arial Bold", 18))


lbl_mensaje.grid(column=0, row = 0)
txt_entrada.grid(column=1, row=0)
btn_leer.grid(column=0, row=1)
lbl_resultado.grid(column=0, row=2)

ventana.geometry('300x300')
ventana.mainloop()          # mostrar la ventana al usuario