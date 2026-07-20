#This activity, "Colorful Bounce," involves a moving rectangle (sprite) that bounces off the window edges. Each bounce changes its color and the window's background color, creating a dynamic display of colors.
import pygame 
import random
pygame.init()
SpriteColorChangeEvent = pygame.USEREVENT + 1
BackgroundColorChangeEvent = pygame.USEREVENT + 2
Blue = pygame.Color(" Blue ")
LightBlue = pygame.Color(" Light Blue ")
DarkBlue = pygame.Color(" Dark Blue ")
Yellow = pygame.Color(" Yellow ")
Magenta = pygame.Color(" Magenta ")
Orange = pygame.Color(" Orange ")
White = pygame.Color(" White ")
class Sprite(pygame.sprite.Sprite):
    def __init__(Self, Color, Height, Width) :
        super().__init__()
        Self.Image = pygame.Surface((Width, Height))
        Self.Image.fill(Color)
        Self.Rect = Self.Image.get_rect()
        Self.Velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(Self):
        Self.Rect.move_ip(Self.Velocity)
        BoundaryHit = False
        if Self.Rect.Left <= 0 or Self.Rect.Right >= 500:
            Self.Velocity[0] = -Self.Velocity[0]
            BoundaryHit = True
        if Self.Rect.Top <= 0 or Self.Rect.Bottom >= 400:
            Self.Velocity[1] = -Self.Velocity[1]
            BoundaryHit = True
        if BoundaryHit:
            pygame.event.post(pygame.event.Event(SpriteColorChangeEvent))
            pygame.event.post(pygame.event.Event(BackgroundColorChangeEvent))
    def ChangeColor(self):
        self.Image.fill(random.choice([Yellow, Magenta, Orange, White]))
def ChangeBackgroundColor(self):
    global BackgroundColor
    BackgroundColor = random.choice([Blue, LightBlue, DarkBlue])
AllSpritesList = pygame.sprite.Group()
TheSprite = Sprite(White, 20, 30)
TheSprite.rect.x = random.randint(0, 480)
TheSprite.rect.y = random.randint(0, 370)
AllSpritesList.add(TheSprite)
Screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption(" Colorful Boundary Sprite Bounce! ")
BackgroundColor = Blue
Screen.fill(BackgroundColor)
Exit = False
Clock = pygame.time.Clock()
while not Exit :
    for Event in pygame.event.get() :
        if Event.type in pygame.QUIT :
            Exit = True
        elif Event.type == SpriteColorChangeEvent :
            TheSprite.ChangeColor()
        elif Event.type == BackgroundColorChangeEvent :
            ChangeBackgroundColor()
    AllSpritesList.update()
    Screen.fill(BackgroundColor)
    AllSpritesList.draw(Screen)
    pygame.display.flip()
    Clock.tick(240)
pygame.quit()