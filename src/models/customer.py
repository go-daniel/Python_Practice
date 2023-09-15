class Customer:
    
    def __init__(self, name: str, idNo: str, address: str) -> None:
        self.__name = name
        self.__idNo = idNo
        self.__address = address
        
    def __str__(self) -> str:
        return 'Name: %s, IDNO: %s, Address: %s' % (self.__name, self.__idNo, self.__address)
    
    def get_name(self) -> str:
        return self.__name
    
    def get_idNo(self) -> str:
        return self.__idNo
    
    def get_address(self) -> str:
        return self.__address

    def set_name(self, name: str) -> None:
        self.__name = name
    
    def set_idNo(self, idNo: str) -> None:
        self.__idNo = idNo
    
    def set_address(self, address: str) -> None:
        self.__address = address
    
    
    
    
         