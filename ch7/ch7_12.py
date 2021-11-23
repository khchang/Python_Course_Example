# ch7_12.py
n = int(input("請輸入n值: "))   # input輸入為字串，須轉換為int
sum = 0

for num in range(1, n+1):
    print(f"{num = }")
    sum = sum + num

print("總和 =", sum)



    


