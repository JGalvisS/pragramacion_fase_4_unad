from datetime import date
import Customer
import Exception
import logging
import Event_room
import re
import Equipment
import Consulting

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
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
            if reservation["state"] == True and reservation["service_type"].lower() == _service_type.lower() and  _start_service <= reservation["finish_service"] and _finish_service >= reservation["start_service"]:
                raise Exception.Service_Not_Available_Exception("The requested service is not available for the specified dates")
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
            RESERVATIONS.append(new_reservation.__dict__)
            logging.info(f"Reservation {reservation_id} for event room {room_name} created successfully.")
        except (Exception.Error_Invalid_Client, Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to create reservation for event room {room_name}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Reservation {reservation_id} for event room {room_name} created successfully.")
        finally:
            logging.info(f"Finished processing reservation attempt for event room {room_name}.")

    #Created equipment_reserve
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
            RESERVATIONS.append(new_reservation.__dict__)
            logging.info(f"Reservation {reservation_id} for equipment {equipment_name} created successfully.")
        except (Exception.Error_Invalid_Client, Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to create reservation for equipment {equipment_name}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Reservation {reservation_id} for equipment {equipment_name} created successfully.")
        finally:
            logging.info(f"Finished processing reservation attempt for equipment {equipment_name}.")

    #Created consulting_reserve
    @staticmethod
    def consulting_reserve(id:str, consulting_name:str, _start_service:date, _finish_service:date, hiring_model:str, in_site:bool = False):
        try:
            if not Consulting.Consulting.find_consulting(consulting_name):
                    raise Exception.Service_Not_Available_Exception(f"The consulting service {consulting_name} is not existing")
            Reservations.available_validate(id, consulting_name, _start_service, _finish_service)
            days = (_finish_service - _start_service).days + 1
            consulting = Consulting.Consulting(consulting_name)
            total_cost = consulting.calculate_cost(hiring_model, in_site)
            reservation_id = len(RESERVATIONS) + 1
            new_reservation = Reservations(reservation_id, id, consulting_name, _start_service, _finish_service, days, total_cost, True)
            RESERVATIONS.append(new_reservation.__dict__)
            logging.info(f"Reservation {reservation_id} for consulting service {consulting_name} created successfully.")
        except (Exception.Error_Invalid_Client, Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to create reservation for consulting service {consulting_name}: {err}")
            print(f"Warning: {err}")
        else:
            print(f"Reservation {reservation_id} for consulting service {consulting_name} created successfully.")
        finally:
            logging.info(f"Finished processing reservation attempt for consulting service {consulting_name}.")

#Helper method to format lists into clean strings
    @staticmethod
    def _format_list(title: str, items: list) -> str:
        if not items:
            return f"\n--- {title} ---\nNo items available.\n"
        text = f"\n--- {title} ---\n"
        count = 1
        for item in items:
            if isinstance(item, dict):
                details = " | ".join([f"{key}: {value}" for key, value in item.items()])
                text += f"{count}. {details}\n"
            elif hasattr(item, "__dict__"):
                details = " | ".join([f"{key}: {value}" for key, value in item.__dict__.items()])
                text += f"{count}. {details}\n"
            else:
                text += f"{count}. {item}\n"
            count += 1
        return text

    #Created get_all_services
    @staticmethod
    def get_all_services() -> str:
        try:
            rooms = Event_room.Event_room.get_all_event_rooms()
            if hasattr(Equipment.Equipment, "get_all_equipments"):
             equipments = Equipment.Equipment.get_all_equipments()
            else:
             equipos = Equipment.Equipment.gell_all_equipments()
            if hasattr(Consulting.Consulting, "get_all_consultings"):
             consultings = Consulting.Consulting.get_all_consultings()
            else:
             consultings = Consulting.Consulting.get_all_consulting()

            output = "\n========================================\n"
            output += "       AVAILABLE SERVICES LIST\n"
            output += "========================================"
            output += Reservations._format_list("EVENT ROOMS", rooms)
            output += Reservations._format_list("EQUIPMENTS", equipments)
            output += Reservations._format_list("CONSULTING SERVICES", consultings)
            output += "========================================\n"
            logging.info("All available services were listed successfully.")
        except BaseException as err:
         logging.error(f"Error getting all services: {err}")
         raise Exception.Exception_System("Failed to load the services list.") from err
        else:
            return output
        finally:
            logging.info("Finished processing get_all_services request.")

    #Created get_descprition
    @staticmethod
    def get_descprition(type: str, name: str) -> str:
        try:
            if not type or not name:
                raise Exception.Exception_System("Service type and name cannot be empty.")

            service_type = type.strip().lower()
            service_name = name.strip()

            if service_type in ["event_room", "sala", "room"]:
                if not Event_room.Event_room.find_event_room(service_name):
                    raise Exception.Service_Not_Available_Exception(f"The event room {service_name} does not exist.")
                description = Event_room.Event_room.get_description(service_name)
            elif service_type in ["equipment", "equipo"]:
                if not Equipment.Equipment.find_equipment(service_name):
                    raise Exception.Service_Not_Available_Exception(f"The equipment {service_name} does not exist.")
                description = Equipment.Equipment.get_description(service_name)
            elif service_type in ["consulting", "asesoria", "asesoría"]:
                if not Consulting.Consulting.find_consulting(service_name):
                    raise Exception.Service_Not_Available_Exception(f"The consulting service {service_name} does not exist.")
                description = Consulting.Consulting.get_description(service_name)
            else:
                raise Exception.Exception_System(f"Service type '{type}' is not valid. Use event_room, equipment or consulting.")

            logging.info(f"Description found for {service_type}: {service_name}.")
        except (Exception.Service_Not_Available_Exception, Exception.Exception_System) as err:
            logging.warning(f"Failed to get description for {name}: {err}")
            print(f"Warning: {err}")
            return f"Warning: {err}"
        else:
            return f"Service: {service_name} ({service_type}) -> Description: {description}"
        finally:
            logging.info(f"Finished processing get_descprition for {name}.")

    #Alias in case main calls get_description without typo
    @staticmethod
    def get_description(type: str, name: str) -> str:
        return Reservations.get_descprition(type, name)

    #Created get_all_by_service
    @staticmethod
    def get_all_by_service(service_type: str = None) -> str:
        try:
            if not RESERVATIONS:
                raise Exception.Service_Not_Available_Exception("There are no reservations registered yet.")

            filtered_list = []
            if service_type:
                for res in RESERVATIONS:
                    if res["service_type"].lower() == service_type.strip().lower():
                        filtered_list.append(res)
                if not filtered_list:
                    raise Exception.Service_Not_Available_Exception(f"No reservations found for service '{service_type}'.")
            else:
                filtered_list = RESERVATIONS

            header = f"RESERVATIONS FOR: {service_type.upper()}" if service_type else "ALL RESERVATIONS"
            result = "\n========================================\n"
            result += f"  {header}\n"
            result += "========================================\n"

            for res in filtered_list:
                status_str = "Active" if res["state"] else "Cancelled"
                result += (
                    f"ID: {res['reservation_id']} | Customer: {res['customer_id']} | "
                    f"Service: {res['service_type']} | From: {res['start_service']} to {res['finish_service']} | "
                    f"Days: {res['duration']} | Cost: ${res['cost']:,.2f} | State: {status_str}\n"
                )
            result += "========================================\n"
            logging.info(f"Listed {len(filtered_list)} reservations successfully.")
        except Exception.Service_Not_Available_Exception as err:
            logging.warning(f"Failed to list reservations by service: {err}")
            print(f"Warning: {err}")
            return f"Warning: {err}"
        else:
            return result
        finally:
            logging.info("Finished processing get_all_by_service request.")

    #Created get_reservation
    @staticmethod
    def get_reservation(reservation_id: int) -> str:
        try:
            if not isinstance(reservation_id, int) or reservation_id <= 0:
                raise Exception.Exception_System("The reservation ID must be a positive integer.")

            found_reservation = None
            for res in RESERVATIONS:
                if res["reservation_id"] == reservation_id:
                    found_reservation = res
                    break

            if not found_reservation:
                raise Exception.Service_Not_Available_Exception(f"Reservation with ID {reservation_id} was not found.")

            status_str = "Active" if found_reservation["state"] else "Cancelled"
            info = (
                f"\n--- RESERVATION DETAILS #{found_reservation['reservation_id']} ---\n"
                f"Customer ID  : {found_reservation['customer_id']}\n"
                f"Service      : {found_reservation['service_type']}\n"
                f"Start Date   : {found_reservation['start_service']}\n"
                f"Finish Date  : {found_reservation['finish_service']}\n"
                f"Duration     : {found_reservation['duration']} days\n"
                f"Total Cost   : ${found_reservation['cost']:,.2f}\n"
                f"State        : {status_str}\n"
                f"-----------------------------------\n"
            )
            logging.info(f"Reservation {reservation_id} consulted successfully.")
        except (Exception.Exception_System, Exception.Service_Not_Available_Exception) as err:
            logging.warning(f"Failed to get reservation {reservation_id}: {err}")
            print(f"Warning: {err}")
            return f"Warning: {err}"
        else:
            return info
        finally:
            logging.info(f"Finished processing get_reservation for ID: {reservation_id}.")

    #Created cancel_reservation
    @staticmethod
    def cancel_reservation(reservation_id: int) -> str:
        try:
            if not isinstance(reservation_id, int) or reservation_id <= 0:
                raise Exception.Exception_System("The reservation ID must be a positive integer.")

            found_reservation = None
            for res in RESERVATIONS:
                if res["reservation_id"] == reservation_id:
                    found_reservation = res
                    break

            if not found_reservation:
                raise Exception.Service_Not_Available_Exception(f"Reservation with ID {reservation_id} does not exist.")

            if not found_reservation["state"]:
                raise Exception.Exception_System(f"Reservation {reservation_id} is already cancelled.")

            found_reservation["state"] = False
            logging.info(f"Reservation {reservation_id} cancelled successfully.")
        except (Exception.Exception_System, Exception.Service_Not_Available_Exception) as err:
            logging.warning(f"Failed to cancel reservation {reservation_id}: {err}")
            print(f"Warning: {err}")
            return f"Warning: {err}"
        else:
            msg = f"Reservation {reservation_id} for {found_reservation['service_type']} was cancelled successfully."
            print(msg)
            return msg
        finally:
            logging.info(f"Finished processing cancel_reservation for ID: {reservation_id}.")
#Create a new customer
#Reservations.create_customer("1023957","Jose Lopez", 3184454525)

#Reserve an event room
#Reservations.event_room_reserve("1023957", "Salón Diamante", date(2026, 11, 20), date(2026, 11, 22), True, False)

#Failed to reserve an event room
#Reservations.event_room_reserve("1023957", "Salón Diamante", date(2026, 11, 21), date(2026, 11, 23), False, True)

#Reserve equipment
#Reservations.equipment_reserve("1023957", "Proyector", date(2026, 11, 20), date(2026, 11, 21))

#Reserve consulting service
#Reservations.consulting_reserve("1023957", "Consultoría tecnológica", date(2026, 11, 25), date(2026, 11, 26), "Por horas", True)
#Reserve consulting service
#Reservations.consulting_reserve("1023957", "Consultoría tecnológica", date(2026, 11, 25), date(2026, 11, 26), "Por horas", True)
