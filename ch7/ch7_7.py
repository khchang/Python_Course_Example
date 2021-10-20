# ch7_7.py
files = ['da1.c','da2.py','da3.py','da4.java']
py = []                         # 建立一個空串列

for file in files:
    if file.endswith('.py'):    # 判斷結尾字串是否為".py"
        py.append(file)         # 如果結尾字串是".py"，則加入py串列
print(py)








