#Write a Python program to create an empty Pygame window.
import pygame
pygame.init()
Screen = pygame.display.set_mode((400, 500))
Done = False
while not Done :
    for Event in pygame.Event.get() :
        if Event.type == pygame.QUIT :
            pygame.quit()
    pygame.display.flip