# ch7_36.py
x = 1000001
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i % 100000 == 0:      # 隔100000執行一次
        print(f"當 i = {i:7d} 時 PI = {pi:20.19f}")


  













          

