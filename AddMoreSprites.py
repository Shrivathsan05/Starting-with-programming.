import pygame
import random
pygame.init()
MovementSpeed = 5
Score = 0
ScreenWidth, ScreenHeight = 500, 400
class Sprite(pygame.sprite.Sprite):
    def __init__(Self, Size, ImagePath, x, y):
        super().__init__()
        Self.image = pygame.image.load(ImagePath).convert_alpha()
        Self.image = pygame.transform.scale(Self.image, (Size, Size))
        Self.rect = Self.image.get_rect()
        Self.rect.topleft = (x, y)
    def move(Self, x, y):
        Self.rect.x = max(min(Self.rect.x + x, ScreenWidth - Self.rect.width), 0)
        Self.rect.y = max(min(Self.rect.y + y, ScreenHeight - Self.rect.height), 0)
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption(" Collect Enemies! ")
Player = Sprite(50, "Hero.jpeg", 350, 250)
Player.rect.x = random.randint(0, ScreenWidth - Player.rect.width)
Player.rect.y = random.randint(0, ScreenHeight - Player.rect.height)
Enemies = pygame.sprite.Group()
for s in range(7):
    Enemy = Sprite(50, "Enemy.jpg", 20, 20)
    Enemy.rect.x = random.randint(0, ScreenWidth - Enemy.rect.width)
    Enemy.rect.y = random.randint(0, ScreenHeight - Enemy.rect.height)
    Enemies.add(Enemy)
Clock = pygame.time.Clock()
Running = True
while Running:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False
    keys = pygame.key.get_pressed()
    x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MovementSpeed
    y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MovementSpeed
    Player.move(x, y)
    HitList = pygame.sprite.spritecollide(Player, Enemies, True)
    if HitList:
        Score += len(HitList)
        print("Score:", Score)
        if Score >= 7:
            print("You won!")
            Running = False
    Screen.fill(pygame.Color("Red"))
    Screen.blit(Player.image, Player.rect)
    Enemies.draw(Screen)
    pygame.display.flip()
    Clock.tick(60)
pygame.quit()