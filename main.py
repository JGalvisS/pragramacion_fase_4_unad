from datetime import date
import re
import Reservation
import Exception
import logging

print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("-------------//  WELCOME TO SOFTWARE FJ  //-------------")
print("--------------------------------------------------------")
print("--------------------------------------------------------")
#Start Fuction
while True:
    try:
        is_register=str(input("Are you registered in our system? yes/no "))
        is_register.lower()
        if is_register =="yes":
            pass
        if is_register =="no":
            #Register a new user and check their inputs
            while True:
                while True:
                    customer_id=str(input(f"We gonna start with your register \nPlease enter your id: "))
                    if re.match(r"^[A-Z0-9]+$",customer_id):
                        break
                    else:
                        print("Invalid ID. Only uppercase letters and numbers are allowed.")
                while True:
                    customer_name=str(input(" What is your full name? "))
                    if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",customer_name):
                        break
                    else:
                        print("Invalid name. Only letters are allowed.")
                while True:
                    customer_number_phone=str(input("what is your number phone? "))
                    if re.match(r"^(?:\+57\s*)?3\d{2}(?:\s*\d){7}$",customer_number_phone):
                        break
                    else:
                        print("Invalid phone number. Enter a 10-digit Colombian mobile number (optional +57).")
                break
            Reservation.Reservations.create_customer(customer_id,customer_name,int(customer_number_phone))
        print("Discover our services")
        print(Reservation.Reservations.get_all_services())
        break
    except Exception.Exception_System as err:
        logging.error("Error en la aplicación: %s", err)
        
            