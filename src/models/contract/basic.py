from .contract import Contract
from ..customer import Customer

class Basic(Contract):
    def __init__(self, customer: Customer):
        self._call_fee = 1000
        self._internet_fee = 200
        super().__init__(customer)
    
    def phone_charge(self) -> float:
        return self.get_call_time() * self.get_call_fee()
    
    def internet_charge(self) -> float:
        return self.get_data_used() * self.get_internet_fee()
        
        