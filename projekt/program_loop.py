from classes import Box, Container
import math
from greedy import *
from brute import *
import time

def program_loop(container, boxes, option):
    pygame.init()
    pygame.display.set_caption("Problem plecakowy")
    
    done = False
    chosen = False
    screen.fill(gray)
    container.display()
    
    screen.blit(TITLE_LABEL, TITLE_LABEL_RECT)
    screen.blit(SUM_LABEL, SUM_LABEL_RECT)
    display_Boxes(boxes, container.x + container.width + 10, container.y)
    pygame.display.flip()
    #pygame.time.delay(1000)
    
    #for _ in range(10):
    #boxes = random_Boxes()
    start = time.time()
    if option == "greedy":
        greedy(boxes, container)
    elif option == "brute":
        brute_force(boxes, container)
    end = time.time()
    duration = end - start
    print(duration)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
