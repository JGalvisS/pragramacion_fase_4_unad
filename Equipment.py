from Service import Service


class Equipment(Service):
    _equipments = []

    def __init__(self, _name: str, _fee: float, _description: str = "", _refundable_deposit: float = 0.0):
        super().__init__(_name, _fee, _description)
        self._refundable_deposit = _refundable_deposit
        Equipment._equipments.append(self)

    def calculate_cost(self, days: int = 1) -> float:
        total = (self._fee * days) + self._refundable_deposit
        return float(total)

    @staticmethod
    def get_description(name: str) -> str:
        for equipment in Equipment._equipments:
            if equipment._name.lower() == name.lower():
                return f"Equipo: {equipment._name}. {equipment._description}"
        return f"No se encontró el equipo: {name}"

    @staticmethod
    def find_equipment(name: str) -> bool:
        return any(eq._name.lower() == name.lower() for eq in Equipment._equipments)

    @staticmethod
    def get_all_equipments() -> list:
        return list(Equipment._equipments)


