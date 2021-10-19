# ch6_24.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("列印使用[::-1]顛倒排序\n", cars[::-1])		# 直接列印cars[::-1]顛倒排序,不更改串列內容
print('========== 我是分隔線 ==========')
# 更改串列內容
print("使用reverse()顛倒排序串列元素")
cars.reverse()            						   # 顛倒排序串列，串列內容會一併更改
print("新的串列內容 = ",cars)

    
