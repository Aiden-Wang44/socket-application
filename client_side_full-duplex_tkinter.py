import socket
from tkinter import *
import threading
canvas_width = 200
canvas_height =200
python_green = "#476042"
master = Tk()
master.title("client")
host='127.0.0.1'  # server side ip address
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
x=3
f1=Frame(master,width=100,height=100)
f1.grid(row=1,column=1)
def rec():
    global x
    while True:
        data = s.recv(1024)
        l = Label(f1, text=data,fg='green')

        l.grid(row=x, column=1)
        x=x+1
    s.close()




def sen():
    global x
    l2 = Label(f1, text=e.get(), fg='red')
    l2.grid(row=x, column=2)
    x = x + 1
    message=e.get()
    s.send(message.encode())
    e.delete(0, END)

f2=Frame(master,width=100,height=100)
f2.grid(row=2,column=1)
e=Entry(f2)
e.grid(row=2,column=1)
b=Button(f2,text='send', command=sen).grid(row=3,column=1)



recp=threading.Thread(target=rec)
recp.start()

master.mainloop()

