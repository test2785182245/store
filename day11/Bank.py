class Bank:
    allUser=[{'账号': 236632, '账户类型': 1, '姓名': '1', '密码': '1', '余额': 0, '银行名称': '中国农业银行'}]
    def is_exit(self,key,value):
        for i in range(len(self.allUser)):
            if value==self.allUser[i][key]:
                return i

    def getMessage(self,index,colName):
        return self.allUser[index][colName]
    def newAccount(self,user):
        if None==self.is_exit("账号",user.getAccountNumber()):
            if len(self.allUser)<99:
                dict_user={"账号":user.getAccountNumber(),
                           "账户类型":user.getAccountType(),
                           "姓名":user.getClientName(),
                           "密码":user.getPassword(),
                           "余额":user.getMoney(),
                           "银行名称":user.getBankName()
                           }
                self.allUser.append(dict_user)
                return 1
            else:
                return 3
        else:
            return 2

    def saveMoney(self,account,money):
        index=self.is_exit("账号",account)
        if index==None:
            return False
        else:
            self.allUser[index]["余额"] += money
            return True

    def takeMoney(self,account,password,money):
        index = self.is_exit("账号", account)
        if self.allUser[index]["密码"]==password:
            if self.allUser[index]['余额']>=money:
                self.allUser[index]['余额']-=money
                return  1
            else:
                return 2
        else:
            return 3

    def turnMoney(self,nameIn,nameOut,password,money):
        index_in = self.is_exit("账号",nameIn)
        index_out = self.is_exit("账号", nameOut)

        if index_in!=None and index_out!=None:
            if password==self.getMessage(index_in,"密码"):
                self.allUser[index_in]["余额"]-=money
                self.allUser[index_out]["余额"]+=money
                return 1
            else:return 2
        else:return 3

    def selectAll(self,account,password):
        index = self.is_exit("账号", account)
        if self.allUser[index]["密码"] == password:
            return self.allUser[index]