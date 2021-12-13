import xlrd

def excel(co):
    wb = xlrd.open_workbook('12月.xls')
    sheet = wb.sheet_by_name("12月份各种服饰销售情况")
    dat=[]
    for i in range(1,sheet.nrows):
        cells = sheet.row_values(i,start_colx=co)
        date =(cells[0])
        dat.append(date)
    return dat
def rate(number):
    sum = 0
    for i in range(len(goods_list)-1):
        if goods_list[i] == good_list[number]:
            sum += num_list[i]
    return round(sum/1844*100,1)
price_list = excel(2)
num_list=excel(4)
goods_list=excel(1)

sum=0
for i in range(len(price_list)):
    sum+=price_list[i]*num_list[i]
print("1.销售总额为{0}".format(round(sum,2)))

num_sum=0
for i in num_list:
    num_sum+=i
print("2.平均每日销售数量为{0}".format(num_sum))

good_list = []
for i in goods_list:
    if i not in good_list:
        good_list.append(i)
print(good_list)

print("3.",end="")
for i in range(len(good_list)):
    print("{0}的销售量占比为{1}%".format(good_list[i],rate(i)))