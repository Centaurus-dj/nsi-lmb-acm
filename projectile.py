import pygame

import player


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, img_path):
        super().__init__()
        self.player = player
        self.path = img_path

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


class Fireball(Projectile):
    def __init__(self, player):
        super().__init__(player, "assets/projectile/Projectile-0.png")
