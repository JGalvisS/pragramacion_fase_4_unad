from datetime import date
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