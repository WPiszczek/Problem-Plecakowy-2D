import random
from classes import *

def coords(boxes):
    list = []
    [list.append((box.x, box.y)) for box in boxes]
    [list.append((box.x, box.y + box.height)) for box in boxes]
    [list.append((box.x + box.width, box.y)) for box in boxes]
    [list.append((box.x + box.width, box.y + box.height)) for box in boxes]
    return list

def random_Boxes():
    l = []
    for i in range(N):
        a = random.randint(1,10) * CHANGE
        b = random.randint(1,10) * CHANGE
        c = random.randint(1,10)
        d = random.choice(colors)
        l.append(Box(a,b,c,d))
    return l

def read_Boxes():
    l = []
    for i in range(N):
        print("Przedmiot ", i, ":")
        a = int(input("Podaj szerokosc (1-10): ")) * CHANGE
        b = int(input("Podaj wysokosc (1-10): ")) * CHANGE
        c = int(input("Podaj wartosc (1-10): "))
        d = random.choice(colors)
        l.append(Box(a,b,c,d))
    return l

def print_Boxes(boxes):
    i = 0
    for box in boxes:
        print("Pudełko nr {}: szerokosc {} wysokosc {} wartosc {}".format(i, box.width, box.height, box.value))
        i += 1

def display_Boxes(boxes, a, b):
    A = a
    B = b
    max_height = 0
    for box in boxes:
        if box.width < SCREEN_WIDTH - a - 10:
            box.display(a, b)
            a = a + box.width + 10
            if box.height > max_height:
                max_height = box.height
        else:
            a = A
            b = B + max_height + 10
            max_height = 0
            B = b
            box.display(a, b)
            a = a + box.width + 10
            if box.height > max_height:
                max_height = box.height
        
        
    