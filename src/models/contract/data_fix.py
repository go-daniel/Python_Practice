from .contract import Contract
from ..customer import Customer

class DataFix(Contract):
    def __init__(self, customer: Customer):
        self._call_fee = 1000 * 0.9
        super().__init__(customer)
    
    def phone_charge(self) -> float:
        return self.call_time * self.call_fee
    
    def internet_charge(self) -> float:
        return 1_000_000
        