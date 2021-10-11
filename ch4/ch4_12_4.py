# ch4_12_4.py
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
print('使用print()')
print(url + city + '&radius=' + str(r) + '&type=' + type)
print('使用print()+format{}')
print(url + "{}&radius={}&type={}".format(city, r, type))
