"""
Main file, execute initialization of process, variables, etc...

"""
import projectile
from game import *
from projectile import *

pygame.init()
projectile_ = projectile.Projectile
pygame.display.set_caption("jeux")
screen = pygame.display.set_mode((1080, 600))
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1080, 600))
game = Game()

running = True

while running:

    screen.blit(background, (0, 0))

    game.update(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_z:
                projectile_.shoot_up()
            if event.key == pygame.K_q:
                game.player.launch_projectile()
            if event.key == pygame.K_s:
                game.player.launch_projectile()
            if event.key == pygame.K_d:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
