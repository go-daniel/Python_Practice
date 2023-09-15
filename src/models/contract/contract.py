from ..customer import Customer
from abc import ABC, abstractmethod

class Contract(ABC):
    
    def __init__(self, customer: Customer, name: str = 'Contract') -> None:
        self.name = name
        self._customer = customer
        
    
    @abstractmethod
    def phone_charge(self) -> float:
        pass
    
    @abstractmethod
    def internet_charge(self) -> float:
        pass
    
    def total_charge(self) -> float:
        total = self.phone_charge() + self.internet_charge()
        if total > 0: 
            return total + 0.1 * total
        else: 
            return 0
    
    @property
    def call_fee(self) -> float:
        return self._call_fee
    
    @property
    def internet_fee(self) -> float:
        return self._internet_fee
    
    @property
    def customer(self) -> Customer:
        return self._customer
    
    @property  
    def call_time(self) -> str:
        return self._call_time

    @property
    def data_used(self) -> str:
        return self._data_used  
    
    @property
    def customer(self) -> Customer:
        return self._customer
    
    @call_time.setter
    def call_time(self, time: float):
        self._call_time = time
        
    @data_used.setter
    def data_used(self, amount: float):
        self._data_used = amount
    
    def __str__(self) -> str:
        return self.name 
    