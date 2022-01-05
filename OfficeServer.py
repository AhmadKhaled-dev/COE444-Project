import socket
from datetime import *
from firebase import firebase
import time

firebase = firebase.FirebaseApplication("add the link to your firebase database",None)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''

port = 5555

s.bind((host, port))

s.listen(5)

clientSocket, address = s.accept()

while True:

    print("Connection established")
    datarec = clientSocket.recv(1024)
    da = datarec.decode()

    now = datetime.now()

    fireTime = now.strftime(" %d %b, %Y %H:%M:%S")
    date = {
        'info' : "There is a fire in the "+da,
        'time' : fireTime
    }
    if(da == 'Office'):
        result = firebase.post('/fireHistory', date)
        print(result)
