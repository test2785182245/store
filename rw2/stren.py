# 双色球
import random
t=int(input("机选几注："))

def ran():
    list1=[]
    for i in range(6):
        list1.append(random.randint(1,34))
    list1.sort()
    return list1

while t>0:
    list_hong=ran()
    for i in list_hong:
        print("{0:0>2}".format(i),end=" ")
    print("| {0:0>2}".format(random.randint(1,16)))

    t-=1
# {0:0>2}.formate()    冒号后边的0是填充符，>是对齐符号 2是字符宽度
