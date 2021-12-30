import ConnUtils
import time


def add_account():
    type=input("请输入类别：")
    account = input("请输入账户：")
    money = input("请输入金额：")
    time = input("请输入时间：")
    intr = input("请输入说明：")

    sql = "insert into bella values(0,%s,%s,%s,%s,%s)"
    date=[type,account,money,time,intr]
    ConnUtils.inserinto(sql,date)
    print("账务添加成功！")

def edit_account():
    ID = input("请输入ID:")
    type=input("请输入新类别：")
    account = input("请输入新账户：")
    money = input("请输入新金额：")
    time = input("请输入新时间：")
    intr = input("请输入新说明：")

    sql="update bella set 类别=%s,账户=%s,金额=%s,时间=%s,说明=%s where ID=%s"
    date = [type, account, money, time, intr,ID]
    ConnUtils.inserinto(sql,date)
    print("编辑账务成功！")

def delete_account():
    ID = input("请输入要删除的ID:")
    sql="delete from bella where ID =%s"
    date=[ID,]
    ConnUtils.inserinto(sql,date)
    print("删除成功!")

def check_account():
    o=input("请选择查询类型：1.查询所有\t2.按条件查询")
    if o=="1":
        sql="select * from bella"
        result=ConnUtils.select(sql)
        print('ID\t\t\t类别\t\t\t账户\t\t\t金额\t\t\t时间\t\t\t\t\t说明')
        for i in result:
            for k in i:
                print("{0:-<8}".format(i[k]),end="\t")
            print()
    elif o=="2":
        sql="select * from bella where 时间>%s and 时间<%s"
        date=[input("请输入起始时间"),input("请输入结束时间")]

        result=ConnUtils.select(sql,date)
        print('ID\t\t\t类别\t\t\t账户\t\t\t金额\t\t\t时间\t\t\t\t\t说明')
        for i in result:
            for k in i:
                print("{0:-<8}".format(i[k]),end="\t")
            print()

def run():
    while True:
        print("-----------------------家庭记账软件-----------------------")
        print("1.添加账务\t2.编辑账务\t3.删除账务\t4.查询账务\t5.退出系统")
        o = int(input("请输入功能序号[1-5]"))
        if o == 1:
            add_account()
        elif o == 2:
            edit_account()
        elif o == 3:
            delete_account()
        elif o == 4:
            check_account()
        elif o == 5:
            print("退出系统")
            break
if __name__ == '__main__':
    run()