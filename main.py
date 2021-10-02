import pygame

running = True

ballPOSX = 500
ballPOSY = 500
ballSpeed = 100

ballM = 2
ballDir2L = True;

botPOSX = 790;
botPOSY = 10;

pygame.init()

screen = pygame.display.set_mode([800, 600])


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update


    # Render

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (ballPOSX, ballPOSY), 5)

    for i in range(0, 600, 15):

        pygame.draw.rect(screen, (255, 255, 255), (399, i, 2, 10))

    pygame.draw.rect(screen, (255, 255, 255), (botPOSX, botPOSY, 5, 75))

    pygame.display.update()

pygame.quit()
