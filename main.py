import socket
from tkinter import *
def leak():
  s = socket.Socket(socket.AF_INET, socket.SOCK_STREAM)
  ip = s.listen(ip)
  print(ip)
  s.send(ip, "https://github.com/Hackerr7767")
root = Tk()
btn = Button(root, text="Leak 'MeowMid!' IP Address in the console", command=leak)
root.mainloop()
