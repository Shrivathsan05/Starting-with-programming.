import pygame
pygame.init()
ScreenWidth, ScreenHeight = 500, 500
DisplaySurface = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption(" My First Game Screen ")
BackgroundColor = pygame.Color(" Grey ")
SpiderManImage = pygame.transform.scale(pygame.image.load("Spidey.jpg").convert_alpha(), (300, 300))
SpidermanRectangularAreaOfTheSurface = SpiderManImage.get_rect(center = (ScreenWidth // 2, ScreenHeight // 2))
def GameLoop() :
    Clock = pygame.time.Clock()
    Running = True
    while Running :
        for Event in pygame.event.get() :
            if Event.type == pygame.QUIT :
                Running = False
        DisplaySurface.fill(BackgroundColor)
        DisplaySurface.blit(SpiderManImage, SpidermanRectangularAreaOfTheSurface)
        pygame.display.flip()
        Clock.tick(30)
    pygame.quit()
if __name__ == "__main__" :
    GameLoop()