
from pynput import keyboard
from random import *

def padmiddle(nbr: int):
    return ((4 - int(len(str(nbr)) / 2) - (len(str(nbr)) % 2)) * " " + str(nbr) + (4 - int(len(str(nbr)) / 2)) * " ")


nbrs = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def alea():
    nbr = randint(0, 15)
    if (nbrs[nbr] != ""):
        alea()
        return
    nbrs[nbr] = 2

def right():
    for x in range (40):
        for j in range(4):
            for i in range(3):
                if (nbrs[(2-i)+j*4 + 1] == ""):
                    nbrs[(2-i)+j*4 + 1] = nbrs[(2-i)+j*4]
                    nbrs[(2-i)+j*4] = ""
                if (nbrs[(2-i)+j*4] == nbrs[(2-i)+j*4 + 1]):
                    nbrs[(2-i)+j*4 + 1] *= 2
                    nbrs[(2-i)+j*4] = ""

def left():
    for x in range (40):
        for j in range(4):
            for i in range(1,4):
                if (nbrs[(i)+j*4 - 1] == ""):
                    nbrs[(i)+j*4 - 1] = nbrs[(i)+j*4]
                    nbrs[(i)+j*4] = ""
                if (nbrs[(i)+j*4] == nbrs[(i)+j*4 - 1]):
                    nbrs[(i)+j*4 - 1] *= 2
                    nbrs[(i)+j*4] = ""

def down():
    for x in range (40):
        for j in range(4):
            for i in range(3):
                if (nbrs[(3-j)+i*4 + 4] == ""):
                    nbrs[(3-j)+i*4 + 4] = nbrs[(3-j)+i*4]
                    nbrs[(3-j)+i*4] = ""
                if (nbrs[(3-j)+i*4] == nbrs[(3-j)+i*4 + 4]):
                    nbrs[(3-j)+i*4 + 4] *= 2
                    nbrs[(3-j)+i*4] = ""

def up():
    for x in range (40):
        for j in range(4):
            for i in range(1,4):
                if (nbrs[(j)+i*4 - 4] == ""):
                    nbrs[(j)+i*4 - 4] = nbrs[(j)+i*4]
                    nbrs[(j)+i*4] = ""
                if (nbrs[(j)+i*4] == nbrs[(j)+i*4 - 4]):
                    nbrs[(j)+i*4 - 4] *= 2
                    nbrs[(j)+i*4] = ""




def on_press(key):
    tab =f"\n\n\n\n\
+--------+--------+--------+--------+\n\
|        |        |        |        |\n\
|{padmiddle(nbrs[0])}|{padmiddle(nbrs[1])}|{padmiddle(nbrs[2])}|{padmiddle(nbrs[3])}|\n\
|        |        |        |        |\n\
+--------+--------+--------+--------+\n\
|        |        |        |        |\n\
|{padmiddle(nbrs[4])}|{padmiddle(nbrs[5])}|{padmiddle(nbrs[6])}|{padmiddle(nbrs[7])}|\n\
|        |        |        |        |\n\
+--------+--------+--------+--------+\n\
|        |        |        |        |\n\
|{padmiddle(nbrs[8])}|{padmiddle(nbrs[9])}|{padmiddle(nbrs[10])}|{padmiddle(nbrs[11])}|\n\
|        |        |        |        |\n\
+--------+--------+--------+--------+\n\
|        |        |        |        |\n\
|{padmiddle(nbrs[12])}|{padmiddle(nbrs[13])}|{padmiddle(nbrs[14])}|{padmiddle(nbrs[15])}|\n\
|        |        |        |        |\n\
+--------+--------+--------+--------+\n"
    print(tab)
    if (key == key.right):
        right()
        alea()
    if (key == key.left):
        left()
        alea()
    if (key == key.up):
        up()
        alea()
    if (key == key.down):
        down()
        alea()

def on_release(key):
    return
print(" ___   ___    __   ___ \n\
(__ \ / _ \  /. | ( _ )\n\
 / _/( (_) )(_  _)/ _ \\\n\
(____)\___/   (_) \___/\n\n\
use arrows start game and play ! have fun")
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()