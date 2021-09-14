import pygame
import configparser

config = configparser.ConfigParser()
config.read("config.ine")
ploegnaam = config["teamA"]["naam"]
print(ploegnaam)

Scorethuisteam = 0
Scoregastteam = 0
WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("comicsansms", 90)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Scorethuisteam = Scorethuisteam + 1

            if event.key == pygame.K_RIGHT:
                Scoregastteam = Scoregastteam + 1
            if event.key == pygame.K_r:
                Scoregastteam = 0
                Scorethuisteam = 0

    screen.fill("white")



    label = f"""De score tijdens de match is {Scorethuisteam} - {Scoregastteam}"""
    text = font.render(f"""De score  is {Scorethuisteam} - {Scoregastteam}""", True, "blue")
    tekstbreedte = text.get_width()
    teksthoogte = text.get_height()

    screen.blit(text, (WIDTH / 2 - tekstbreedte / 2, HEIGHT / 2 - teksthoogte / 2))
    pygame.display.flip()