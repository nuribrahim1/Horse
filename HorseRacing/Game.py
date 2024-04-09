import pygame


pygame.init()
screen_height = 280
screen_width = 560

screen = pygame.display.set_mode((screen_width,screen_height))

def draw_game():
    bg = (17,124,19)
    grid = (255,255,255)
    screen.fill(bg)
    pygame.draw.line(screen,grid,(140,100),(140,240),5)
    for y in range(120,240,20):
        pygame.draw.line(screen,grid,(70,y),(480,y),5)