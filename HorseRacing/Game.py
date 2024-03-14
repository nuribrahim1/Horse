import pygame
from random import randint
nameList = ["a","b","c","d","e","f","g"]

class horse():
    def __init__(self,name,speed,y_value,colour):
        self.name = name
        self.speed = speed
        self.odds = (f"{20-speed}/1")
        self.x_value = 135
        self.y_value = y_value
        self.colour = colour

    def run(self):
        self.x_value += randint(1,self.speed)

pygame.init()
screen_height = 280
screen_width = 560
please = int(input("HEllo"))

screen = pygame.display.set_mode((screen_width,screen_height))

def draw_game():
    bg = (17,124,19)
    grid = (255,255,255)
    screen.fill(bg)
    pygame.draw.line(screen,grid,(140,100),(140,240),5)
    for y in range(120,240,20):
        pygame.draw.line(screen,grid,(70,y),(480,y),5)

h1 = horse("5",randint(11,18),130,(255,0,0))
h2 = horse("4",randint(11,18),150,(10,10,10))
h3 = horse("3",randint(11,18),170,(0,0,255))
h4 = horse("2",randint(11,18),190,(255,165,0))
h5 = horse("1",randint(11,18),210,(238,130,238))

horses = [h1,h2,h3,h4,h5]
x = 135
run = True
while run:

    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for horse in horses:
        if horse.x_value < 480:
            pygame.draw.rect(screen,horse.colour,(horse.x_value,horse.y_value,5,5))
            horse.run()
        else:
            print(f"{horse.name} wins")
            pygame.quit()
    pygame.display.update()
    pygame.time.delay(200)

pygame.quit()
