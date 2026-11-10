import copy
from Service import Service


class Consulting(Service):
    __consultings = []
    def __init__(self, _name: str, _fee: float = 0.0, _description: str = ""):
        for c in Consulting.__consultings:
            if c._name.lower() == _name.lower():
                _fee = c._fee
                _description = c._description
        super().__init__(_name, _fee, _description)
       
    @classmethod
    def _load_initial_data(cls) -> None:
        if cls.__consultings:
            return
        cls.__consultings.extend([
            cls("Consultoría de eventos", 300000, "Planeación y coordinación de eventos"),
            cls("Consultoría tecnológica", 500000, "Asesoría en tecnología y sistemas"),
            cls("Consultoría logística", 400000, "Organización de recursos y proveedores"),
        ])
    def calculate_cost(self, hiring_model: str, in_site: bool = None) -> float:
        total = self._fee
        if in_site:
            total += 150000
        return float(total)

    @staticmethod
    def get_description(name: str) -> str:
        for c in Consulting.__consultings:
            if c._name.lower() == name.lower():
                return f"Consultoría: {c._name}. {c._description}"
        return f"No se encontró la consultoría: {name}"
    @staticmethod
    def find_consulting(name: str) -> bool:
        for c in Consulting.__consultings:
            if c._name.lower() == name.lower():
                return True
        return False
    @staticmethod
    def get_all_consulting() -> list:
        return [copy.copy(c) for c in Consulting.__consultings]


Consulting._load_initial_data()



