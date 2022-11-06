import socket
from _thread import *
from Player import player
import pickle
import random

colorlist = [(255, 0,0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (134, 55, 167), (0, 255, 167)]

def get_color():
    color = colorlist.pop(colorlist.index(random.choice(colorlist)))
    return color


server = socket.gethostname()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print('waiting for connection')

players = [player(0,0,10, get_color()), player(0,0,10, get_color())]

def threaddin_the_breadin(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(10000))
            players[player] = data

            if not data:
                print("you done fucked up")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentplayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaddin_the_breadin, (conn, currentplayer))
    players.append(player(0, 0, 10, get_color()))
    currentplayer += 1



