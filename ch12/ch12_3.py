# ch12_3.py
# 設計一個類別，內含查詢餘額的方法。

class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'                # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def get_balance(self):                  # 獲得存款餘額
        return self.balance

hungbank = Banks('hung', 100)               # 定義物件hungbank
                                            # 將'hung'傳給uname
                                            # 將100傳給money

print(hungbank.name.title(), " 存款餘額是 ", hungbank.get_balance())





