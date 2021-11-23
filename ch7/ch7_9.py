# ch7_9.py
fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print("目前fruits串列 : ", fruits)

for fruit in fruits[:]:         # 要使用淺拷貝，fruit才能一直是在索引0的內容值。
    fruits.remove(fruit)
    print(f"刪除 {fruit} ")
    print("目前fruits串列 : ", fruits)

