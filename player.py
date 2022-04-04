import pygame
#import time


class Player(pygame.sprite.Sprite):
    def __init__(self, game, id):
        super().__init__()
        self.id = id
        self.game = game
        self.hp = 8
        self.max_hp = 10
        self.attack = 1
        self.speed = 3
        self.range = 10
        self.shot_speed = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/mage/mage-F0.png')
        self.skin = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.score = 0

    def gain_score(self):
        self.score += 1

    def set_score(self, score):
        self.score = score

    def damage(self, amount):
        if self.hp - amount > amount:
            self.hp -= amount
        else:
            self.game.game_over()

    def update_username(self, surface):
        pygame.font.init()
        font = pygame.font.Font("fonts/Roboto-Regular.ttf", 30)
        surface.blit(font.render(self.id, True, "white"), (10, 5))
        pygame.font.quit()

    def update_score(self, surface):
        pygame.font.init()
        font = pygame.font.Font("fonts/Roboto-Regular.ttf", 24)
        surface.blit(font.render(str(self.score), True, "white"), (450, 10))
        pygame.font.quit()

    def update_health_bar(self, surface):
        pygame.font.init()
        font = pygame.font.Font("fonts/Roboto-Regular.ttf", 24)
        surface.blit(font.render("HP: ", True, "white"), (10, 30))
        pygame.draw.rect(surface, (60, 63, 60), [50, 43, self.max_hp * 10, 10], width=5)
        pygame.draw.rect(surface, (111, 210, 46), [50, 43, self.hp*10, 10], width=5)
        pygame.font.quit()

    def update_magic_points_bar(self, surface):
        pygame.font.init()
        font = pygame.font.Font("fonts/Roboto-Regular.ttf", 24)
        surface.blit(font.render("MP: ", True, "white"), (8, 50))
        pygame.draw.rect(surface, (60, 63, 60), [50, 63, self.max_hp * 10, 10], width=5)
        pygame.draw.rect(surface, (9, 149, 204), [50, 63, self.hp*10, 10], width=5)
        pygame.font.quit()

    def skin_update(self):
        ... ### Not implemented yet

    # def launch_projectile(self):
    #     self.all_projectiles.add(self.game.fireball)

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
