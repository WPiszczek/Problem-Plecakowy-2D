from globals import *

class Container:
    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.items = 0
        self.color = color
        self.x = x
        self.y = y

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)

    
#######################################################################
class Box:
    def __init__(self, width, height, value, color):
        self.width = width
        self.height = height
        self.value = value
        self.wage = value/(width * height)
        self.color = color
        self.font = BOX_FONT
        self.x = None
        self.y = None

    def display(self, a, b):
        label = self.font.render("{}".format(int(self.value)),1, black)
        pygame.draw.rect(screen, self.color, (a, b, self.width, self.height))
        pygame.draw.rect(screen, black, (a, b, self.width, self.height),1)
        label_rect = label.get_rect(center=(a + self.width/2, b + self.height/2))
        screen.blit(label, label_rect)

    def check_place(self, container, boxes):
        if container.x <= self.x < self.x + self.width <= container.x + container.width and container.y <= self.y < self.y + self.height <= container.y + container.height: #pojemnik
            pass
        else:
            return False

        for box in boxes:
            if box.x < self.x < box.x + box.width and box.y < self.y < box.y + box.height: #lewy gorny
                return False
            if box.x < self.x < box.x + box.width and box.y < self.y + self.height < box.y + box.height: #lewy dolny
                return False            
            if box.x < self.x + self.width < box.x + box.width and box.y < self.y < box.y + box.height: #prawy gorny
                return False
            if box.x < self.x + self.width < box.x + box.width and box.y < self.y + self.height < box.y + box.height: #prawy dolny
                return False
                ####
            if self.x < box.x < self.x + self.width and self.y < box.y < self.y + self.height: #lewy gorny
                return False
            if self.x < box.x < self.x + self.width and self.y < box.y + box.height < self.y + self.height: #lewy dolny
                return False
            if self.x < box.x + box.width < self.x + self.width and self.y < box.y < self.y + self.height: #prawy gorny
                return False
            if self.x < box.x + box.width < self.x + self.width and self.y < box.y + box.height < self.y + self.height: #prawy dolny
                return False
                ####
            if self.y <= box.y <= box.y + box.height <= self.y + self.height and box.x <= self.x <= self.x + self.width <= box.x + box.width: #zawiera sie w szerokosci
                return False
            if self.x <= box.x <= box.x + box.width <= self.x + self.width and box.y <= self.y <= self.y + self.height <= box.y + box.height: #zawiera sie w wysokosci
                return False
            if self.x <= box.x <= box.x + box.width <= self.x + self.width and self.y <= box.y <= box.y + box.height <= self.y + self.height: #zaslania caly
                return False
            if box.x == self.x and box.x + box.width == self.x + self.width and box.y < self.y < box.y + box.height < self.y + self.height: #zawiera sie w dolnej czesci
                return False
            if box.y == self.y and box.y + box.height == self.y + self.height and box.x < self.x < box.x + box.width < self.x + self.width: #zawiera sie w prawej czesci
                return False
            if box.y == self.y and box.y + box.height == self.y + self.height and self.x < box.x < self.x + self.width < box.x + box.width: #zawiera sie w lewej czesci
                return False
            if box.x == self.x and box.x + box.width == self.x + self.width and self.y < box.y < self.y + self.height < box.y + box.height: #zawiera sie w gornej czesci
                return False
        return True
