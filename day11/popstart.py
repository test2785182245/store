from Address import Address
from Bank import Bank
from User import User
from interface import Interface

bank = Bank()
sc = Interface()
while True:
    choose = sc.show_main()
    if choose == 1:
        list_add = sc.show_add()
        jack_address = Address(country=list_add[2], province=list_add[3], street=list_add[4], door=list_add[5])
        jack = User(1, list_add[0], list_add[1], jack_address)
        result = bank.newAccount(jack)
        if result == 1:
            print("开户成功！")
        elif result == 2:
            print("您已开户，如需开新户请退出系统重新开户")
        elif result == 3:
            print("数据库已满")
        print(bank.allUser)
    elif choose == 2:
        list_save = sc.show_save()
        result = bank.saveMoney(list_save[0], list_save[1])
        if result:
            print("ok")
        else:
            print("账户不存在")
    elif choose == 3:
        list_take = sc.show_take()
        result = bank.takeMoney(list_take[0], list_take[1], list_take[2])
        if result == 1:
            print("ok")
        elif result == 2:
            print("余额不足")
        else:
            print("密码错误")
    elif choose == 4:
        list_turn = sc.show_turn()
        result = bank.turnMoney(list_turn[0], list_turn[1], list_turn[2], list_turn[3])
        if result == 1:
            print("ok")
        elif result == 2:
            print("密码错误")
        else:
            print("账户不存在")
    elif choose == 5:
        li = sc.show_all()
        mate = bank.selectAll(li[0], li[1])
        print(mate)
    elif choose == 6:
        print("退出系统！")
        break
