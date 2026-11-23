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
        print("What would you like to do?")
        while True:
            action=input((f"""
                1. Reserve an event room
                2. Reserve an equipment
                3. Reserve a consulting
                4. Cancel a reservation 
                5. Consulting a reservation
                6. Discover each our services
                Mark number of the option that you want to select: """))
            if action.isdigit():
                action= int(action)
                if 1 <= action <= 6:
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 6")
            
        
        
        break
    except Exception.Exception_System as err:
        logging.error("Error en la aplicación: %s", err)
        
            