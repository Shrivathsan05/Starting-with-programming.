#Write a program where a player controls a sprite when two sprites collide , the game displaying a win message upon meeting a specific condition.
import pygame
import random
ScreenWidth, ScreenHeight = 500, 400
MovmentSpeed = 5
FontSize = 72
pygame.init()
BackgroundImage = pygame.image.load("MARVEL.jpg")
Font = pygame.font.SysFont("Times New Roman", FontSize, True, True)
class Sprite(pygame.sprite.Sprite) :
    def __init__(Self, Color, Height, Width):
        super().__init__()
        Self.image = pygame.Surface((Width, Height))
        Self.image.fill(pygame.Color(" DodgerBlue "))
        pygame.draw.rect(Self.image, Color, pygame.Rect(0, 0, Width, Height))
        Self.rect = Self.image.get_rect()
    def Move(Self, X, Y):
        Self.rect.x = max(min(Self.rect.x + X, ScreenWidth - Self.rect.width), 0)
        Self.rect.y = max(min(Self.rect.y + Y, ScreenHeight - Self.rect.height), 0)
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Sprite Collision")
AllSprites = pygame.sprite.Group()
Sprite1 = Sprite(pygame.Color(" Black "), 20, 30)
Sprite1.rect.x, Sprite1.rect.y = random.randint(0, ScreenWidth - Sprite1.rect.width), random.randint(0, ScreenHeight - Sprite1.rect.height)
AllSprites.add(Sprite1)
Sprite2 = Sprite(pygame.Color(" Red "), 20, 30)
Sprite2.rect.x, Sprite2.rect.y = random.randint(0, ScreenWidth - Sprite2.rect.width), random.randint(0, ScreenHeight - Sprite2.rect.height)
AllSprites.add(Sprite2)
Running, Won = True, False
Clock = pygame.time.Clock()
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            Running = False
    if not Won:
        keys = pygame.key.get_pressed()
        x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MovmentSpeed
        y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MovmentSpeed
        Sprite1.Move(x, y)
    if Sprite1.rect.colliderect(Sprite2.rect):
        AllSprites.remove(Sprite2)
        Won = True
    Screen.blit(BackgroundImage, (0, 0))
    AllSprites.draw(Screen)
    if Won :
        WinText = Font.render("You Win!", True, pygame.Color(" Dark Red "))
        Screen.blit(WinText, (ScreenWidth // 2 - WinText.get_width() // 2, ScreenHeight // 2 - WinText.get_height() // 2))
    pygame.display.flip()
    Clock.tick(90)
pygame.quit()
