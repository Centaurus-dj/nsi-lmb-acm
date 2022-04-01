"""
Main file, execute initialization of process, variables, etc...

"""
import pygame
from game import Game


def show_startscreen():
    global size

    pygame.display.set_caption("Alone on the start screen - Alexis O., Chloé Sch., Matéo D.")

    # The background color can be whatever you want
    screen_background = pygame.transform.scale(pygame.image.load("assets/main_background.jpg"), size)
    start_btn = pygame.transform.scale(pygame.image.load("assets/Boutons/start.png"), (41*5, 15*5))
    saves_btn = pygame.transform.scale(pygame.image.load("assets/Boutons/settings.png"), (16*3, 16*3))

    screen = pygame.display.set_mode(size)

    ### Show Elements on screen
    screen.blit(screen_background, (0, 0))
    start_b = screen.blit(start_btn, (440, 10))
    screen.blit(saves_btn, (650, 34))
    pygame.display.flip()


    ### While loop to stay displayed until input of user
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                if start_b.collidepoint(pos):
                    running = False
                    pygame.quit()

def main():
    pygame.display.set_caption("Alone in a room - Alexis O., Chloé Sch., Matéo D.")
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('assets/background.jpg')
    background = pygame.transform.scale(background, size)

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
                    game.fireball.shoot_up()
                if event.key == pygame.K_q:
                    game.player.launch_projectile()
                if event.key == pygame.K_s:
                    game.player.launch_projectile()
                if event.key == pygame.K_d:
                    game.player.launch_projectile()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

if __name__ == "__main__":

    (width, height) = (1080, 720)
    size = (width, height)

    pygame.init()

    show_startscreen()
    main()
