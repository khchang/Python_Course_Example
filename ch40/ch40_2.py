import requests, os
 
"""
發送 Line Notify 訊息與圖片
"""
token = "YskG1vGeWISsQdlYyOjyeRObmmBxUhSmU28MmJTDf0L"   # 個人
































def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    r = requests.post(url, headers = headers, params = payload, files = files)
    return r.status_code
 


# msg = "\n國立虎尾科技大學\n電機工程系\n系統控制研究室\nLine傳訊傳圖測試"
msg = "\nHello World! NFU"
picURI = "D:\\Course_Region\\Python_Course_Example\\ch40\\photo_1.jpg"
 
lineNotify(token, msg, picURI)










