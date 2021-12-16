names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
sala=0
for i in names:
    sala+=i[5]
print("平均薪资为:",sala/4)

# 平均年龄
age=0
for i in names:
    age+=int(i[1])
print("平均年龄为:",age/4)

# 添加新员工刘备
emp_liu=["刘备","45","男","220","alibaba",500,"30"]
names.append(emp_liu)
print(names)
# 4.统计公司男女人数
male,female=0,0
for i in names:
    if i[2]=="男":
        male+=1
    else:
        female+=1
print("男：",male,"女：",female)

# 5.每个部门的人数

print(105/10)

a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            space=a[j]
            a[j]=a[j+1]
            a[j+1]=space
print(a)