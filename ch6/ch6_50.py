# ch6_50.py
drinks = ["咖啡", "茶", "酒"]
enum_drinks = enumerate(drinks)        # 數值初始是0
print(enum_drinks)                     # 傳回enumerate物件所在記憶體
print("下列是輸出enumerate物件類型")
print(type(enum_drinks))               # 列出物件類型
print("下列是輸出enumerate物件內容")
print(list(enum_drinks))

