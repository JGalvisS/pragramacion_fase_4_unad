import copy
from Service import Service

class Event_room(Service):
    __event_rooms = []

    def __init__(self, _name: str, _fee: float = 1000000, _description: str = ""):
        for room in Event_room.__event_rooms:
            if room._name.lower() == _name.lower():
                _fee = room._fee
                _description = room._description
        super().__init__(_name, _fee, _description)
        
    @classmethod
    def _load_initial_data(cls) -> None:
        if cls.__event_rooms:
            return
        cls.__event_rooms.extend([
            cls("Salón Diamante", 1000000, "Capacidad para 100 personas"),
            cls("Salón Esmeralda", 1500000, "Capacidad para 200 personas"),
            cls("Salón de Oro", 800000, "Capacidad para 50 personas"),
        ])
        
    def calculate_cost(self, fornature: bool = None, buffet: bool = None, days: int = 1) -> float:
        total_cost = self._fee * days
        if fornature:
            total_cost += 500000
        if buffet:
            total_cost += 300000
        return float(total_cost)
        
    @staticmethod
    def get_description(name: str) -> str:
        for room in Event_room.__event_rooms:
            if room._name.lower() == name.lower():
                return f"Descripción del salón de eventos: {room._name}. {room._description}"
        return f"No se encontró el salón de eventos: {name}"
    @staticmethod
    def find_event_room(name: str) -> bool:
        for room in Event_room.__event_rooms:
            if room._name.lower() == name.lower():
                return True
        return False
    @staticmethod
    def get_all_event_rooms() -> list:
        return [copy.copy(room) for room in Event_room.__event_rooms]


Event_room._load_initial_data()



