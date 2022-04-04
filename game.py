import pygame
from player import Player
#import projectile
from osinteract import SaveSystem


class Game:
    def __init__(self):
        self.is_playing = False

        ### Player init
        self.all_player = pygame.sprite.Group()

        ### Monsters init
        self.all_monsters = pygame.sprite.Group()

        ### Projectiles init
        #self.fireball = None

        self.pressed = {}

        self.saves = SaveSystem()

    def create_player(self, playerID):
        self.player = Player(self, playerID)
        self.all_player.add(self.player)
        #self.fireball = projectile.Fireball(self.player)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.hp = self.player.max_hp
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.update_username(screen)
        self.player.update_score(screen)
        self.player.update_health_bar(screen)
        self.player.update_magic_points_bar(screen)

        # move
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width()-60:
            self.player.move_right()

        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 60:
            self.player.move_left()

        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height()-80:
            self.player.move_down()

        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 100:
            self.player.move_up()

    def save_progression(self, playerObject):
        if isinstance(playerObject, Player):
            self.saves.save(playerObject)

    def load_progression(self, playerObject):
        self.saves.load(playerObject)
