import pygame
from time import sleep
from random import randint
pygame.init()
screen = pygame.display.set_mode((600,450))
fon = pygame.image.load("fon.jpg").convert()
fon=pygame.transform.scale(fon,(600,450))
screen.blit(fon,(0,0))

clock  = pygame.time.Clock()

rocket = pygame.image.load("rocket.png").convert_alpha()
rocket = pygame.transform.scale(rocket,(rocket.get_width()//8, rocket.get_height()//8))
rocket_rect = rocket.get_rect()



meteorit = pygame.image.load('meteorit.png').convert_alpha()
meteorit = pygame.transform.scale(meteorit,(meteorit.get_width()//5, meteorit.get_height()//5))

meteorit_rect = meteorit.get_rect()


game = True
move_right = False
move_left = False
speed_x = 0
speed_y = 5
heals=3
rocket_rect.x = 250
rocket_rect.y = 250
while game:
    screen.blit(fon,(0,0))
    screen.blit(pygame.font.Font(None, 70).render("Health: "+str(heals),True,(255,0,0)),(10,10))
    screen.blit(rocket, rocket_rect)
    screen.blit(meteorit, meteorit_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    
    if move_right and rocket_rect.x <470:
        rocket_rect.x +=5
        
    if move_left and rocket_rect.x >-60:
        rocket_rect.x -=5
        
    meteorit_rect.y  +=speed_y
    
    if meteorit_rect.y >450:
        meteorit_rect.x = randint(-60,470)
        meteorit_rect.y = 0
    if rocket_rect.colliderect(meteorit_rect):
        meteorit_rect.y=-100
        meteorit_rect.x=randint(-60,470)
        for i in range(3):
            screen.blit(fon,(0,0))
            pygame.display.flip()
            sleep(0.5)
            screen.blit(rocket, rocket_rect)
            pygame.display.flip()
            sleep(0.5)
        heals-=1
        if heals==0:
            game=False


            
    
    clock.tick(40)
    pygame.display.flip()
screen.blit(fon,(0,0))
screen.blit(pygame.font.Font(None,40).render("You lost your love",True,(0,0,0)),(250,200))


clock.tick(40)
pygame.display.flip()
