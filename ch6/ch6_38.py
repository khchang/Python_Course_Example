# ch6_38.py
mysports = ['籃球', '棒球']
friendsports = mysports[:]	# 淺拷貝(shallow copy)
print("列出mysports位址     = ", hex(id(mysports)))
print("列出friendsports位址 = ", hex(id(friendsports)))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('足球')
friendsports.append('游泳')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", hex(id(mysports)))
print("列出friendsports位址 = ", hex(id(friendsports)))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)
                   
