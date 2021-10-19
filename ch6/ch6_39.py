# ch6_39.py
string = "Python"
# 正值索引
print(" string[0] = ", string[0],
      "\n string[1] = ", string[1],
      "\n string[2] = ", string[2],
      "\n string[3] = ", string[3],
      "\n string[4] = ", string[4],
      "\n string[5] = ", string[5])
print("========== 我是分隔線 ==========")
# 負值索引
print(" string[-1] = ", string[-1],       # 倒數第1個索引的元素值
      "\n string[-2] = ", string[-2],     # 倒數第2個索引的元素值
      "\n string[-3] = ", string[-3],     # 倒數第3個索引的元素值
      "\n string[-4] = ", string[-4],     # 倒數第4個索引的元素值
      "\n string[-5] = ", string[-5],     # 倒數第5個索引的元素值
      "\n string[-6] = ", string[-6])     # 倒數第6個索引的元素值
print("========== 我是分隔線 ==========")      
# 多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ",s1,s2,s3,s4,s5,s6)

"""
字串可以當作是一個序列，這個序列是由字元(character)所組成，可想像成字元的序列，但字串內的單一元素內容不可更改。
"""


