# ch4_12_5.py
name = '張凱雄'
message1 = f"我是{name}"
print(message1)
message2 = f"我是{name=}"	# 在Python 3.8版後，f-strings內的變數名稱後加上'='，則可列出變數名稱與值，可方便除錯。
print(message2)

score = 95.5
message = f"我的成績是{score:6.2f}"
print(message)
