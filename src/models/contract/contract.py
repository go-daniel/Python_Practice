from ..customer import Customer
from abc import ABC, abstractmethod

class Contract(ABC):
    VAT = 10000
    
    def __init__(self, customer: Customer) -> None:
        self._customer = customer
        
    
    @abstractmethod
    def phone_charge(self) -> float:
        pass
    
    @abstractmethod
    def internet_charge(self) -> float:
        pass
    
    def totalCharge(self) -> float:
        total = self.phone_charge() + self.internet_charge()
        if total > 0: 
            return total + 0.1 * self.VAT 
        else: 
            return 0
    
    def get_call_fee(self) -> float:
        return self._call_fee
    
    def get_internet_fee(self) -> float:
        return self._internet_fee
    
    def get_customer(self) -> Customer:
        return self._customer
    
        
    def get_call_time(self) -> str:
        return self._call_time

    def get_data_used(self) -> str:
        return self._data_used  
    
    def set_call_time(self, time: float):
        self._call_time = time
 
    def set_data_used(self, amount: float):
        self._data_used = amount
            
    