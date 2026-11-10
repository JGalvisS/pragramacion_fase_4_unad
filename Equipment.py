import copy
from Service import Service


class Equipment(Service):
    __equipments = []

    def __init__(self, _name: str, _fee: float = 0.0, _description: str = "", _refundable_deposit: float = 0.0):
        for eq in Equipment.__equipments:
            if eq._name.lower() == _name.lower():
                _fee = eq._fee
                _description = eq._description
                _refundable_deposit = eq._refundable_deposit
        super().__init__(_name, _fee, _description)
        self._refundable_deposit = _refundable_deposit
       
    @classmethod
    def _load_initial_data(cls) -> None:
        if cls.__equipments:
            return
        cls.__equipments.extend([
            cls("Proyector", 80000, "Proyector HD con cable HDMI", 200000),
            cls("Sonido profesional", 150000, "Parlantes, micrófonos y consola", 300000),
            cls("Portátil", 60000, "Portátil con software de presentación", 500000),
        ])

    def calculate_cost(self, days: int = 1) -> float:
        total = (self._fee * days) + self._refundable_deposit
        return float(total)
    @staticmethod
    def get_description(name: str) -> str:
        for eq in Equipment.__equipments:
            if eq._name.lower() == name.lower():
                return f"Equipo: {eq._name}. {eq._description}"
        return f"No se encontró el equipo: {name}"
    @staticmethod
    def find_equipment(name: str) -> bool:
        for eq in Equipment.__equipments:
            if eq._name.lower() == name.lower():
                return True
        return False
    @staticmethod
    def get_all_equipments() -> list:
        return [copy.copy(eq) for eq in Equipment.__equipments]


Equipment._load_initial_data()



