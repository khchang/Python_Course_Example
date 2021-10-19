# ch6_45.py
password = 'National Formosa University'

ch = input("請輸入字元 = ")
print("in運算式")
if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")

print("========== 我是分隔線 ==========")

print("not in運算式")
if ch not in password:
    print("輸入字元不在密碼中")
else:
    print("輸入字元在密碼中")
        
