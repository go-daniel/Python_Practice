class Customer:
    
    def __init__(self, name: str, idNo: str, address: str) -> None:
        self.__name = name
        self.__idNo = idNo
        self.__address = address
        
    def __str__(self) -> str:
        return 'Name: %s, IDNO: %s, Address: %s' % (self.__name, self.__idNo, self.__address)
    
    @property
    def name(self) -> str:
        return self.__name
    @property
    def idNo(self) -> str:
        return self.__idNo
    @property
    def address(self) -> str:
        return self.__address
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    @idNo.setter
    def idNo(self, idNo: str) -> None:
        self.__idNo = idNo
    @address.setter
    def address(self, address: str) -> None:
        self.__address = address
    
    
    
    
         