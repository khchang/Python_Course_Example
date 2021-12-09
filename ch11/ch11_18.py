# ch11_18.py
def product_msg(customers):
    str1 = '敬愛的 '
    str2 = '本研究室將在2021年12月7日舉行產品發表會'
    str3 = 'kh敬上'
    for customer in customers:
        msg = str1 + customer + ':\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)


