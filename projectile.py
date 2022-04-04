import pygame

import player


class Fireball(pygame.sprite.Sprite):
    def __init__(self, player: player.Player):
        super().__init__()
        self.player = player
        self.path = "assets/projectile/Projectile-0.png"
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()


    def remove(self):
        self.player.all_projectiles.remove(self)

    def shoot_up(self):
        self.image = pygame.image.load(self.path)
        for i in range(self.player.range):
            self.rect.y -= self.player.shot_speed

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        self.remove()

    def shoot_right(self):
        self.image = pygame.image.load(self.path)
        for i in range(self.player.range):
            self.rect.x += self.player.shot_speed

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        self.remove()

    def shoot_left(self):
        self.image = pygame.image.load(self.path)
        for i in range(self.player.range):
            self.rect.x -= self.player.shot_speed

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        self.remove()

    def shoot_down(self):
        self.image = pygame.image.load(self.path)
        for i in range(self.player.range):
            self.rect.y += self.player.shot_speed

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        self.remove()

