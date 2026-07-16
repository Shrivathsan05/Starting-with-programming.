#Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
pygame.init()
Window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hollow and Solid Balls")
Window.fill((255, 255, 255))
Green = (0, 255, 0)
pygame.draw.circle(Window, Green, (300, 300), 50)
pygame.draw.circle(Window, Green, (100, 100), 50, 3)
pygame.display.update()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()