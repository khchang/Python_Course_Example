# ch11_16.py
def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member1 = build_vip('101', 'Nelson')
member2 = build_vip('102', 'kh')

print(member1)
print(member2)

