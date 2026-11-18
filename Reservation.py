from datetime import date
import Customer
import Exception
import logging
import Event_room
import re
import Equipment
import Consulting


RESERVATIONS=[]

class Reservations:
    #Constructor
    def __init__(self,_reservation_id:int, _customer_id:str,_service_type:str,_start_service:date,_finish_service:date,_duration:int,_cost:float,_state:bool):
        self.reservation_id=_reservation_id
        self.customer_id=_customer_id
        self.service_type=_service_type
        self.start_service=_start_service
        self.finish_service=_finish_service
        self.duration=_duration
        self.cost=_cost
        self.state=_state
    
    #Create a new customer
    @staticmethod
    def create_customer(id:str,name:str,number_phone:int):
        try:
            if Customer.Customer.find_customer(id):
                raise Exception.Exception_customer("The customer ID is already registered")
            expression_name= r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"
            if not re.match(expression_name,name):
                raise Exception.Exception_customer("Name field is invalid. Please try again using only letters")
            number_str=str(number_phone).strip()
            expression_number=r"^3\d{9}$"
            if not re.match(expression_number,number_str):
                raise Exception.Exception_customer("Number Phone field is invalid. Please try again using only Colombian number phone")
            new_customer =Customer.Customer(id,name,number_phone)
            is_created=new_customer.create_customer()
            if not is_created:
                raise Exception.Exception_customer(f"Customer with ID {id} created unsuccessfully.")
            logging.info(f"Customer with ID {id} created successfully.")
        except Exception.Exception_customer as err:
            logging.warning(f"Failed to create customer {id}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Customer with ID {id} created successfully.")
        finally:
            logging.info(f"Finished processing customer creation attempt for ID: {id}.")

    #Created Available_validate
    @staticmethod
    def available_validate(id:str, _service_type:str, _start_service:date, _finish_service:date):
        if not Customer.Customer.find_customer(id):
            raise Exception.Error_Invalid_Client("The customer ID is not registered")
        if _start_service > _finish_service:
            raise Exception.Exception_System("The start date cannot be greater than the finish date")
        for reservation in RESERVATIONS:
            if reservation.state == True and reservation.service_type.lower() == _service_type.lower() and  _start_service <= reservation.finish_service and _finish_service >= reservation.start_service:
                raise Exception.Service_Not_Available("The requested service is not available for the specified dates")
        return True

    #Created event_room_reserve
    @staticmethod
    def event_room_reserve (id:str, room_name:str, _start_service:date, _finish_service:date, fornature:bool = False, buffet: bool = False):
        try:
            if not Event_room.Event_room.find_event_room(room_name):
                    raise Exception.Service_Not_Available_Exception(f"The event room {room_name} is not existing")
            Reservations.available_validate(id, room_name, _start_service, _finish_service)
            days = (_finish_service - _start_service).days + 1
            room = Event_room.Event_room(room_name)
            total_cost = room.calculate_cost(fornature, buffet, days)
            reservation_id = len(RESERVATIONS) + 1
            new_reservation = Reservations(reservation_id, id, room_name, _start_service, _finish_service, days, total_cost, True)
            RESERVATIONS.append(new_reservation)
            logging.info(f"Reservation {reservation_id} for event room {room_name} created successfully.")
        except (Exception.Error_Invalid_Client, Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to create reservation for event room {room_name}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Reservation {reservation_id} for event room {room_name} created successfully.")
        finally:
            logging.info(f"Finished processing reservation attempt for event room {room_name}.")

    @staticmethod
    def equipment_reserve(id:str, equipment_name:str, _start_service:date, _finish_service:date):
        try:
            if not Equipment.Equipment.find_equipment(equipment_name):
                    raise Exception.Service_Not_Available_Exception(f"The equipment {equipment_name} is not existing")
            Reservations.available_validate(id, equipment_name, _start_service, _finish_service)
            days = (_finish_service - _start_service).days + 1
            equipment = Equipment.Equipment(equipment_name)
            total_cost = equipment.calculate_cost(days)
            reservation_id = len(RESERVATIONS) + 1
            new_reservation = Reservations(reservation_id, id, equipment_name, _start_service, _finish_service, days, total_cost, True)
            RESERVATIONS.append(new_reservation)
            logging.info(f"Reservation {reservation_id} for equipment {equipment_name} created successfully.")
        except (Exception.Error_Invalid_Client, Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to create reservation for equipment {equipment_name}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Reservation {reservation_id} for equipment {equipment_name} created successfully.")
        finally:
            logging.info(f"Finished processing reservation attempt for equipment {equipment_name}.")



#Reservations.create_customer("1023957","Jose Lopez", 3184454525)