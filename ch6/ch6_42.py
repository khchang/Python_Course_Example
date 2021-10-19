# ch6_42.py
str1 = "National Formosa University"
str2 = "D:\Python\ch6"

sList1 = str1.split()                       # 將字串以空格為分隔符號轉成串列
sList2 = str2.split("\\")                   # 將字串以"\"為分隔符號轉成串列
print(str1, " 串列內容是 ", sList1)         # 列印串列
print(str1, " 串列字數是 ", len(sList1))    # 列印字數
print(str2, " 串列內容是 ", sList2)         # 列印串列
print(str2, " 串列字數是 ", len(sList2))    # 列印字數

