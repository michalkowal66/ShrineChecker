import pygame

pygame.init()

tableCol = (54, 103, 38)

gameScreen = pygame.display.set_mode((800,400))

pygame.display.set_caption("Blackjack")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameScreen.fill(tableCol)
    pygame.display.update()