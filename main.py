"""
Main file, execute initialization of process, variables, etc...

"""
import pygame
from game import Game


def show_startscreen():
    global size

    pygame.display.set_caption("Alone on the start screen - Alexis O., Chloé Sch., Matéo D.")
    clock = pygame.time.Clock()

    # The background color can be whatever you want
    screen_background = pygame.transform.scale(pygame.image.load("assets/main_background.jpg"), size)
    start_btn = pygame.transform.scale(pygame.image.load("assets/Boutons/start.png"), (41*5, 15*5))
    saves_btn = pygame.transform.scale(pygame.image.load("assets/Boutons/settings.png"), (16*3, 16*3))

    screen = pygame.display.set_mode(size)

    ### Show Elements on screen
    screen.blit(screen_background, (0, 0))
    start_b = screen.blit(start_btn, (440, 10))
    screen_b = screen.blit(saves_btn, (650, 34))
    font = pygame.font.Font("fonts/Roboto-Regular.ttf", 24)
    user_text = ''

    # create rectangle
    screen.blit(font.render("Your username", True, "white"), (420, 200))
    input_rect = pygame.Rect(440, 230, 140, 32)

    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('black')
    color = color_passive

    active = False
    running = True

    while running:
        for event in pygame.event.get():

        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if start_b.collidepoint(event.pos):
                    if len(user_text) != 0:
                        game.create_player(user_text)
                        running = False


            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def main():
    pygame.display.set_caption("Alone in a room - Alexis O., Chloé Sch., Matéo D.")
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('assets/background.jpg')
    background = pygame.transform.scale(background, size)

    running = True

    while running:

        screen.blit(background, (0, 0))
        game.update(screen)
        save_b = screen.blit(pygame.transform.scale(pygame.image.load("assets/Boutons/save.png",), (13*4, 13*4)), (900, 10))
        load_b = screen.blit(pygame.transform.scale(pygame.image.load("assets/Boutons/load.png",), (13*4, 13*4)), (960, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.save_progression(game.player)
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if save_b.collidepoint(event.pos):
                    game.save_progression(game.player)
                if load_b.collidepoint(event.pos):
                    game.load_progression(game.player)

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.player.gain_score()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


if __name__ == "__main__":
    game = Game()
    (width, height) = (1080, 720)
    size = (width, height)

    pygame.init()

    show_startscreen()
    main()
