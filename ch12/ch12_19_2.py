# ch12_19_2.py
class A():
    def __init__(self):
        super().__init__()      # 在基底類別也使用super()
        print('class A')

class B():
    def __init__(self):
        super().__init__()      # 在基底類別也使用super()
        print('class B')

class C(A,B):
    def __init__(self):
        super().__init__()      # 使用super()繼承父類別的方法
                                # class A, class B, class C的__init__()都可以被執行。
        print('class C')

x = C()

