import ConnUtils
import time

bank_name="工商银行"
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入六位数字密码")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")


#   函数传值  位置对应 不是名称对应      有几个传几个
    ssr=bankadd()
    if ssr==1:
        try:
            sql = "insert into t_user values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            date = [username, password, country, province, street, door, 0, "中国工商银行", time.strftime("%Y-%m-%d:%H.%M.%S")]
            ConnUtils.inserinto(sql, date)
        except Exception as e:
            print("错误，请检查SQL",e)

        print("添加用户成功，以下是您的详细信息")

        sql = "SELECT account FROM t_user ORDER BY account DESC LIMIT 1 ;"
        account=ConnUtils.select(sql)
        info='''
            --------开户信息------
                账号:%s
                用户名:%s
                密码:******
                国家:%s
                省份:%s
                街道:%s
                门牌号:%s
                金额:%s
                开户行:%s
        '''
        print( info %(account,username,country,province,street,door,0,bank_name))

    elif ssr ==3:
        print("数据库已满")


def bankadd():
    sql="select count(*) from t_user"
    result=ConnUtils.select(sql,type="one")
    print(result['count(*)'])
    if result['count(*)']>100:
        return 3
    else:
        return 1


def savemoney():
    account=input("请输入您的账户")
    num=int(input("请输入存入金额："))

    result=save(account)
    if result:
        sql="UPDATE  t_user SET money = money+%s  WHERE account=%s;"
        date = [num,account]
        ConnUtils.inserinto(sql,date)
        print("ok")
    else:
        print("请输入正确的账户")

def save(account):
    sql="select count(*) from t_user where account=%s"
    result=ConnUtils.select(sql,account,type="one")
    if result['count(*)']>0:
        return True
    else:
        return False

def take_money():
    username = input("请输入您的用户名")

    password = input("请输入您的密码")

    take_num=int(input("请输入取出金额："))

    result=take(username,password,take_num)
    if result==1:
        print("请检查输入")
    elif result==2:
        print("ok")

def take(account,password,num):
    sql="select count(*) from t_user where account=%s and password=%s and money>%s"
    date=[account,password,num]
    result=ConnUtils.select(sql,date,type="one")
    if result['count(*)']>0:
            sql="update t_user set money=money-%s where account=%s"
            date=[num,account]
            ConnUtils.inserinto(sql,date)
            return 2
    else:
        return 1


def turn_money():
    username = input("请输入您的用户名")
    user2=input("请输入要转入的用户名")
    password = input("请输入您的密码")

    take_num=int(input("请输入转出金额："))

    result=turn(username,user2,password,take_num)
    if result==1:
        print("请检查输入")
    elif result==2:
        print("转账成功")

def turn(name,name2,password,num):
    sql="SELECT COUNT(username) FROM t_user WHERE account=%s AND PASSWORD =%s AND money>%s OR account=%s;"
    date=[name,password,num,name2]
    result=ConnUtils.select(sql,date)
    if result[0]['COUNT(username)']==2:
        sql1="UPDATE t_user SET money=money-%s WHERE account=%s;"
        sql2="UPDATE t_user SET money=money+%s WHERE account=%s;"
        ConnUtils.inserinto(sql1,[num,name])
        ConnUtils.inserinto(sql2, [num, name2])
        return 2
    else:
        return 1

def check_account():
    username = input("请输入您的用户名")

    password = input("请输入您的密码")
    check(username,password)
def check(username,password):
    info = '''
                --------账户信息------
                    账号:%s
                    用户名:%s
                    用户居住地址:%s%s%s%s
                    账号余额:%s
                    当前账户开户行:%s
            '''
    sql="select count(*) from t_user where account=%s and password=%s"
    result=ConnUtils.select(sql,[username,password])

    if (result[0]['count(*)']) >0:
        sql = "select *  from t_user  where account=%s"
        result = ConnUtils.select(sql,[username])
        mate=result[0]
        print( info %(mate['account'],username,mate['country'],mate['provice'],mate['street'],mate['door'],mate["money"],bank_name))

while True:
    print("=====================")
    print(" 1、开户")
    print(" 2、存钱")
    print(" 3、取钱")
    print(" 4、转账")
    print(" 5、查询账户功能")
    print( "6.退出！")
    print("=====================")
    o=input("请选择一个业务")
    if o =="1":
        print("开户")
        useradd()
    elif o=="2":
        savemoney()
    elif o=="3":
        take_money()
    elif o=="4":
        turn_money()
    elif o=="5":
        check_account()
    elif o=="6":
        print("退出系统！")
        break

