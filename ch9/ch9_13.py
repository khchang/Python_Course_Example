# ch9_13.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
key = input("請輸入鍵(key) = ")
value = input("請輸入值(value) = ")
if key in fruits:
    print(f"{key}已經在字典了")
else:
    fruits[key] = value
    print("新的fruits字典內容 = ", fruits)


