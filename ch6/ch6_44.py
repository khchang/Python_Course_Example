# ch6_44.py
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print("字串開頭是CIA: ", msg.startswith("CIA"))	# startswith(): 可以列出字串的起始文字是否為特定子字串。
print("字串結尾是CIA: ", msg.endswith("CIA"))	# endswith(): 可以列出字串的結尾文字是否為特定子字串。
print("CIA出現的次數: ",msg.count("CIA"))		# count(): 計算"CIA"在msg出現的次數。
msg = msg.replace('Linda','Lxx')				# 將msg中的"Linda"取代為Lxx
print("新的msg內容 : ", msg)

