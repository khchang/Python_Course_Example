import requests, os
 
"""
發送 Line Notify 訊息與圖片
"""
def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    r = requests.post(url, headers = headers, params = payload, files = files)
    return r.status_code
 
 
token = "sGEixOukPN5Iw5Nsr24ZU2naOFQFbuJThKVIW4qTUAf"   # 個人
msg = "Hello World!\nLine Notify 傳圖測試"
picURI = "Naruto.png"
 
lineNotify(token, msg, picURI)
