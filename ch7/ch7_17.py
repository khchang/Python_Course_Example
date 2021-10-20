# ch7_17.py
# 新串列 = [運算式 for 項目 in 可迭代物件]

celsius = [21, 25, 29]
fahrenheit = [(x * 9 / 5 + 32) for x in celsius]
# x =  21, 25, 29，將(x * 9 / 5 + 32)的元素值放入fahrenheit

print(fahrenheit)

