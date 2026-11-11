import tkinter

#========================================================
#Definición de la clase Vehiculo y sus subclases
#========================================================
class Vehiculo:
    def __init__(self,marca, modelo, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_actual = velocidad_actual

    def acelerar(self, turbo=0, terreno=0):
        pass
    def detener(self, turbo=0, terreno=0):
        pass
    def obtener_informacion(self):
        pass


#========================================================
#Definición de las subclases de Vehiculo (Clases hijas)
#========================================================
# Con las clases hijas, se implementan los métodos acelerar y detener de manera específica para cada tipo de vehículo
# considerando factores como turbo y terreno.
# Esto afectando la velocidad actual del vehículo y limitando la velocidad máxima según el tipo de vehículo.
#========================================================
class AutoElectrico(Vehiculo):
    def acelerar(self, turbo=0, terreno=20):
        self.velocidad_actual += 90 - terreno
        self.velocidad_actual = min(self.velocidad_actual,300)
        

    def detener(self, turbo=0, terreno=5):
        self.velocidad_actual -= 90-terreno
        self.velocidad_actual = max(self.velocidad_actual, 0)

class Moto(Vehiculo):
    def acelerar(self, turbo=20, terreno=0):
         self.velocidad_actual += 5 + turbo - terreno
         self.velocidad_actual = min(self.velocidad_actual, 120)  # Limitar la velocidad máxima a 120 km/h
        
    def detener(self, turbo=20, terreno=0):
        self.velocidad_actual -= 60 - turbo
        self.velocidad_actual = max(self.velocidad_actual, 0)        
    
class Camion(Vehiculo):
    def acelerar(self, turbo=0, terreno=0):
        self.velocidad_actual += 16 + turbo - terreno
        self.velocidad_actual = min(self.velocidad_actual, 100)
        

    def detener(self, turbo=0, terreno=0):
        self.velocidad_actual -= 20
        self.velocidad_actual = max(self.velocidad_actual, 0)

#========================================================
#la siguiente clase es la guia para que en un futuro se pueda agregar otro vehiculo
# sin modificar gran parte del codigo, como lo indica la guia.
#========================================================
"""class Bicicleta(Vehiculo):
    def acelerar(self, turbo=0, terreno=0):
        self.velocidad_actual += 5 + turbo - terreno
        self.velocidad_actual = min(self.velocidad_actual, 50)
        

    def detener(self, turbo=0, terreno=0):
        self.velocidad_actual -= 10
        self.velocidad_actual = max(self.velocidad_actual, 0)"""



#========================================================
#Definición de la función para el boton acelerar
#========================================================
def boton_acelerar():
    for vehiculo in vehiculos:
            vehiculo.acelerar()
        #=======================================================================================
        #Actualización de los labels informando la velocidad máxima alcanzada por cada vehículo
        #=======================================================================================
            if isinstance(vehiculo, Moto) and vehiculo.velocidad_actual ==120:
                lbl_resultado1.config(text="La moto llego a su velocidad máxima de 120 km/h con turbo", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            elif isinstance(vehiculo, AutoElectrico) and vehiculo.velocidad_actual ==300:
                lbl_resultado2.config(text="El auto eléctrico llego a su velocidad máxima de 300 km/h, con un terreno hostil", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            elif isinstance(vehiculo, Camion) and vehiculo.velocidad_actual ==100:
                lbl_resultado3.config(text="El camión llego a su velocidad máxima de 100 km/h,sin turbo y sin terreno hostil", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            #========================================================
            #la dos siguientes lineas de codigo son la guia para que en un futuro se pueda agregar
            #otro vehiculo, sin modificar gran parte del codigo, como lo indica la guia.
            #========================================================
            """elif isinstance(vehiculo, Bicicleta) and vehiculo.velocidad_actual ==50:
                lbl_resultado4.config(text="La bicicleta llego a su velocidad máxima de 50 km/h, sin turbo y sin terreno hostil", font=("Times New Roman", 13), bg="#4682B4", fg="black")"""

#========================================================
#listo.box elimina los datos iniciales desde el índice 0 hasta el final y luego inserta los datos actualizados de cada vehículo en la lista.
#========================================================
    listbox.delete(0, tkinter.END)
    for vehiculo in vehiculos:
        listbox.insert(tkinter.END, f"{vehiculo.marca} {vehiculo.modelo} - Velocidad: {vehiculo.velocidad_actual} km/h")


#========================================================
#Definición de la función para el boton detener
#========================================================
def boton_detener():
    for vehiculo in vehiculos:
        vehiculo.detener()
        if isinstance(vehiculo, AutoElectrico) and vehiculo.velocidad_actual ==0:
            lbl_resultado2.config(text="the vehicle electric has stopped", font=("Times New Roman", 13), bg="#4682B4", fg="black")
        elif isinstance(vehiculo, Moto) and vehiculo.velocidad_actual ==0:
            lbl_resultado1.config(text="the motorcycle has stopped", font=("Times New Roman", 13), bg="#4682B4", fg="black")
        elif isinstance(vehiculo, Camion) and vehiculo.velocidad_actual ==0:
            lbl_resultado3.config(text="the truck has stopped", font=("Times New Roman", 13), bg="#4682B4", fg="black")
        #========================================================
        #la dos siguientes lineas de codigo son la guia para que en un futuro se pueda agregar
        #otro vehiculo, sin modificar gran parte del codigo, como lo indica la guia.
        #========================================================
        """elif isinstance(vehiculo, Bicicleta) and vehiculo.velocidad_actual ==0:
            lbl_resultado4.config(text="the bicycle has stopped", font=("Times New Roman", 13), bg="#4682B4", fg="black")"""

    listbox.delete(0, tkinter.END)
    for vehiculo in vehiculos:
        listbox.insert(tkinter.END, f"{vehiculo.marca} {vehiculo.modelo} - Velocidad: {vehiculo.velocidad_actual} km/h")



#========================================================
#Definición de la función para obtener información de los vehículos
#========================================================
def obtener_informacion_vehiculos():
    ventana_info = tkinter.Tk()
    ventana_info.title("Information about Vehicles")
    ventana_info.geometry("600x100")
    ventana_info.config(bg="#4682B4")
    for vehiculo in vehiculos:
        if isinstance(vehiculo, Moto):
            lblresultado = tkinter.Label(ventana_info, text=f"brand: {vehiculo.marca}, Model: {vehiculo.modelo} aceleración + turbo ", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            lblresultado.pack(pady=5)
        elif isinstance(vehiculo, AutoElectrico):
            lblresultado = tkinter.Label(ventana_info, text=f"brand: {vehiculo.marca}, Model: {vehiculo.modelo} aceleración + terreno hostil ", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            lblresultado.pack(pady=5)
        elif isinstance(vehiculo, Camion):
            lblresultado = tkinter.Label(ventana_info, text=f"brand: {vehiculo.marca}, Model: {vehiculo.modelo} aceleración + terreno hostil ", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            lblresultado.pack(pady=5)
        #========================================================
        #la dos siguientes lineas de codigo son la guia para que en un futuro se pueda agregar
        #otro vehiculo, sin modificar gran parte del codigo, como lo indica la guia.
        #========================================================
        """elif isinstance(vehiculo, Bicicleta):
            lblresultado = tkinter.Label(ventana_info, text=f"brand: {vehiculo.marca}, Model: {vehiculo.modelo} aceleración + terreno hostil ", font=("Times New Roman", 13), bg="#4682B4", fg="black")
            lblresultado.pack(pady=5)"""

#========================================================
#Creación de los objetos de las clases hijas
#========================================================
vehiculo1 = AutoElectrico("Tesla", "Model S")
vehiculo2 = Moto("Hero", "hunk 160R")
vehiculo3 = Camion("Volvo", "FH16")

#========================================================
#la siguiente linea de codigo es la guia para que en un futuro se pueda agregar otro vehiculo
#========================================================
"""Vehiculo4 = Bicicleta("GW", "BMX")"""


#========================================================
#Creación de la lista de vehículos
#========================================================
vehiculos=[vehiculo2, vehiculo1, vehiculo3]

#========================================================
#Creación de la ventana principal
#========================================================
ventana = tkinter.Tk() 
ventana.title(" VEHICLES SMART SIMULATOR")
ventana.config(bg="#4682B4") 
ventana.geometry("600x400")

#========================================================
#Creación de los labels para mostrar los resultados
#========================================================

global lbl_resultado
lbl_resultado1=tkinter.Label(ventana, background="#4682B4", font=("Times New Roman", 13), fg="black")
lbl_resultado1.pack()

lbl_resultado2=tkinter.Label(ventana, background="#4682B4", font=("Times New Roman", 13), fg="black")
lbl_resultado2.pack()

lbl_resultado3=tkinter.Label(ventana, background="#4682B4", font=("Times New Roman", 13), fg="black")
lbl_resultado3.pack()

#========================================================
#la siguiente linea de codigo es la guia para que en un futuro se pueda agregar otro vehiculo
#========================================================
lbl_resultado4=tkinter.Label(ventana, background="#4682B4", font=("Times New Roman", 13), fg="black")
lbl_resultado4.pack()

#========================================================
#Creación de los labels para mostrar los títulos y la lista de vehículos
#========================================================
tkinter.Label(ventana, text="One click = One second ", font=("Times New Roman", 16), bg="#4682B4", fg="black").pack(pady=0)
tkinter.Label(ventana, text="Vehicles", font=("Times New Roman", 16), bg="#4682B4", fg="black").pack(pady=0)



#========================================================
#Creación del listbox para mostrar la lista de vehículos
#========================================================
listbox = tkinter.Listbox(ventana, width=35, height=5, font=("Times New Roman", 13))
for vehiculo in vehiculos:
    listbox.insert(tkinter.END, f"{vehiculo.marca} {vehiculo.modelo} - Velocity: {vehiculo.velocidad_actual} km/h")
    listbox.pack(pady=10)

#========================================================
#Creación del frame para los botones
#========================================================
frame_botones = tkinter.Frame(ventana, bg="#4682B4")
frame_botones.pack(pady=10)


#========================================================
#Creación de los botones para acelerar, detener y obtener información
#========================================================
tkinter.Button(frame_botones, text="Accelerate", font=("Times New Roman", 13), command=boton_acelerar).pack(side=tkinter.LEFT, padx=5, pady=0)
tkinter.Button(frame_botones, text="Stop", font=("Times New Roman", 13), command=boton_detener).pack(side=tkinter.LEFT, padx=5, pady=0)
tkinter.Button(frame_botones, text="Get Information", font=("Times New Roman", 13), command=obtener_informacion_vehiculos).pack(side=tkinter.RIGHT,padx=5, pady=0)

#========================================================
#Ejecución del bucle principal de la ventana
#========================================================
ventana.mainloop()