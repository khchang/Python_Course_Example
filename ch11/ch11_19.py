# ch11_19.py
"""
若傳遞的是一般變數，則只是將變數的值傳給函數，若此變數在函數內的值被修改，
也不會影響到主程式的變數值，相當於C語言中【傳值】的概念。
"""
def mydata(n):
    print("副程式 id(n) = : ", hex(id(n)), "\t", "n = ", n)
    n = 5
    print("副程式 id(n) = : ", hex(id(n)), "\t", "n = ", n)

x = 1
print("主程式 id(x) = : ", hex(id(x)), "\t", "x = ", x)
mydata(x)
print("主程式 id(x) = : ", hex(id(x)), "\t", "x = ", x)








