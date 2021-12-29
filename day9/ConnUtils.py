import  pymysql


def select(sql,pram=None,type="all",size=""):
    conn = pymysql.connect(host="localhost", user="root", password="", database="icbc")
    cur=conn.cursor(pymysql.cursors.DictCursor)#创建一个控制台
    if pram==None:
        cur.execute(sql)
    else:
        cur.execute(sql,pram)
    if type == "all":
        return cur.fetchall()
    elif type == "one":
        return cur.fetchone()
    elif type == 'many':
        return cur.fetchmany(size)
    cur.close()
    conn.close()

def  inserinto(sql,date):
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="icbc")
        cur=conn.cursor()#控制台
        insert=cur.execute(sql,date)#传入sql语句 ，数据
        conn.commit()#插入或者更新或者是删除#提交上数据
        cur.close()
        conn.close()
        print("受影响的行数为", insert)
    except Exception as re:
        print("执行错误",re)










