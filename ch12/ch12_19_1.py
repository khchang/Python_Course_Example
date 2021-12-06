# ch12_19_1.py
class A():
    def __init__(self):
        print('class A')

class B():
    def __init__(self):
        print('class B')

class C(A,B):
    def __init__(self):
        super().__init__()  # 使用super()繼承父類別的方法
                            # 但只有執行到class A的__init__()
        print('class C')

x = C()

