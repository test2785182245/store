class Interface:

    def show_main(self):
        print("=====================")
        print(" 1、开户")
        print(" 2、存钱")
        print(" 3、取钱")
        print(" 4、转账")
        print(" 5、查询账户功能")
        print("6.退出！")
        print("=====================")
        return int(input("请选择一个业务"))

    def show_add(self):
        username = int(input("请输入您的账户"))
        password = input("请输入六位数字密码")
        country = input("\t\t请输入您的国家")
        province = input("\t\t请输入您的省份")
        street = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门派号")
        return [username,password,country,province,street,door]
    def show_save(self):
        username = int(input("请输入您的账户"))
        num = int(input("请输入存入金额："))
        return [username,num]
    def show_take(self):
        username = int(input("请输入您的账户"))
        password = input("请输入密码")
        num = int(input("请输入取出金额："))
        return [username,password,num]
    def show_turn(self):
        username = int(input("请输入您的账户"))
        user2 = int(input("请输入要转入的账户"))
        password = input("请输入您的密码")
        take_num = int(input("请输入转出金额："))
        return [username,user2,password,take_num]
    def show_all(self):
        username = int(input("请输入您的账户"))
        password = input("请输入密码")
        return [username,password]