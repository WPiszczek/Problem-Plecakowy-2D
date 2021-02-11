import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

CONTAINER_WIDTH = 400
CONTAINER_HEIGHT = 400

CONTAINER_X = 50
CONTAINER_Y = 50

CHANGE = CONTAINER_WIDTH/20

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

N = 6

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (128,128,128)
violet = (153,51,255)
yellow = (255,255,51)
orange = (255,128,0)
pink = (255,102,178)
salmon = (255,102,102)

tea = (211,241,210)
cornflower=(144,204,222)
bluebell=(160,155,204)
lilac=(203,166,204)
orchid=(243,198,209)
pale=(253,218,209)
pastel=(210,145,188)
thistle=(224,187,228)
lavender=(149,125,173)
lumber = (225,223,211)

colors = [tea, cornflower, bluebell,lilac, orchid, pale, pastel, thistle, lavender, lumber]
#colors = [white, red, green, blue, violet, yellow, orange, pink, salmon]

flaga = 0

pygame.font.init()
BOX_FONT = pygame.font.SysFont("calibri", 20)
TITLE_FONT = pygame.font.SysFont("calibri", 40)
TITLE_LABEL = TITLE_FONT.render("Problem plecakowy", 1, black)
TITLE_LABEL_RECT = TITLE_LABEL.get_rect(center=(SCREEN_WIDTH/2,25))

SUM_FONT = pygame.font.SysFont("calibri", 30)
SUM_LABEL = SUM_FONT.render("Suma wartości: 0", 1, black)
SUM_LABEL_RECT = SUM_LABEL.get_rect(topleft=(50,470))
