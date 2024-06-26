import random
from Game import *

n = open("namelist.txt", "r")
nameList = n.read().split("\n")

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




