class Address:
    __country=""
    __province=""
    __street=""
    __door=""

    def __init__(self,country,province,street,door):
        self.__country=country
        self.__province=province
        self.__street=street
        self.__door=door


    def getCountry(self):
        return self.__country
    def getProvince(self):
        return self.__province
    def getStreet(self):
        return self.__street
    def getDoor(self):
        return self.__door
