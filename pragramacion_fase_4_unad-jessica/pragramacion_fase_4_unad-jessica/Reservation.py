from datetime import date
import Customer
import Exception
import logging
import re

RESERVATIONS=[]

class Reservations:
    #Constructor
    def __init__(self,_reservation_id:int, _customer_id:str,_service_type:str,_start_service:date,_finish_service:date,_duration:int,_cost:float,_state:bool):
        self.reservation_id=_reservation_id
        self.customer_id=_customer_id
        self.service_type=_service_type
        self.start_service=_service_type
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
            
#Reservations.create_customer("1023957","Jose Lopez", 3184454525)