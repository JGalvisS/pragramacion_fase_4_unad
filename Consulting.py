from Service import Service
class Consulting(Service):
    _consultings = []

    def __init__(self, _name: str, _fee: float, _description: str = ""):
        super().__init__(_name, _fee, _description)
        Consulting._consultings.append(self)

    def calculate_cost(self, hiring_model: str, in_site: bool = None) -> float:
        total = self._fee
        if in_site:
            total += 150000
        return float(total)

    @staticmethod
    def get_description(name: str) -> str:
        for consulting in Consulting._consultings:
            if consulting._name.lower() == name.lower():
                return f"Consultoría: {consulting._name}. {consulting._description}"
        return f"No se encontró la consultoría: {name}"

    @staticmethod
    def find_consulting(name: str) -> bool:
        return any(c._name.lower() == name.lower() for c in Consulting._consultings)

    @staticmethod
    def get_all_consulting() -> list:
        return list(Consulting._consultings)


