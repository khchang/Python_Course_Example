# ch6_21.py
cars = ['Honda','Toyota','Ford']     
print("目前串列內容 = ",cars)
print('========== 我是分隔線 ==========')
print("在索引1位置插入Nissan")
cars.insert(1,'Nissan')			# insert()方法可在串列的任意位置新增元素
print("新的串列內容 = ",cars)
print('========== 我是分隔線 ==========')
print("在索引0位置插入BMW")
cars.insert(0,'BMW')
print("最新串列內容 = ",cars)

    
