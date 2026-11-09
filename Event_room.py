from Service import Service


class Event_room(Service):
    _event_rooms = [] 

    def __init__(self, _name: str, _fee: float = 1000000, _description: str = ""):
        super().__init__(_name, _fee, _description)
        Event_room._event_rooms.append(self)

    def calculate_cost(self, fornature: bool = None, buffet: bool = None, days: int = 1) -> float:
        total_cost = self._fee * days
        if fornature:
            total_cost += 500000
        if buffet:
            total_cost += 300000
        return float(total_cost)

    @staticmethod
    def get_description(name: str) -> str:
        for room in Event_room._event_rooms:
            if room._name.lower() == name.lower():
                return f"Descripción del salón de eventos: {room._name}. {room._description}"
        return f"No se encontró el salón de eventos: {name}"

    @staticmethod
    def find_event_room(name: str) -> bool:
        return any(room._name.lower() == name.lower() for room in Event_room._event_rooms)

    @staticmethod
    def get_all_event_rooms() -> list:
        return list(Event_room._event_rooms)


