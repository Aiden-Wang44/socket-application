import socket
import threading
#server side
from tkinter import *
from threading import Thread
canvas_width = 200
canvas_height =200
python_green = "#476042"
master = Tk()
master.title("server")
host=''
port=12345
backlog = 5
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f1=Frame(master,width=100,height=100)
f1.grid(row=1,column=1)

s.bind((host, port))
print('socket binded to', port)
s.listen(backlog)
conn,addr = s.accept()
print ('socket is listening')
print ("Got connection from",addr)
x=3

def rec():
 global x
 while True:
  data = conn.recv(1024)
  l = Label(f1, text=data,fg='red')
  l.grid(row=x, column=1)
  x=x+1
 conn.close()



def sen():
 global x
 l2=Label(f1,text=e.get(),fg='green')
 l2.grid(row=x,column=2)
 x=x+1

 m=e.get().encode()
 e.delete(0,END)
 conn.send(m)



f2=Frame(master,width=100,height=100)
f2.grid(row=2,column=1)
e=Entry(f2)
e.grid(row=2,column=1)
b=Button(f2,text='send', command=sen).grid(row=3,column=1)


recp = threading.Thread(target=rec)
recp.start()
master.mainloop()





