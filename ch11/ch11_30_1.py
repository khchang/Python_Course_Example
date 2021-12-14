# ch11_30_1.py
def printmsg():
    msg = "Java"        # 嘗試更改全域變數造成建立一個區域變數
    print("副程式更改後: ", msg)

msg = "Python"
printmsg()              # 在函數內要修改全域變數，結果新增了一個區域變數。
print("主程式更改後: ", msg)



   
