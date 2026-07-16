import pygame
pygame.init()
ScreenWidth, ScreenHeight = 640, 480
DisplaySurface = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption(" My First Game Screen ")
BackgroundColor = pygame.Color(" White ")
Text = pygame.font.Font(None, 36).render(" Hello World ", True, pygame.Color(" Crimson "))
TextRectangularAreaOfTheSurface = Text.get_rect(center = (ScreenWidth // 2, ScreenHeight // 2 + 110))
def GameLoop() :
    Clock = pygame.time.Clock()
    Running = True
    while Running :
        for Event in pygame.event.get() :
            if Event.type == pygame.QUIT :
                Running = False
        DisplaySurface.fill(BackgroundColor)
        DisplaySurface.blit(Text, TextRectangularAreaOfTheSurface)
        pygame.draw.rect(DisplaySurface, (255, 0, 0), pygame.Rect(290, 200, 60, 70))
        pygame.display.flip()
        Clock.tick(30)
    pygame.quit()
if __name__ == "__main__" :
    GameLoop()