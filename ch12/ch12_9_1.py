# ch12_9_1.py
# Son繼承Father，可以使用Father的公有屬性與方法。

class Father():
    def hometown(self):
        print('我住在雲林')

class Son(Father):
    pass

hung = Father()
ivan = Son()
hung.hometown()
ivan.hometown()





