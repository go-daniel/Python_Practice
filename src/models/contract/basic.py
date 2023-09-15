from .contract import Contract
from ..customer import Customer

class Basic(Contract):
    def __init__(self, customer: Customer):
        self._call_fee = 1000
        self._internet_fee = 200
        super().__init__(customer)
    
    def phone_charge(self) -> float:
        return self.call_time * self.call_fee
    
    def internet_charge(self) -> float:
        return self.data_used * self.internet_fee
        
        