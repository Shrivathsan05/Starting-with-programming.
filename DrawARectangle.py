#Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Draw a Rectangle")
Done = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()