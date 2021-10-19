# ch6_29.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)	# count()方法可以傳回特定搜尋元素內容在串列中出現的次數。
print(f"所搜尋元素 {search_str} 出現 {num1} 次")
print('========== 我是分隔線 ==========')
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print(f"所搜尋元素 {search_val} 出現 {num2} 次")

