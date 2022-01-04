import random
ac=random.randint(100000,999999)
class User:

    __accountNumber=ac
    __accountType =1
    __clientName=""    # 客户姓名
    __password=""
    __address=""
    __money=0
    __bankName="中国农业银行"

    def __init__(self,accountType,clienttName,password,address):
        self.__accountType=accountType
        self.__clientName=clienttName
        self.__password=password
        self.__accountType=accountType
        self.__address=address

    def getAccountNumber(self):
        return self.__accountNumber
    def getAccountType(self):
        return self.__accountType
    def getPassword(self):
        return self.__password
    def getAddress(self):
        return self.__address
    def getClientName(self):
        return self.__clientName
    def getMoney(self):
        return self.__money
    def getBankName(self):
        return self.__bankName
