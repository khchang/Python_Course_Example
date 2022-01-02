"""
Reference:
1. https://ithelp.ithome.com.tw/articles/10276740?sc=iThelpR
2. pip install requests
"""
import requests

def line_notify():

    # token = "E7AoXInAnnnKpHPWGZDRt3g6hilNJfETg6y7kQNSdix" # 聊天室
    token = "YskG1vGeWISsQdlYyOjyeRObmmBxUhSmU28MmJTDf0L"   # 個人
    message = "Hello World! \n這是測試文字!"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)

if __name__ == '__main__':
    line_notify()