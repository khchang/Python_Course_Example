# ch2_4.py
a = b = c = 10
print('變數a的位址：', hex(id(a))) # id(x)回傳變數x的記憶體位址
print('變數b的位址：', hex(id(b))) # hex(x)將x轉成16進制
print('變數c的位址：', hex(id(c)))

x = a + b + c + 12
print('變數x的位址：', hex(id(x)))
print(x)

# 續行方法1
print('續行方法1')
y = a +\
    b +\
    c +\
    12
print(y)

# 續行方法2
print('續行方法2')
z = ( a +     # 此處可以加上註解  
      b +
      c +
      12 )
print(z)
