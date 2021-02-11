from inout import *

def update_greedy(container, boxes_in, boxes, suma):
    screen.fill(gray)
    container.display()
    for box in boxes_in:
        box.display(box.x, box.y)
    TITLE_LABEL = TITLE_FONT.render("Problem plecakowy - algorytm zachłanny", 1, black)
    TITLE_LABEL_RECT = TITLE_LABEL.get_rect(center=(SCREEN_WIDTH/2,25))
    screen.blit(TITLE_LABEL, TITLE_LABEL_RECT)
    SUM_LABEL = SUM_FONT.render("Suma wartości: {}".format(suma),1,black)
    SUM_LABEL_RECT = SUM_LABEL.get_rect(topleft=(50,470))
    screen.blit(SUM_LABEL, SUM_LABEL_RECT)
    display_Boxes(boxes, container.x + container.width + 10, container.y)
    pygame.display.flip()
    #pygame.time.delay(2000)

def greedy(boxes, container):
    boxes.sort(key=lambda x: x.wage, reverse=True)
    first_box = boxes.pop(0)
    first_box.x = container.x
    first_box.y = container.y
    boxes_in = [first_box]
    suma = first_box.value
    update_greedy(container, boxes_in, boxes, suma)
    i = 0 
    while len(boxes)>i>=0:
        flaga1 = 0
        box = boxes[i]
        coords_list = coords(boxes_in)
        for coord in coords_list: #wstawiamy normalnie lewym gornym
            box.x = coord[0]
            box.y = coord[1]
            if box.check_place(container, boxes_in):
                boxes_in.append(box)
                boxes.remove(box)
                flaga1 = 1
                suma += box.value
                update_greedy(container, boxes_in, boxes, suma)
                break
            
        if flaga1 == 0: #wstawiamy lewym dolnym
            for coord in coords_list:
                box.x = coord[0]
                box.y = coord[1] - box.height
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break
        
        if flaga1 == 0: #wstawiamy prawym gornym
            for coord in coords_list:
                box.x = coord[0] - box.width
                box.y = coord[1]
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break
                
        if flaga1 == 0: #wstawiamy prawym dolnym
            for coord in coords_list:
                box.x = coord[0] - box.width
                box.y = coord[1] - box.height
                if box.check_place(container, boxes_in):
                    boxes_in.append(box)
                    boxes.remove(box)
                    flaga1 = 1
                    suma += box.value
                    update_greedy(container, boxes_in, boxes, suma)
                    break

        if flaga1 == 0:
            i = i+1
    return