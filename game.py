from player import *


class Game:
    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.hp = self.player.max_hp
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        # move
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width()-60:

            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 60:

            self.player.move_left()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height()-80:

            self.player.move_down()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 100:

            self.player.move_up()


