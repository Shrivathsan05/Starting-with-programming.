#Write a program that detects when keys are pressed and changes the color of a sprite when it touches the screen boundaries.
import pygame
def main():
    pygame.init()
    ScreenWidth, ScreenHeight = 500, 500
    Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
    pygame.display.set_caption(" Color Changing Sprite ")
    Colors = {" Red " : pygame.Color(" Red "), " Green " : pygame.Color(" Green "), " Blue " : pygame.Color(" Blue "), " Yellow " : pygame.Color(" Yellow "), " White " : pygame.Color(" White ")}
    CurrentColor = Colors[" White "]
    X, Y = 30, 30
    SpriteWidth, SpriteHeight = 60, 60
    Clock = pygame.time.Clock()
    Done = False
    while not Done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Done = True
        Pressed = pygame.key.get_pressed()
        if Pressed[pygame.K_LEFT]:
            X -= 3
        if Pressed[pygame.K_RIGHT]:
            X += 3
        if Pressed[pygame.K_UP]:
            Y -= 3
        if Pressed[pygame.K_DOWN]:
            Y += 3
        X = min(max(0, X), ScreenWidth - SpriteWidth)
        Y = min(max(0, Y), ScreenHeight - SpriteHeight)
        if X == 0 :
            CurrentColor = Colors[" Blue "]
        elif X == ScreenWidth - SpriteWidth:
            CurrentColor = Colors[" Yellow "]
        elif Y == 0:
            CurrentColor = Colors[" Red "]
        elif Y == ScreenHeight - SpriteHeight:
            CurrentColor = Colors[" Green "]
        else:
            CurrentColor = Colors[" White "]
        Screen.fill((0, 0, 0))
        pygame.draw.rect(Screen, CurrentColor, (X, Y, SpriteWidth, SpriteHeight))
        pygame.display.flip()
        Clock.tick(90)
    pygame.quit()   
if __name__ == "__main__":
    main()