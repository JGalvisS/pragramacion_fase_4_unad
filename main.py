from datetime import date
import re
import Reservation
import Exception
import logging
import Event_room
import Customer

print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("-------------//  WELCOME TO SOFTWARE FJ  //-------------")
print("--------------------------------------------------------")
print("--------------------------------------------------------") 
#Start 
while True:
    try:
        is_register=str(input("Are you registered in our system? yes/no "))
        is_register.lower()
        if is_register =="yes":
            pass
        if is_register =="no":
            #Register a new user and check their inputs
            while True:
                #check customer_id
                while True:
                    customer_id=str(input(f"We gonna start with your register \nPlease enter your id: "))
                    if re.match(r"^[A-Z0-9]+$",customer_id):
                        break
                    else:
                        print("Invalid ID. Only uppercase letters and numbers are allowed.")
                #check customer name
                while True:
                    customer_name=str(input(" What is your full name? "))
                    if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",customer_name):
                        break
                    else:
                        print("Invalid name. Only letters are allowed.")
                #check customer number phone
                while True:
                    customer_number_phone=str(input("what is your number phone? "))
                    if re.match(r"^(?:\+57\s*)?3\d{2}(?:\s*\d){7}$",customer_number_phone):
                        break
                    else:
                        print("Invalid phone number. Enter a 10-digit Colombian mobile number (optional +57).")
                break
            Reservation.Reservations.create_customer(customer_id,customer_name,int(customer_number_phone))
        print("What would you like to do?")
        #Ask select an action to user
        while True:
            action=input((f"""
                1. Reserve an event room
                2. Reserve an equipment
                3. Reserve a consulting
                4. Cancel a reservation 
                5. Consulting a reservation
                6. Discover each our services
                Mark number of the option that you want to select: """))
            #che selection
            if action.isdigit():
                action= int(action)
                if 1 <= action <= 6:
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 6")
        #Switch case
        match action:
            case 1:
                while True:
                    #check
                    while True:
                        print(Reservation.Reservations.get_descriptions_by_service("EVENT_ROOM"))
                        name_room=input("Which room would you like to reserve? ").strip().lower()
                        validate_room_name=Event_room.Event_room.find_event_room(name_room)
                        if validate_room_name ==True:
                            break
                        else:
                            ("Invalid event room name, Please try it again.")
                    while True:
                        customer_id_room=input("What is your ID? ")
                        if re.match(r"^[A-Z0-9]+$",customer_id_room):
                            find_customer=Customer.Customer.find_customer(customer_id_room)
                            if  find_customer==True:
                                break
                            else:
                                print("The customer ID is not registered, please try it again")
                        else:
                            print("Invalid ID. Only uppercase letters and numbers are allowed.")
                    while True:
                        start_room=input("When would you like start the service? YYYY-MM-DD: ").strip()
                        if re.fullmatch(r"\d{4}-\d{2}-\d{2}",start_room):
                            start_room_format=date.fromisoformat(start_room) 
                            break
                        else:
                            print("Invalid start date. Please enter date in format YYYY-MM-DD")
                    while True:
                        finish_room=input("When would you like finish the service? YYYY-MM-DD: ").strip()
                        if re.fullmatch(r"\d{4}-\d{2}-\d{2}",finish_room):
                            finish_room_format=date.fromisoformat(finish_room)
                            break
                        else: 
                            print("Invalid start date. Please enter date in format YYYY-MM-DD")
                    if Reservation.Reservations.available_validate(customer_id_room,name_room,start_room_format,finish_room_format)==True:
                        break
                    else:
                        print(f"The {name_room} event room is not available try it again.")
                while True:
                    include_furniture=input("Would you like include furniture service? yes/no: ").strip().lower()
                    if include_furniture=="yes":
                        furniture=True
                        break
                    elif include_furniture=="no":
                        furniture=False
                        break
                    else: 
                        print("Invalid option. Please answer yes or no")
                while True:
                    include_buffet=input("Would you like include buffet service? yes/no: ").strip().lower()
                    if include_buffet=="yes":
                        buffet=True
                        break
                    elif include_buffet=="no":
                        buffet=False
                        break
                    else: 
                        print("Invalid option. Please answer yes or no")
                calculate_days=(finish_room_format-start_room_format).days
                print("We are calculate a budget...")
                calculate_cost_room=Event_room.Event_room.calculate_cost_by_name(name_room,furniture,buffet, calculate_days)
                print(f"This reservation will have a cost of ${calculate_cost_room}")
                reserve=input("Would you like continue with the reservation? yes/no: ").strip().lower()
                if reserve=="yes":
                    len_reservations_before=len(Reservation.RESERVATIONS)
                    Reservation.Reservations.event_room_reserve(customer_id_room,name_room,start_room_format,finish_room_format,furniture,buffet)
                    if len(Reservation.RESERVATIONS)>len_reservations_before:
                        print("Your Reservation has been registered successfully ")
                        print(Reservation.Reservations.get_reservation(len(Reservation.RESERVATIONS)))
                elif reserve=="no":
                    print("Please come back soon, Bye")
                    
                    
                    
            
            
        
        
        break
    except Exception.Exception_System as err:
        logging.error("Error en la aplicación: %s", err)
        
            