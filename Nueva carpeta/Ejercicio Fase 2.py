import tkinter
#Creacion de clase Usuario
class Usuario:
#Definimos cual usuario y clave daran acceso.
    def __init__(self):
        self.__usuario = "admin"
        self.__clave = "admin"
#Implementación del metodo validar.
    def validar(self, usuario, clave):
        return usuario == self.__usuario and clave == self.__clave


#Creacion de clase reservasala
class ReservaSala:

    def __init__(self, usuario, hora_inicio, tarifa_hora):
        self.__usuario = usuario
        self.__hora_inicio = hora_inicio
        self.__tarifa_hora = tarifa_hora

    def registrar_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def registrar_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    #el metodo Calcular_costo tiene la condición de que el numero que se ingrese tiene que estar entre 1 y 24 y hora_fin debe ser mayor 
    # a la hora inicio.
    def calcular_costo(self, hora_fin):
        if 1<= hora_fin <= 24 and hora_fin > self.__hora_inicio:
            self.__hora_fin = hora_fin
            #para calculcar el costo, restamos la hora fin a la hora de inicio y lo multiplicamos por la tarifa por hora que se haya ingresado
            costo = (self.__hora_fin - self.__hora_inicio)*self.__tarifa_hora
            return costo
        #si la condición del if no se cumple retornara a calcular_costo el valor de none.
        else:
            return None
    #Este metodo nos ayuda a que el programa al registrar y calcular llame el nombre de usuario y pueda mostranos el valor. 
    def obtener_usuario(self):
        return self.__usuario


#Creación de la funciono que permite calcular el costo de la reserva y registrar la hora de fin
def calcular_y_registrar():
    #Si al momento de darle al boton de registrar y calcular dtecta que esta vacio le dara un mensaje de error. 
    if txt_hora_fin.get()=="":
        lbl_resultado.config(text="Error: Please enter the end hour.", font=("Times New Roman", 14),background="#4682B4")
        return

    try:
        #Si el usuario si introduce una hora fin, pero no selecciona la reserva, le genera error indicandole que seleccione una reserva. 
        seleccion=listbox.curselection()
        if not seleccion:
            lbl_resultado.config(text="Error: No reservation selected.", font=("Times New Roman", 14),background="#4682B4")
            return
        #reserva seleccionada sera tomara el valor que se seleccione en la lista de reservas.
        reserva_seleccionada=lista_reservas[listbox.curselection()[0]]

        #hora_fin tomara el valor que se introdujo en el label de txt_hora_fin en formato entero.
        hora_fin=int(txt_hora_fin.get())

        #costa_total hara la validación si todos los parametrs enteriores se cumples y el metodo calcular_costo hara las validaciones.
        costo_total=reserva_seleccionada.calcular_costo(hora_fin)

        #si el costo total no es "None" dara el resultado de costo de la reserva. 
        if costo_total is not None:
            #Elimina la reserva seleccionada.
            listbox.delete(listbox.curselection())
            lbl_resultado.config(text=f"Total cost for {reserva_seleccionada.obtener_usuario()}: ${costo_total:.2f}", font=("Times New Roman", 14),background="#4682B4")

           

        #Si el valor que se introdujo en costo_total no cumple con los parametros en el metodo costo_total generara error.
        else:
            lbl_resultado.config(text="Error: Hour invalid or End hour must be greater than start hour.", font=("Times New Roman", 14), background="#4682B4")

    #Esto es una excepcion de indexerror, se utiliza para que en casod de que .curselection intente ingresar o seleccionar un elemento de la ista
    #que no existe el programa no se congele o genere error en consola, de lo contrario muestre el mensaje de error.
    except IndexError:
       lbl_resultado.config(text="Error: No reservation selected.", font=("Times New Roman", 14), background="#4682B4") 

    #Esta excepcipn de value error se utiliza para que en caso de que el usuario ingrese un str en vez de un int, el programa no se rompa
    #y unicamente le indique ese valor no es correcto. 
    except ValueError:
        lbl_resultado.config(text="Error: please enter a valid number for the end hour.", font=("Times New Roman", 14), background="#4682B4")

    
#Creacion de lista para almacenar las reservas y funcion para crear reservas
lista_reservas = []

def crear_reserva():

    #En caso de que el usuario en los campos deje todo en blanco le generar error, esto para asegurarse de que todo se diligencie antes de continuar.
    if txt_usuario.get() == "" or txt_hora_inicio.get() == "" or txt_tarifa_hora.get() == "":
        lbl_resultado.config(text="Error: Please fill in all fields.", font=("Times New Roman", 14), background="#4682B4")

    else:
        #hora_inicio tomara el valor que se le ingrese en la entrada.
        hora_inicio = int(txt_hora_inicio.get())
        #Si el numero que se ingresa esta entre 1 y 24 continua la funcion if
        if 1 <= hora_inicio <= 24:

            #usuario tomara el varlo que se le ingrese en la entrada.
            usuario=txt_usuario.get()
            #Hora_inicio tomara el valor que se le ingrese en la entrada y lo convertira en un int.
            hora_inicio=int(txt_hora_inicio.get())
            #tarifa_hora tomara el valor que se le ingrese en la entrada y lo convertira en un float.
            tarifa_hora=float(txt_tarifa_hora.get())
            #crea una instancia de reservasala a la cual se le pasaran los datos dentro de los parentesis
            reserva = ReservaSala(usuario, hora_inicio, tarifa_hora)
            #a la lista_reservas se le agrega la reserva con los parametros.
            lista_reservas.append(reserva)


            #En esta parte del codigo se le aplica el .pack a las funciones anteriormente creadas, en este punto es donde 
            #Se le indica alcodigo que una vez se cumpla las condiciones anteriores haga aparecer la etiqueta, la entrada y el boton.
            lbl_hora_fin.pack()
            txt_hora_fin.pack(pady=5)
            btn_calcular_costo.pack(pady=5)

            #Muestra una etiqueta que confirme la reservación. 
            lbl_resultado.config(text=f"Reservation created for {usuario} at {hora_inicio} with a rate of {tarifa_hora} per hour.", font=("Times New Roman", 14), background="#4682B4")

            #cada vez que el proceso llegue a este punto agregara la reserva en la ultima pocision de la lista.
            listbox.insert(tkinter.END, f"Reservation for {usuario} hour start {hora_inicio} with a rate of {tarifa_hora} per hour")

        #Si el numero esta por fuea del rango del if generara este mensaje de error, donde se le indica que ingrese un numero entre 1 y 24
        else:
            lbl_resultado.config(text="Error: Please enter a valid start hour between 1 and 24.", background="#4682B4")

#creación de ventana principal
def abrir_ventana_principal():
    ventana_principal = tkinter.Tk()
    ventana_principal.title("Study Room Reservation")
    ventana_principal.geometry("700x700")
    ventana_principal.config(bg="#4682B4")


    #Declaramos global la funciones para puedan acceder a ellas desde diferentes partes del codigo sin problemas.
    global listbox
    listbox = tkinter.Listbox(ventana_principal, width=70, bg="#ECECFA" , font=("Times New Roman", 14))
    listbox.pack(pady=20)

    #Creamos una etiqueta llamada User
    tkinter.Label(ventana_principal, text="User", font=("Times New Roman", 24), background="#4682B4").pack()
    #Declaramos que txt es global para que se pueda acceder en otras funciones.
    global txt_usuario
    #Creamos una entrada donde le indicamos al codigo que txt_usuario sera igual a lo que el usuario ingrese.
    txt_usuario = tkinter.Entry(ventana_principal)
    # Lo empaquetamos para que sea visible en la ventana. 
    txt_usuario.pack()

    tkinter.Label(ventana_principal, text="Hour Start", font=("Times New Roman", 24), background="#4682B4").pack()
    global txt_hora_inicio
    txt_hora_inicio=tkinter.Entry(ventana_principal)
    txt_hora_inicio.pack()

    #Declaramos 3 valores globales, la etiqueta, el texto y el boton de calcular costo 
    #esto sin agregarles el .pack para que desde un inicio no aparezcan, si no hasta que se realice la primera reserva
    global lbl_hora_fin, txt_hora_fin, btn_calcular_costo
    lbl_hora_fin = tkinter.Label(ventana_principal, text="Hour End", font=("Times New Roman", 24), background="#4682B4")
    txt_hora_fin = tkinter.Entry(ventana_principal)

    #Creamos el boton calcular costo con el comando de nuestro metodo calcular_y_registrar
    btn_calcular_costo = tkinter.Button(ventana_principal, text="Register and Calculate Cost", font=("Times New Roman", 18),background="#838485", command=calcular_y_registrar)

    #Creamos la etiqueta de la tarifa junto con su entrada 
    tkinter.Label(ventana_principal, text="Tariff per Hour", font=("Times New Roman", 24),background="#4682B4").pack()
    global txt_tarifa_hora
    txt_tarifa_hora = tkinter.Entry(ventana_principal)
    txt_tarifa_hora.pack(pady=10)

    #Boton_creación de reserva con el comando del metodo crear_reserva. 
    tkinter.Button(ventana_principal, text="Create Reservation", font=("Times new roman",18),background="#838485", command=crear_reserva).pack(pady=10)

    global lbl_resultado
    #Este lbl crea un espacio para que aparezcan mensajes de error o los resultados de las funciones
    lbl_resultado=tkinter.Label(ventana_principal, background="#4682B4")
    lbl_resultado.pack(pady=10)


#Creacion del objeto login
usuario = Usuario()

#Funcion de inicio/login
#Get significa leamos el valor que se encuentra en la caja de texto.
def login():

    #Aca llamamos al metodo validar le indicamos que si el txt de usuario y clave son igual a los que se introdujeron en 
    # el metodo validar genere un mensaje que diga User Correct
    if usuario.validar(txt_usuario.get(), txt_clave.get()):
        lbl_resultado.config(text="User Correct")
        ventana.timer = ventana.after(2000, ventana.destroy)  # Cierra la ventana después de 2 segundos
        abrir_ventana_principal()
    else:
    # Si el usuario y contraseña no coinciden generar un mensaje que diga User or Password incorrect.
        lbl_resultado.config(text="User or Password incorrect", background="#4682B4", font=("Times New Roman", 14) )
        ventana.timer = ventana.after(3000, ventana.destroy) #cerrar ventana despues de 3 segundos. 

#Ventana login
ventana = tkinter.Tk() #Aca invocamos o le decimos al codigo que me genere una ventana
ventana.title("Validation User") #Titulo de la ventana de login
ventana.config(bg="#4682B4") #Color del fondo de la pantalla 
#Tamaño de la ventana
ventana.geometry("300x300") #Resolucion de pixeles de la ventana

#aca creamos un titulo en la ventana que diga "User"
tkinter.Label(ventana, text="User:", font=("Times new roman", 24), background="#4682B4").pack() 
#cuadro blanco donde se introduciran los caracteres 
txt_usuario = tkinter.Entry(ventana) 
#empaquetamos para que sea visible en la ventana. 
txt_usuario.pack(pady=5) 

#Creamos nuevamente un titulo, esta vez con la palabra password teniendo en cuenta la misma estructura de User
tkinter.Label(ventana, text="Password:", font=("Times new roman", 24),background="#4682B4").pack()
txt_clave = tkinter.Entry(ventana)
txt_clave.pack(pady=5)

#Creamos un boton que tenga como texto Login, y que al presionarlo realice la funcion de login.
tkinter.Button(ventana, text="Login", font=("Times new roman",18), background="#838485", command=login).pack(pady=10) 

lbl_resultado=tkinter.Label(ventana, background="#4682B4")
lbl_resultado.pack(pady=30)

#El mainloop, permie que la ventana permanezca abierta hasta que el usuario interacture de los contrario, el codigo se lee en milisegundos y se cierra.
ventana.mainloop()
