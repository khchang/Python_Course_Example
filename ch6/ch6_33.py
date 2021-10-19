# ch6_33.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.extend(cars2)			# 將串列cars2分解成元素後，再加入cars1中
print("執行extend()後串列cars1內容 = ", cars1)
print("執行extend()後串列cars2內容 = ", cars2)


