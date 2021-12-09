# ch11_19_1.py
def mydata(n):
    print("函  數 id(n) = : ", hex(id(n)), "\t", "n = ", n)
    n[0] = 5
    print("函  數 id(n) = : ", hex(id(n)), "\t", "n = ", n)

x = [1, 2]
print("主程式 id(x) = : ", hex(id(x)), "\t", "x = ", x)
mydata(x)
print("主程式 id(x) = : ", hex(id(x)), "\t", "x = ", x)








