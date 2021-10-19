# ch6_49.py
mysports = ['籃球', '棒球']
sports1 = mysports          # 賦值
sports2 = mysports[:]       # 切片拷貝新串列
print("我喜歡的運動 = ", mysports, "位址是 = ", hex(id(mysports)))
print("運動 1       = ", sports1,  "位址是 = ", hex(id(sports1)))
print("運動 2       = ", sports2,  "位址是 = ", hex(id(sports2)))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", boolean_value)


