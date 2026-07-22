import pygame
pygame.init()
GameScreen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" Add Sprites ")
RectangleStationary = pygame.Rect(350, 275, 100, 50)
RectangleMoving = pygame.Rect(350, 275, 25, 50)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    GameScreen.fill((0, 0, 0))
    pygame.draw.rect(GameScreen, (0, 0, 255), RectangleStationary)
    pygame.draw.rect(GameScreen, (255, 0, 0), RectangleMoving)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            RectangleMoving.x -= 1
        if event.key == pygame.K_RIGHT:
            RectangleMoving.x += 1
        if event.key == pygame.K_UP:
            RectangleMoving.y -= 1
        if event.key == pygame.K_DOWN:
            RectangleMoving.y += 1
    pygame.display.flip()    
pygame.quit()