class Service:
    def __init__(self,_name: str,_fee:float,_description:str):
        self.name = _name
        self.fee = _fee
        self.description = _description

    def calculate_cost(self, fee: float) -> float:
        return self.fee * fee

    @staticmethod
    def get_description(_name: str) -> str:
        return f"Description del servicio: {_name}"
