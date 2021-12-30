import pymysql
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a,%d %b %Y %H:%M:%S',
    filename='test.log',
    filemode='w'
)
# 数据库名 accounts 表名bella
def select(sql,pram=None,type="all",size=""):
    conn = pymysql.connect(host="localhost", user="root", password="", database="accounts")
    cur=conn.cursor(pymysql.cursors.DictCursor)#创建一个控制台
    if pram==None:
        cur.execute(sql)
    else:
        cur.execute(sql,pram)
    if type == "all":
        logging.info("查询")
        return cur.fetchall()

    elif type == "one":
        logging.info("查询")
        return cur.fetchone()
    elif type == 'many':
        logging.info("查询")
        return cur.fetchmany(size)
    cur.close()
    conn.close()


def  inserinto(sql,date):
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="accounts")
        cur=conn.cursor()#控制台
        insert=cur.execute(sql,date)#传入sql语句 ，数据
        conn.commit()#插入或者更新或者是删除#提交上数据
        cur.close()
        conn.close()
        print("添加账务的ID为",cur.lastrowid)
        logging.info("info message:执行成功,修改ID为:{0}".format(cur.lastrowid))
    except Exception as re:
        logging.debug("debug message:执行失败{0}".format(re))
        print("执行错误",re)