# ch11_29.py
def defmsg():
    msg = 'pringmsg variable'

def printmsg():
    print(msg)      # 列印defmsg( )函數定義的區域變數
                    # 區域變數內容無法在其他函數引用

printmsg()         # 呼叫printmsg( )



