# ch7_18.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")    # <3d: 3位整數靠左
    print()                                         # 換行輸出
    

