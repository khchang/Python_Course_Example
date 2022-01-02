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
 
 
token = "YskG1vGeWISsQdlYyOjyeRObmmBxUhSmU28MmJTDf0L"   # 個人
msg = "\n國立虎尾科技大學\n電機工程系\n系統控制研究室\nLine傳訊傳圖測試"
picURI = "photo_1.jpg"
 
lineNotify(token, msg, picURI)
