from inout import *
from math import factorial

def copy_coords(l):
    l2 = []
    for i in range(len(l)):
        l2.append([l[i].x, l[i].y])
    return l2

def update_brute(container, boxes_in, boxes, suma, number, end):
    screen.fill(gray)
    container.display()
    for box in boxes_in:
        box.display(box.x, box.y)
        
    TITLE_LABEL = TITLE_FONT.render("Problem plecakowy - algorytm brute force", 1, black)
    TITLE_LABEL_RECT = TITLE_LABEL.get_rect(center=(SCREEN_WIDTH/2,25))
    screen.blit(TITLE_LABEL, TITLE_LABEL_RECT)
    
    SUM_LABEL = SUM_FONT.render("Suma wartości: {}".format(suma),1,black)
    SUM_LABEL_RECT = SUM_LABEL.get_rect(topleft=(50,50+CONTAINER_HEIGHT+20))
    screen.blit(SUM_LABEL, SUM_LABEL_RECT)

    nr_label = SUM_FONT.render("Rozwiazanie nr {}".format(number),1,black)
    nr_label_rect = nr_label.get_rect(topleft=(50,50+CONTAINER_HEIGHT+70))
    screen.blit(nr_label,nr_label_rect)

    display_Boxes(boxes, container.x + container.width + 10, container.y)
    pygame.display.flip()
    #pygame.time.delay(1000)

    if end:
        best_label = SUM_FONT.render("Najlepsze rozwiazanie: {}".format(number),1, black)
        best_label_rect = best_label.get_rect(topleft=(50,50+CONTAINER_HEIGHT+120))
        screen.blit(best_label, best_label_rect)
        pygame.display.flip()

def perm(t, max):
    tab = t
    # wyznaczanie pierwszego od prawej elementu 
    # mniejszego niz jego sasiad z prawej strony
    i = max - 1
    while i>0 and tab[i-1].value >= tab[i].value:
        i -= 1
    # wyznaczanie elementu wiekszego od znalezionego
    if i > 0:
        j = max
        while j > 0 and tab[j-1].value <= tab[i-1].value:
            j -= 1
    # zamiana miejscami dwoch znalezionych wyzej elementow
    if i > 0 and j > 0:
        k = tab[i-1]
        tab[i-1] = tab[j-1]
        tab[j-1] = k
    # odbicie lustrzane szeregu elementow od indeksu i+1 do konca tablicy
    i += 1
    j = max
    while i < j:
        k = tab[i-1]
        tab[i-1] = tab[j-1]
        tab[j-1] = k
        i += 1
        j -= 1
    return tab

def brute_force(boxes, container):
    best_list = []
    best_coords = []
    best_sum = 0
    best_number = 0
    best_left = []
    end = False
    for j in range(factorial(N)):
        number = j + 1
        perm(boxes,N)
        boxes1 = boxes.copy()
        first_box = boxes1.pop(0)
        first_box.x = container.x
        first_box.y = container.y
        boxes_in = [first_box]
        suma = first_box.value
        update_brute(container, boxes_in, boxes1, suma, number, end)
        i = 0
        while len(boxes1)>i>=0:
            flaga4 = 0
            box = boxes1[i]
            coords_list = coords(boxes_in)
            for coord in coords_list: #wstawiamy normalnie lewym gornym
                box.x = coord[0]
                box.y = coord[1]
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes1.remove(box)
                    flaga4 = 1
                    suma += box.value
                    update_brute(container, boxes_in, boxes1, suma,number, end)
                    break
                
            if flaga4 == 0: #wstawiamy lewym dolnym
                for coord in coords_list:
                    box.x = coord[0]
                    box.y = coord[1] - box.height
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes1.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes1, suma,number, end)
                        break
            
            if flaga4 == 0: #wstawiamy prawym gornym
                for coord in coords_list:
                    box.x = coord[0] - box.width
                    box.y = coord[1]
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes1.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes1, suma,number, end)
                        break
                    
            if flaga4 == 0: #wstawiamy prawym dolnym
                for coord in coords_list:
                    box.x = coord[0] - box.width
                    box.y = coord[1] - box.height
                    if box.check_place(container, boxes_in):
                        boxes_in.append(box)
                        boxes.remove(box)
                        flaga4 = 1
                        suma += box.value
                        update_brute(container, boxes_in, boxes, suma,number, end)
                        break

            if flaga4 == 0:
                i = i+1
        if suma > best_sum:
            best_sum = suma
            best_list = boxes_in.copy()
            best_coords = copy_coords(boxes_in)
            best_number = number
            best_left = boxes1
    for i in range(len(best_list)):
        best_list[i].x = best_coords[i][0]
        best_list[i].y = best_coords[i][1]

    end = True
    number = best_number 
    update_brute(container, best_list, best_left, best_sum, best_number, end)
    