# ch6_27.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print(f"所搜尋元素 {search_str} 第一次出現位置索引是 {i}")
print('========== 我是分隔線 ==========')
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print(f"所搜尋元素 {search_val} 第一次出現位置索引是 {j}")

# 若搜尋值沒有在串列內，會出現錯誤。
