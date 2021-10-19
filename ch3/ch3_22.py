# ch3_22.py
str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
print("========== 我是分隔線 ==========")
str2 = r"Hello!\nPython"	# 在字串前加r，表示在該字串內若存在逸出字元，則不轉譯。
print("含r字元的輸出")
print(str2)

