from .contract import Contract
from ..customer import Customer

class DataFree(Contract):
    def __init__(self, customer: Customer, free_data: float, subcription_fee: float):
        self._call_fee = 1000
        self._internet_fee = 200
        self.__free_data = free_data
        self.__subcription_fee = subcription_fee
        super().__init__(customer)
    
    def phone_charge(self) -> float:
        return self.call_time * self.call_fee
    
    def internet_charge(self) -> float:
        fee = self.__subcription_fee
        if self.data_used > self.__free_data:
            fee += self._internet_fee * (self.data_used - self.__free_data)
        return fee
    
    
    
    
    