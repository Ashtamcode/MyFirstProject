import pygame
from pygame import mixer

pygame.init()
mixer.init()
# song
mixer.music.load("Inspiring Acoustic - AShamaluevMusic.mp3")
mixer.music.set_volume(1)
mixer.music.play()
# screen
screen = pygame.display.set_mode((1280, 720))

# caption

pygame.display.set_caption('Teachers Day')
# font
ash = pygame.font.Font('freesansbold.ttf', 32)


# pic
pic = pygame.image.load('t.png')
count = 15
running = True
while running:
    screen.blit(pic, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
