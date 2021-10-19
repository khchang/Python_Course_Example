# ch6_22.py
cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print('========== 我是分隔線 ==========')
print("使用pop()刪除串列元素")
popped_car = cars.pop()					# 刪除串列末端值 (pop方法內沒有指定要刪除的索引值，預設為串列末端元素)
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)
print('========== 我是分隔線 ==========')
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)				# 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)    
