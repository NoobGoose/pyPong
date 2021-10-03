import pygame
import random

running = True

ballPOSX = 500
ballPOSY = 500
ballSpeed = 0.1
ballM = 2

timeS = 0
timeE = 0

botPOSX = 790;
botPOSY = 10;

pygame.init()

screen = pygame.display.set_mode([800, 600])


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update

    timeS = timeE
    timeE = pygame.time.get_ticks()
    timeDelta = timeE - timeS

    dDelta = timeDelta * ballSpeed
    tmpballPOSX = ballPOSX + dDelta
    tmpballPOSY = ballPOSY + dDelta * ballM

    if tmpballPOSX > 795 or tmpballPOSX < 5:
        ballM = -1/ballM
        ballSpeed = -ballSpeed

    elif tmpballPOSY > 595 or tmpballPOSY < 5:
        ballM = -1/ballM

    else:
        ballPOSX = tmpballPOSX
        ballPOSY = tmpballPOSY


    ballSpeed = (ballSpeed * (ballSpeed > 1.5)) + (ballSpeed * (random.randint(9999,10003) / 10000) * (ballSpeed < 1.5))
    ballM += (random.randint(-102,100) / 100000)

    print(ballM, "\n")
    print(ballSpeed, "\n")

    # Render


    pygame.draw.circle(screen, (255, 255, 255), (ballPOSX, ballPOSY), 5)

    # for i in range(0, 600, 15):

        # pygame.draw.rect(screen, (255, 255, 255), (399, i, 2, 10))

    # pygame.draw.rect(screen, (255, 255, 255), (botPOSX, botPOSY, 5, 75))

    pygame.display.update()


pygame.quit()
