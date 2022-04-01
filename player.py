#import pygame
from projectile import *
#import time


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 10
        self.max_hp = 10
        self.attack = 1
        self.speed = 1
        self.range = 10
        self.shot_speed = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/mage/mage-F0.png')
        self.skin = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.hp - amount > amount:
            self.hp -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [30, 30, self.max_hp * 10, 8])
        pygame.draw.rect(surface, (111, 210, 46), [30, 30, self.hp*10, 8])

    def skin_update(self):
        ... ### Not implemented yet
    """
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    """
    def move_right(self):
        self.image = pygame.image.load('assets/mage/mage-R0.png')
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed
        self.image = pygame.image.load('assets/mage/mage-L0.png')

    def move_up(self):
        self.image = pygame.image.load('assets/mage/mage-D0.png')
        self.rect.y -= self.speed

    def move_down(self):
        self.image = pygame.image.load('assets/mage/mage-F0.png')
        self.rect.y += self.speed
