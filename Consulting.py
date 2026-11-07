from Service import Service

class Consulting(Service):
    
    def __init__(self, _name: str, _fee: float, _description: str = ""):
        super().__init__(_name, _fee, _description)

    def calculate_cost(self, hiring_model: str, in_site: bool = None) -> float:
        total = self._fee
        if in_site:
            total += 150000 
        return float(total)

    @staticmethod
    def get_description(name: str) -> str:
        return f"Consultoría: {name}"
    
    @staticmethod
    def find_equipment(name: str) -> bool:
        return True

    @staticmethod
    def get_all_consulting() -> list:
        return []
