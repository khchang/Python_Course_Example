# ch6_18.py
string = input("請輸入名字 : ")
print("/%s/" % string)
print(f'/{string}/')				# 用f-string表達上式
print('========== 我是分隔線 ==========')
string = input("請輸入名字 : ")
print("/%s/" % string.strip())
print(f'/{string.strip()}/')		# 用f-string表達上式
