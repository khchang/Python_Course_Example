# ch7_8.py
names = ['張三','李四','張五','林六']
lastname = []
for name in names:
    if name.startswith('張'):    # 判斷起始字串是否為"張"
        lastname.append(name)    # 如果起始字串是"張"，則加入lastname串列
print(lastname)








