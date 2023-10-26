import pygame
import random


class Player:
    def __init__(self, x, y, flipped, control):
        # Var

        self.back_speed = back_speed
        self.speed = player_speed
        self.health = player_health

        # Items

        self.c_images = []
        self.n_images = []
        self.damaged = []
        self.index = 0
        self.count = 0
        self.cooldown = 0
        self.dis_x = 0
        self.dis_y = 0
        self.dir_x = 0
        self.dir_y = 0
        self.time_out_x = 0
        self.time_out_y = 0
        self.shot = False
        self.attacked = False
        self.control = control
        self.flip = flipped

        player_image = pygame.image.load('media\DurrrSpaceShip.png')
        player_damaged = pygame.image.load('media\DurrrSpaceShip(1).png')
        if self.flip:
            player_image = pygame.transform.flip(player_image, False, True)
            player_damaged = pygame.transform.flip(player_damaged, False, True)

        self.n_images.append(player_image)
        self.damaged.append(player_damaged)

        self.c_images = self.n_images

        self.image = self.c_images[self.index]
        self.hitbox = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox.centerx = x
        self.hitbox.centery = y

    def update(self):
        dx = 0
        dy = 0
        dh = 0
        self.count -= 1
        self.cooldown += 1

        # Controls

        key = pygame.key.get_pressed()

        if self.control == "arrows":
            if key[pygame.K_DOWN]:
                dy += self.back_speed

            if key[pygame.K_LEFT]:
                dx -= self.speed

            if key[pygame.K_RIGHT]:
                dx += self.speed

            if key[pygame.K_UP]:
                dy -= self.speed

            if key[pygame.K_SLASH]:
                if not self.shot:
                    if self.cooldown >= shot_cooldown:
                        if not self.flip:
                            laser = Bullet(player_1.hitbox.centerx, player_1.hitbox.top, True)
                            bullets.append(laser)
                        else:
                            laser = Bullet(player_2.hitbox.centerx, player_2.hitbox.bottom, False)
                            enemy_bullets.append(laser)
                        self.cooldown = 0

            if not key[pygame.K_SPACE]:
                self.shot = False

        elif self.control == "wasd":
            if key[pygame.K_s]:
                if not self.flip:
                    dy += self.back_speed
                else:
                    dy += self.speed

            if key[pygame.K_w]:
                if not self.flip:
                    dy -= self.speed
                else:
                    dy -= self.back_speed

            if key[pygame.K_a]:
                dx -= self.speed

            if key[pygame.K_d]:
                dx += self.speed

            if key[pygame.K_SPACE]:
                if not self.shot:
                    if self.cooldown >= shot_cooldown:
                        if not self.flip:
                            laser = Bullet(player_1.hitbox.centerx, player_1.hitbox.top, True)
                            bullets.append(laser)
                        else:
                            laser = Bullet(player_2.hitbox.centerx, player_2.hitbox.bottom, False)
                            enemy_bullets.append(laser)
                        self.cooldown = 0

            if not key[pygame.K_SPACE]:
                self.shot = False

        else:
            if self.dis_x <= 0:
                self.dir_x = random.randint(0, 1)
                self.dis_x = random.randint(50, 100)
                if self.hitbox.right + self.dis_x >= 11 * X/12 and self.dir_x:
                    self.dir_x = 0
                if self.hitbox.left - self.dis_x <= X/12 and not self.dir_x:
                    self.dir_x = 1
            if self.dir_x:
                dx += self.speed
                self.dis_x -= dx
            else:
                dx -= self.speed
                self.dis_x += dx

            if self.dis_y <= 0:
                self.dir_y = random.randint(0, 1)
                self.dis_y = random.randint(10, 30)
                if self.hitbox.bottom + self.dis_y >= Y/2 and self.dir_y:
                    self.dir_y = 0
            if self.dir_y:
                dy += self.speed
                self.dis_y -= dy
            else:
                dy -= self.back_speed
                self.dis_y += dy

            if random.randint(0, 4) == 0:
                if self.cooldown >= shot_cooldown:
                    laser = Bullet(AI_char.hitbox.centerx, AI_char.hitbox.bottom, False)
                    enemy_bullets.append(laser)
                    self.cooldown = 0

        # Bounds

        if self.hitbox.left + dx <= -self.speed:
            dx = 0
        if self.hitbox.right + dx >= X + self.speed:
            dx = 0
        if self.hitbox.top + dy <= -self.speed:
            dy = 0
        if self.hitbox.bottom + dy >= Y + self.speed:
            dy = 0

        # Collisions

        if not self.flip and _2_player:
            if player_2.hitbox.colliderect(self.hitbox.x + dx, self.hitbox.y, self.width, self.height):
                dx = 0
            if player_2.hitbox.colliderect(self.hitbox.x, self.hitbox.y + dy, self.width, self.height):
                dy = 0
        elif not self.flip and not _2_player:
            if AI_char.hitbox.colliderect(self.hitbox.x + dx, self.hitbox.y, self.width, self.height):
                dx = 0
                self.dir_x = 0
                self.dis_x = 0
                self.time_out_x = 0
            if AI_char.hitbox.colliderect(self.hitbox.x, self.hitbox.y + dy, self.width, self.height):
                dy = 0
                self.dir_y = 0
                self.dis_y = 0
                self.time_out_y = 0

        else:
            if player_1.hitbox.colliderect(self.hitbox.x + dx, self.hitbox.y, self.width, self.height):
                dx = 0
            if player_1.hitbox.colliderect(self.hitbox.x, self.hitbox.y + dy, self.width, self.height):
                dy = 0

        if not self.flip:
            for proj in enemy_bullets:
                if not proj.bullet_hit and not proj.hit:
                    if proj.hitbox.colliderect(self.hitbox):
                        dh -= bullet_damage
                        proj.hit = True
                        self.attacked = True
        else:
            for proj in bullets:
                if not proj.bullet_hit and not proj.hit:
                    if proj.hitbox.colliderect(self.hitbox):
                        dh -= bullet_damage
                        proj.hit = True
                        self.attacked = True

        # Changes

        self.hitbox.centerx += dx
        self.hitbox.centery += dy
        self.health += dh

        # Sprites

        if self.count <= 0:
            if self.attacked:
                self.c_images = self.damaged
                self.attacked = False
                self.count = i_frames
            else:
                self.c_images = self.n_images

        self.image = self.c_images[self.index]

        # Output

        display.blit(self.image, self.hitbox)
        if hitbox:
            pygame.draw.rect(display, (255, 255, 255), self.hitbox, 5)


class Bullet:
    def __init__(self, x, y, from_player):
        self.hit = False
        self.bullet_hit = False
        self.from_player = from_player
        self.count = 0
        self.index = 0
        self.c_images = []
        self.n_images = []
        self.e_images = []
        if from_player:
            self.bullet_speed = -20
            image = pygame.image.load('media\Player Bullet.png')
        else:
            self.bullet_speed = 20
            image = pygame.transform.flip(pygame.image.load('media\Enemy Bullet.png'), False, True)

        exp0 = pygame.image.load('media\Exp\F0.png')
        exp1 = pygame.image.load('media\Exp\F1.png')
        exp2 = pygame.image.load('media\Exp\F2.png')
        exp3 = pygame.image.load('media\Exp\F3.png')
        exp4 = pygame.image.load('media\Exp\F4.png')
        exp5 = pygame.image.load('media\Exp\F5.png')
        exp6 = pygame.image.load('media\Exp\F6.png')
        exp7 = pygame.image.load('media\Exp\F7.png')
        exp8 = pygame.image.load('media\Exp\F8.png')
        exp9 = pygame.image.load('media\Exp\F9.png')
        exp10 = pygame.image.load('media\Exp\F10.png')
        exp11 = pygame.image.load('media\Exp\F11.png')

        self.e_images.append(exp0)
        self.e_images.append(exp1)
        self.e_images.append(exp2)
        self.e_images.append(exp3)
        self.e_images.append(exp4)
        self.e_images.append(exp5)
        self.e_images.append(exp6)
        self.e_images.append(exp7)
        self.e_images.append(exp8)
        self.e_images.append(exp9)
        self.e_images.append(exp10)
        self.e_images.append(exp11)

        self.n_images.append(image)
        self.image = self.n_images[self.index]
        self.c_images = self.n_images

        self.hitbox = self.image.get_rect()
        self.hitbox.centerx = x
        self.hitbox.centery = y
        self.e_hitbox = exp0.get_rect()
        self.e_hitbox.centerx = self.hitbox.centerx
        self.e_hitbox.centery = self.hitbox.centery

    def update(self):
        update_cooldown = 2

        self.hitbox.centery += self.bullet_speed
        if sounds:
            laser_shot.play()

        if not self.hit and not self.bullet_hit:
            if self.from_player:
                for proj in enemy_bullets:
                    if not proj.bullet_hit and not proj.hit:
                        if proj.hitbox.colliderect(self.hitbox):
                            self.bullet_hit = True
                            proj.bullet_hit = True
            else:
                for proj in bullets:
                    if not proj.bullet_hit and not proj.hit:
                        if proj.hitbox.colliderect(self.hitbox):
                            self.bullet_hit = True
                            proj.bullet_hit = True

        if self.hit or self.bullet_hit:
            self.e_hitbox.centerx = self.hitbox.centerx
            self.e_hitbox.centery = self.hitbox.centery
            self.hitbox = self.e_hitbox
            self.bullet_speed = 0
            self.c_images = self.e_images
            if self.hit:
                if self.from_player and _2_player:
                    self.hitbox.centerx = player_2.hitbox.centerx
                    self.hitbox.centery = player_2.hitbox.centery
                elif self.from_player and not _2_player:
                    self.hitbox.centerx = AI_char.hitbox.centerx
                    self.hitbox.centery = AI_char.hitbox.centery
                else:
                    self.hitbox.centerx = player_1.hitbox.centerx
                    self.hitbox.centery = player_1.hitbox.centery
            if self.count == update_cooldown:
                if self.index < len(self.c_images) - 1:
                    self.index += 1
                else:
                    self.index = 0
                self.count = 0
            else:
                self.count += 1
        self.image = self.c_images[self.index]
        display.blit(self.image, self.hitbox)


class HP_Bar:
    def __init__(self, player, x, y):
        self.health = player_health
        self.flip = player.flip
        if self.flip:
            self.colour = (220, 0, 0)
        else:
            self.colour = (0, 0, 220)
        self.border = pygame.image.load('media\HP bar.png')

        self.hitbox = self.border.get_rect()
        self.hitbox.centerx = x
        self.hitbox.centery = y

    def update(self):
        if self.flip:
            if _2_player:
                self.health = player_2.health
            else:
                self.health = AI_char.health
            k = 1
        else:
            self.health = player_1.health
            k = 54
        ratio = self.health / player_health

        display.fill((50, 50, 50), ((self.hitbox.left + 3, self.hitbox.top), (self.hitbox.right - 16, self.hitbox.bottom - 10 * k)))
        display.fill(self.colour, ((self.hitbox.left + 3, self.hitbox.top), (self.hitbox.right * ratio - 16, self.hitbox.bottom - 10 * k)))
        display.blit(self.border, self.hitbox)


class Button:
    def __init__(self, light_image, dark_image, x, y):
        self.light = light_image
        self.dark = dark_image
        self.image = self.light
        self.hitbox = self.image.get_rect()
        self.hitbox.centerx = x
        self.hitbox.centery = y
        self.output = False
        self.switchon = False
        self.new = True

    def update(self):
        self.image = self.light
        self.output = False

        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.image = self.dark
            if pygame.mouse.get_pressed()[0]:
                self.output = True

        display.blit(self.image, self.hitbox)

    def switch(self):
        if not pygame.mouse.get_pressed()[0]:
            self.new = True
        self.image = self.light
        if pygame.mouse.get_pressed()[0] and self.hitbox.collidepoint(pygame.mouse.get_pos()) and self.new:
            self.switchon = not self.switchon
            self.new = False

        if self.switchon:
            self.image = self.dark

        display.blit(self.image, self.hitbox)


def main_menu_display():
    display.blit(main_menu, (0, 0))


def refresh():
    player_1.health = player_health
    player_2.health = player_health
    AI_char.health = player_health
    player_1.c_images = player_1.n_images
    player_2.c_images = player_2.n_images
    AI_char.c_images = AI_char.n_images
    for _ in bullets:
        del _
    for _ in enemy_bullets:
        del _
    bullets.clear()
    enemy_bullets.clear()


pygame.init()

X = 600
Y = 600

fps = pygame.time.Clock()

spawn = (X/2, 420)

game_speed = 30
i_frames = 35
shot_cooldown = 7
win_card = False
player_1_won = False
time_out_won = 3000
laser_mode = True
Playing = False
hitbox = False
_2_player = False
sounds = True
player_speed = 10
back_speed = 5
background_speed = 12
back_y_1 = -Y
back_y_2 = 0
player_health = 100
bullet_damage = 5

background_list = []

bullets = []
enemy_bullets = []

# Images
play_image_light = pygame.image.load('media/Play.png')
play_image_dark = pygame.image.load('media/Play_1.png')
_1_P = pygame.image.load('media/1 P.png')
_2_P = pygame.image.load('media/2 P.png')
_1_P_acc = pygame.image.load('media/1 P Dark.png')
_2_P_acc = pygame.image.load('media/2 P Dark.png')
exit_l = pygame.image.load('media/Exit.png')
exit_d = pygame.image.load('media/Exit Dark.png')
muted = pygame.image.load('media/muted.png')
unmuted = pygame.image.load('media/unmuted.png')
blue_wins = pygame.image.load('media/blue won.png')
red_wins = pygame.image.load('media/red won.png')

background = pygame.image.load('media\Stars.jpg!d')
main_menu = pygame.image.load('media/main menu.png')
background = pygame.transform.scale(background, (X, Y))
main_menu = pygame.transform.scale(main_menu, (X, Y))
laser_shot = pygame.mixer.Sound('media\Laser.sound.mp3')

# Resize
play_image_light = pygame.transform.scale(play_image_light, (240, 100))
play_image_dark = pygame.transform.scale(play_image_dark, (240, 100))
muted = pygame.transform.scale(muted, (50, 50))
unmuted = pygame.transform.scale(unmuted, (50, 50))
exit_l = pygame.transform.scale(exit_l, (200, 100))
exit_d = pygame.transform.scale(exit_d, (200, 100))
blue_wins = pygame.transform.scale(blue_wins, (400, 300))
red_wins = pygame.transform.scale(red_wins, (400, 300))

# Buttons

play_button = Button(play_image_light, play_image_dark, 300, 250)
exit_button = Button(exit_l, exit_d, 300, 490)
mute_button = Button(unmuted, muted, 550, 50)
_1_P_switch = Button(_1_P, _1_P_acc, 240, 370)
_2_P_switch = Button(_2_P, _2_P_acc, 360, 370)
_1_P_switch.switchon = True
mute_button.switchon = False
acc_pb = False

player_1 = Player(spawn[0], spawn[1], False, 'arrows')
player_2 = Player(-200, -200, True, 'wasd')
AI_char = Player(-200, -200, True, 'nil')

hp_1 = HP_Bar(player_1, 110, Y - 35)
hp_2 = HP_Bar(player_2, 110, 35)
hp_AI = HP_Bar(AI_char, 110, 35)


# Screen

display = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Space Shooter')


while True:
    main_menu_display()

    _1_P_switch.switch()
    if _1_P_switch.switchon:
        _2_player = False
        _2_P_switch.switchon = False
    else:
        _2_player = True
        _2_P_switch.switchon = True

    _2_P_switch.switch()
    if _2_P_switch.switchon:
        _2_player = True
        _1_P_switch.switchon = False
    else:
        _2_player = False
        _1_P_switch.switchon = True

    play_button.update()
    if play_button.output or acc_pb:
        acc_pb = False
        refresh()
        player_1.hitbox.center = (spawn[0], spawn[1])

        player_2.hitbox.center = (-200, -200)
        AI_char.hitbox.center = (-200, -200)
        if _2_player:
            player_2.hitbox.center = (spawn[0], Y - spawn[1])
        else:
            AI_char.hitbox.center = (spawn[0], Y - spawn[1])
        Playing = True

    exit_button.update()
    if exit_button.output:
        pygame.quit()
        quit()

    mute_button.switch()
    if mute_button.switchon:
        sounds = False
    else:
        sounds = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                acc_pb = True
            if event.key == pygame.K_m:
                mute_button.switchon = not mute_button.switchon

    while Playing:
        back_y_1 += background_speed
        back_y_2 += background_speed
        if back_y_1 >= 0:
            back_y_1 = -Y
        if back_y_2 >= Y:
            back_y_2 = 0
        display.blit(background, (0, back_y_1))
        display.blit(background, (0, back_y_2))

        if player_1.health <= 0:
            player_1_won = False
            win_card = True
        if player_2.health <= 0:
            player_1_won = True
            win_card = True
        if AI_char.health <= 0:
            player_1_won = True
            win_card = True

        player_1.update()
        hp_1.update()
        if _2_player:
            player_2.update()
            hp_2.update()
        else:
            AI_char.update()
            hp_AI.update()

        mute_button.switch()
        if mute_button.switchon:
            sounds = False
        else:
            sounds = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Playing = False
                if event.key == pygame.K_m:
                    mute_button.switchon = not mute_button.switchon

        for bullet in bullets:
            bullet.update()
            if bullet.index == 11:
                bullets.remove(bullet)
            if bullet.hitbox.bottom <= 0:
                bullets.remove(bullet)

        for bullet in enemy_bullets:
            bullet.update()
            if bullet.index >= 11:
                enemy_bullets.remove(bullet)
            if bullet.hitbox.top >= Y:
                enemy_bullets.remove(bullet)

        while win_card:
            Playing = False
            if player_1_won:
                display.blit(blue_wins, (100, 150))
            else:
                display.blit(red_wins, (100, 150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_card = False
                if event.type == pygame.KEYDOWN:
                    win_card = False

            fps.tick(game_speed)
            pygame.display.update()

        fps.tick(game_speed)
        pygame.display.update()

    fps.tick(game_speed)
    pygame.display.update()
