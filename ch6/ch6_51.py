# ch6_51.py
drinks = ["coffee", "tea", "wine"]
enum_drinks = enumerate(drinks)                # 數值初始是0
print("轉成串列輸出, 初始索引值是 0 = ", list(enum_drinks))

enum_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成串列輸出, 初始索引值是10 = ", list(enum_drinks))
