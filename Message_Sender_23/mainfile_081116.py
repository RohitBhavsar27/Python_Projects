import requests
import json


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params ={
        'authorization': 'WZECAcuioK6Tw5Xplb7n2shH0BRjqktGrFSYyeMIN38VazvDOJ7x96lNb8p5QFB4GrLRTuMDtknza1Ci',
        'sender_id': "FSTSMS",
        'message':message,
        'language': 'english',
        'route' : 'q',
        'numbers': number
        }
    response=requests.get(url, params=params)
    dict = response.json()
    print(dict)


send_sms("7499647738", "Trial msg")