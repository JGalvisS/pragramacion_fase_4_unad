from Service import Service

class Event_room(Service):
    
    def __init__(self, _name: str, _fee: float = 1000000, _description: str = ""):
        super().__init__(_name, _fee, _description)
        self._fee = _fee  

    def calculate_cost(self, fornature: bool = None, buffet: bool = None, days: int = 1) -> float:
        total_cost = self._fee * days
        if fornature:
            total_cost += 50000
        if buffet:
            total_cost += 300000
        return float(total_cost)

    @staticmethod
    def get_description(_name: str) -> str:
        return f"Descripción del salón de eventos: {_name}"

    @staticmethod
    def find_event_room(name: str) -> bool:
        return True

    @staticmethod
    def get_all_event_rooms() -> list:
        return []
