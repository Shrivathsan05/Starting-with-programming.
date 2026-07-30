import math
import random
import pygame
ScreenWidth = 800
ScreenHeight = 500
PlayerStartX = 370
PlayerStartY = 380
EnemyStartYMinimum = 50
EnemyStartYMaximum = 150
EnemySpeedX = 4
EnemySpeedY = 40
BulletSpeedY = 10
CollisionDistance = 27
pygame.init()
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
Background = pygame.image.load("Space.jpeg")
pygame.display.set_caption("Space Invaders")
Icon = pygame.image.load("UFO-removebg-preview.png")
pygame.display.set_icon(Icon)
PlayerImage = pygame.image.load("MilanoAKAStarlord_sShip-removebg-preview.png")
PlayerX = PlayerStartX
PlayerY = PlayerStartY
PlayerXChange = 0
EnemyImage = []
EnemyX = []
EnemyY = []
EnemyXChange = []
EnemyYChange = []
NumberofEnemies = 6
for i in range(NumberofEnemies):
    EnemyImage.append(pygame.image.load("UFO-removebg-preview.png"))
    EnemyX.append(random.randint(0, ScreenWidth - 64))
    EnemyY.append(random.randint(EnemyStartYMinimum, EnemyStartYMaximum))
    EnemyXChange.append(EnemySpeedX)
    EnemyYChange.append(EnemySpeedY)
BulletImage = pygame.image.load("Bullet_.jpeg-removebg-preview.png")
BulletX = 0
BulletY = PlayerStartY
BulletXChange = 0
BulletYChange = BulletSpeedY
BulletState = " Ready! "
ScoreValue = 0
Font = pygame.font.Font('freesansbold.ttf', 32)
TextX = 10
TextY = 10
GameOverTextFont = pygame.font.Font('freesansbold.ttf', 64)
def ShowScore(x, y):
    score = Font.render(" Score : " + str(ScoreValue), True, (255, 255, 255))
    Screen.blit(score, (x, y))
def ShowTheGameOverText():
    TheGameOverText = GameOverTextFont.render(" GAME OVER ", True, (255, 255, 255))
    Screen.blit(TheGameOverText, (200, 250))
def DrawThePlayer(x, y):
    Screen.blit(PlayerImage, (x, y))
def DrawTheEnemy(x, y, s):
    Screen.blit(EnemyImage[s], (x, y))
def FireTheBullet(x, y):
    global BulletState
    BulletState = " Firing! "
    Screen.blit(BulletImage, (x + 16, y + 10))
def CheckForCollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((EnemyX - BulletX) ** 2 + (EnemyY - BulletY) ** 2)
    return distance < CollisionDistance
Running = True
while Running:
    Screen.fill((0, 0, 0))
    Screen.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerXChange = -5
            if event.key == pygame.K_RIGHT:
                PlayerXChange = 5
            if event.key == pygame.K_SPACE and BulletState == " Ready! ":
                    BulletX = PlayerX
                    FireTheBullet(BulletX, BulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            PlayerXChange = 0
    PlayerX += PlayerXChange
    PlayerX = max(0, min(PlayerX, ScreenWidth - 64))
    for s in range(NumberofEnemies):
        if EnemyY[s] > 340:
            for k in range(NumberofEnemies):
                EnemyY[k] = 2000
            ShowTheGameOverText()
            break
        EnemyX[s] += EnemyXChange[s]
        if EnemyX[s] <= 0 or EnemyX[s] >= ScreenWidth - 64:
            EnemyXChange[s] *= -1
            EnemyY[s] += EnemyYChange[s]
        if CheckForCollision(EnemyX[s], EnemyY[s], BulletX, BulletY):
            BulletY = PlayerStartY
            BulletState = " Ready! "
            ScoreValue += 1
            EnemyX[s] = random.randint(0, ScreenWidth - 64)
            EnemyY[s] = random.randint(EnemyStartYMinimum, EnemyStartYMaximum)
        DrawTheEnemy(EnemyX[s], EnemyY[s], s)
    if BulletY <= 0:
        BulletY = PlayerStartY
        BulletState = " Ready! "
    elif BulletState == " Firing! ":
        FireTheBullet(BulletX, BulletY)
        BulletY -= BulletYChange
    DrawThePlayer(PlayerX, PlayerY)
    ShowScore(TextX, TextY)
    pygame.display.update()