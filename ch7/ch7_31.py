# ch7_31.py
# enumerate是由索引值與元素值配對呈現。

drinks = ["咖啡", "茶", "酒"]
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")
print()

# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)










          


