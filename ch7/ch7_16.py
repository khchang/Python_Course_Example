# ch7_16.py
# 新串列 = [運算式 for 項目 in 可迭代物件]

n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 限制輸入最大值是10
squares = [num ** 2 for num in range(1, n+1)]	# num =  1, 2, 3, ... n，將num ** 2的元素值放入squares
print(squares)

