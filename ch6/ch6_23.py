# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("使用remove()刪除串列元素")
expensive = 'bmw'					# remove()方法可以刪除串列內指定內容的元素。
cars.remove(expensive)				# 刪除第一次出現的元素bmw
print("所刪除的內容是: 因為 " + expensive.upper() + " 太貴了" )		# upper()：改全部大寫
print("新的串列內容",cars)

    
