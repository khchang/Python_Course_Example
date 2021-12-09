# ch11_14.py
def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('明', '小', '張', 'M')
info2 = guest_info('花', '小', '林', 'F')
print(info1)
print(info2)



