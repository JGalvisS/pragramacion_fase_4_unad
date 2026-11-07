
CUSTOMER=[{"id":"1023957924","name":"Lorena Montoya","number_phone":3226949634},
          {"id":"1016634894","name":"Jorge Sanchez","number_phone":3158569963},
          {"id":"19219860","name":"Angel Velez","number_phone":3125644348},
          {"id":"AM432352","name":"Cecilia Bolivar","number_phone":3158621535}]
class Customer:
    #Constructor
    def __init__(self,_id:str,_name:str,_number_phone:int):
        self.id=_id
        self.name=_name
        self.number_phone=_number_phone
    
    #Add a new customer in CUSTOMER
    def create_customer(self):
        CUSTOMER.append({"id":self.id,"name":self.name,"number_phone":self.number_phone})
        if self.find_customer(self.id)==True:
            return True
        return False
    
    #Find a customer by id
    @staticmethod
    def find_customer(id:str):
        for i in CUSTOMER:
            if i["id"]==id:
                return True
        return False
"""   
print(Customer.find_customer("4564541"))
print(CUSTOMER)
customer1=Customer("AV45455","Maria Carmen",3158786523)
customer1.create_customer()
print(CUSTOMER)
"""