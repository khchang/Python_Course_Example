# ch12_14.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " 正在跑")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('我的寵物 ' + dog_name.title(), dog_age)

mycat = Animals('小白', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' 是 ', mycat.age, " 歲")
mycat.run()

mydog = Dogs('小黃', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' 是 ', mydog.age, " 歲")
mydog.run()
        
        
