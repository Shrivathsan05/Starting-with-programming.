import pygame
pygame.init()
ScreenWidth, ScreenHeight = 500, 500
DisplaySurface = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption(" Adding an image and a background image ")
BackgroundImage = pygame.transform.scale(pygame.image.load("Marvel.jpg").convert(), (ScreenWidth, ScreenHeight))
SpiderManImage = pygame.transform.scale(pygame.image.load("Spidey.jpg").convert_alpha(), (200, 200))
SpidermanRectangularAreaOfTheSurface = SpiderManImage.get_rect(center = (ScreenWidth // 2, ScreenHeight // 2 - 30))
Text = pygame.font.Font(None, 36).render(" Hello World ", True, pygame.Color(" Crimson "))
TextRectangularAreaOfTheSurface = Text.get_rect(center = (ScreenWidth // 2, ScreenHeight // 2 + 110))
def GameLoop() :
    Clock = pygame.time.Clock()
    Running = True
    while Running :
        for Event in pygame.event.get() :
            if Event.type == pygame.QUIT :
                Running = False
        DisplaySurface.blit(BackgroundImage, (0, 0))
        DisplaySurface.blit(SpiderManImage, SpidermanRectangularAreaOfTheSurface)
        DisplaySurface.blit(Text, TextRectangularAreaOfTheSurface)
        pygame.display.flip()
        Clock.tick(30)
    pygame.quit()
if __name__ == "__main__" :
    GameLoop()