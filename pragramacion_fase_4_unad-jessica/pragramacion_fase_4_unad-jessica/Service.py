class Service:
    def __init__(self, _name: str, _fee: float, _description: str = ""):
        self._name = _name
        self._fee = _fee
        self._description = _description

    def calculate_cost(self, *args, **kwargs) -> float:
        return float(self._fee)

    def get_description(self, name: str = None) -> str:
        return self._description

