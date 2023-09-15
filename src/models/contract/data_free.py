from .contract import Contract
from ..customer import Customer

class DataFree(Contract):
    def __init__(self, customer: Customer, free_data: float, subcription_fee: float):
        self._call_fee = 1000
        self.__internet_fee = 200
        self.__free_data = free_data
        self.__subcription_fee = subcription_fee
        super().__init__(customer)
    
    def phone_charge(self) -> float:
        return self.get_call_time() * self.get_call_fee()
    
    def internet_charge(self) -> float:
        fee = self.__subcription_fee
        if (self.get_data_used() > self.__free_data):
            fee = fee + self.__internet_fee * self._customer.get_data_used()
        return fee
    
    
    
    
    