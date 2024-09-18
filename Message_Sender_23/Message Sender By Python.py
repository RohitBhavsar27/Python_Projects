#Creating mainfile
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror


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
    return dict.get('return')
    
def btn_click():
    num=textNumber.get()
    msg=textMsg.get("1.0" , END)
    r = send_sms(num, msg)
    if r== True:
        showinfo("Send Success, Succesfully Sent")
    else:
        showerror("Error, Something went wrong...")
        
    
# creating GUI
root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textMsg=Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()