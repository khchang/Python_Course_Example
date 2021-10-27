# ch4_13.py
fstream1 = open("D:\out1.txt", mode="w") # 取代先前資料
print("Testing for output", file=fstream1)
fstream1.close( )

fstream2 = open("D:\out2.txt", mode="a") # 附加資料後面
print("Testing for output", file=fstream2)
fstream2.close( )

