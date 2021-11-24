# ch12_11_1.py
# 父類別與子類別若有相同屬性名稱，則在子類別中會優先使用自己的屬性名稱。

class Person():
    def __init__(self,name):
        self.name = name

class LawerPerson(Person):
    def __init__(self,name):
        self.name = name + "律師"

hung = Person("nfu")
lawer = LawerPerson("kh")
print(hung.name)
print(lawer.name)
















