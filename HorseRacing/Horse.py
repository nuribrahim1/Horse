import random
import pygame

n = open("namelist.txt","r")
nameList = n.read().split("\n")

def draw_game():
    bg = (17,124,19)
    grid = (255,255,255)
    screen_height = 280
    screen_width = 560
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(bg)
    pygame.draw.line(screen,grid,(140,100),(140,240),5)
    for y in range(120,240,20):
        pygame.draw.line(screen,grid,(70,y),(480,y),5)

class horse():
    def __init__(self,name,speed,y_value,colour):
        self.name = name
        self.speed = speed
        self.odds = (f"{20-speed}/1")
        self.x_value = 135
        self.y_value = y_value
        self.colour = colour

    def run(self):
        self.x_value += random.randint(1,self.speed)

class race():
    def __init__(self,h1,h2,h3,h4,h5):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.race = [h1,h2,h3,h4,h5]
        self.winner = h1

    def begin(self):
        pygame.init()
        screen_height = 280
        screen_width = 560
        screen = pygame.display.set_mode((screen_width, screen_height))

        gun = True
        while gun:
            draw_game()
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    gun = False

            for horse in self.race:
                if horse.x_value < 490:
                    pygame.draw.rect(screen,horse.colour,(horse.x_value,horse.y_value,5,5))
                    horse.run()
                else:
                    print(f"{horse.name} wins")
                    gun = False
            for horse in self.race:
                if horse.x_value > self.winner.x_value:
                    self.winner = horse
            pygame.display.update()
            pygame.time.delay(200)




