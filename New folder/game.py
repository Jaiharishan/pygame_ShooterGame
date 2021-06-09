import pygame
import math
import random
from pygame import mixer

#                                   ABOUT THE GAME

# IN THIS GAME A SURVIVOUR OF A GREAT CRISIS GOT STRUCK IN CENTRE
# OF 4 PATH WAYS WITH HIS TANK IN ALL THE 4 PATHWAYS ENEMY ARE SPAWNED INFINETLY
# IF THE GET DESTROYED BUT LUCKLY OUR HERO CAN TURN SOME OF THEM INTO ANGEL THUS
# RELEASING THEM FROM THE SPELL SO THAT THEY WILL HELP THE HERO TO DO HIS JOB
# THAT IS TO OBTAIN THE SEALING STONE FOR ALL 4 PORTALS AND SEAL THEM BUT ONLY
# THE HERO CAN DO THIS JOB ALSO ONCE THE TANK IS IN THAT POSITION IT CAN HEAL ITSELF
# THE ANGEL WILL HEAL THE TANK WHILE DAMAGING EVERYONE AROUND A FIXED RANGE

   # TODO: TO KNOW HOW TO HAVE HITPOINTS AND DAMAGE IN THE GAME FOR GIVING
   #       MORE THAN ONE ATTACK TO SEEM REALISTIC.
   # DONE

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 600))
game_playing = True
                                #DISLAY INFOS
# SCORE
score_font = pygame.font.SysFont('comicsans', 40)

# CENTER TANK
centertank_img_T = pygame.image.load('photos/centertank.png')
tank_x, tank_y, x_c, y_c, speed  = 368, 270, 0, 0, 2
hitpoints_tank = 100000

                                   # BULLETS
bullet_speed, damage_bullet = 24, 100
 #BULLETS UP
bullet_imgU = pygame.image.load('photos/tank_bullet_U.png')
bulletU_x, bulletU_y, bulletU_x_c , bulletU_y_c = 0 ,tank_y, bullet_speed, bullet_speed
bullet_stateU = "ready"
 #BULLETS DOWN
bullet_imgD = pygame.image.load('photos/tank_bullet_D.png')
bulletD_x,bulletD_y, bulletD_x_c , bulletD_y_c =0, tank_y, bullet_speed, bullet_speed
bullet_stateD = "ready"
#BULLETS LEFT
bullet_imgL = pygame.image.load('photos/tank_bullet_L.png')
bulletL_x,bulletL_y, bulletL_x_c , bulletL_y_c = 0, tank_y, bullet_speed, bullet_speed
bullet_stateL = "ready"
#BULLETS RIGHT
bullet_imgR = pygame.image.load('photos/tank_bullet_R.png')
bulletR_x,bulletR_y, bulletR_x_c , bulletR_y_c = 0, tank_y, bullet_speed, bullet_speed
bullet_stateR = "ready"

                                #MELEE ENEMIES
#ENEMIES IMAGE
enemyM_img = []

#ENEMIES FROM UP
enemyMU_x, enemyMU_y = [], []
#ENEMIES FROM DOWN
enemyMD_x, enemyMD_y = [], []
# ENEMIES FROM LEFT
enemyML_x, enemyML_y = [], []
#ENEMIES FROM RIGHT
enemyMR_x, enemyMR_y = [], []

#  ENEMY ATTRIBUTES
enemy_speed, enemy_damage = 0.32, 40
enemyM_x_c , enemyM_y_c, num_of_enemies, pix_EM =  enemy_speed,enemy_speed, 4, 64
hitpoints_enemyU = []
hitpoints_enemyD = []
hitpoints_enemyL = []
hitpoints_enemyR = []

for i in range(num_of_enemies):
    enemyM_img.append(pygame.image.load('photos/new_enemy.png'))
    enemyMU_x.append(random.randint(300, 500 - pix_EM))
    enemyMU_y.append(0)
    hitpoints_enemyU.append(256)

for i in range(num_of_enemies):
    enemyM_img.append(pygame.image.load('photos/new_enemy.png'))
    enemyMD_x.append(random.randint(300, 500 - pix_EM))
    enemyMD_y.append(800 - pix_EM)
    hitpoints_enemyD.append(256)

for i in range(num_of_enemies):
    enemyM_img.append(pygame.image.load('photos/new_enemy.png'))
    enemyML_x.append(0)
    enemyML_y.append(random.randint(225, 375 - pix_EM))
    hitpoints_enemyL.append(256)

for i in range(num_of_enemies):
    enemyM_img.append(pygame.image.load('photos/new_enemy.png'))
    enemyMR_x.append(800 - pix_EM)
    enemyMR_y.append(random.randint(225, 375 - pix_EM))
    hitpoints_enemyR.append(256)


                                #TOUGH ENEMIES

tough_enemyU_img, tough_enemyD_img, tough_enemyL_img, tough_enemyR_img = [], [], [], []

tough_enemyU_x, tough_enemyU_y, status_toughU = [], [], []
tough_enemyD_x, tough_enemyD_y, status_toughD = [], [], []
tough_enemyL_x, tough_enemyL_y, status_toughL = [], [], []
tough_enemyR_x, tough_enemyR_y, status_toughR = [], [], []
tough_enemy_speed, tough_enemy_damage = 0.32, 30
tough_enemy_x_c , tough_enemy_y_c = tough_enemy_speed, tough_enemy_speed
tough_enemy_HP = 1200
hitpoints_Tough_enemyU,hitpoints_Tough_enemyD,\
hitpoints_Tough_enemyL,hitpoints_Tough_enemyR, num_of_tough_enemies = [], [], [], [], 2
angel_speed, angel_damage, angel_heal, range_of_attack = 3.2, 0.4, 40, 90

for i in range(num_of_tough_enemies):
    tough_enemyU_img.append(pygame.image.load('photos/demon.png'))
    tough_enemyU_x.append(random.randint(300, 500 - pix_EM))
    tough_enemyU_y.append(0)
    status_toughU.append("enemy")    # NOW HE IS ENEMY
    hitpoints_Tough_enemyU.append(tough_enemy_HP)
angelU_x, angelU_y, angel_U_HP = tough_enemyU_x, tough_enemyU_y, hitpoints_Tough_enemyU

for i in range(num_of_tough_enemies):
    tough_enemyD_img.append(pygame.image.load('photos/demon.png'))
    tough_enemyD_x.append(random.randint(300, 500 - pix_EM))
    tough_enemyD_y.append(600)
    status_toughD.append("enemy")    # NOW HE IS ENEMY
    hitpoints_Tough_enemyD.append(tough_enemy_HP)
angelD_x, angelD_y, angel_D_HP = tough_enemyD_x, tough_enemyD_y, hitpoints_Tough_enemyD

for i in range(num_of_tough_enemies):
    tough_enemyL_img.append(pygame.image.load('photos/demon.png'))
    tough_enemyL_x.append(0)
    tough_enemyL_y.append(random.randint(225, 375 - pix_EM))
    status_toughL.append("enemy")    # NOW HE IS ENEMY
    hitpoints_Tough_enemyL.append(tough_enemy_HP)
angelL_x, angelL_y, angel_L_HP = tough_enemyL_x, tough_enemyL_y, hitpoints_Tough_enemyL

for i in range(num_of_tough_enemies):
    tough_enemyR_img.append(pygame.image.load('photos/demon.png'))
    tough_enemyR_x.append(600 - pix_EM)
    tough_enemyR_y.append(random.randint(225, 375 - pix_EM))
    status_toughR.append("enemy")    # NOW HE IS ENEMY
    hitpoints_Tough_enemyR.append(tough_enemy_HP)
angelR_x, angelR_y, angel_R_HP = tough_enemyR_x, tough_enemyR_y, hitpoints_Tough_enemyR


bomb = False
bomb_remaining = 5
bomb_damage = 270
bomb_radius = 100


tough_img = pygame.image.load('photos/demon.png')
enemy_img = pygame.image.load('photos/new_enemy.png')
bomb_img = pygame.image.load('photos/bomb.png')
                                    # FUNCTIONS


def show_player(x, y):
    if hitpoints_tank > 0:
        screen.blit(centertank_img_T, (x, y))


def show_score_enemy():
    screen.blit(enemy_img, (10, 10))
    if game_playing:
        score_txt = score_font.render(" :  " + str(score_E), True, (255, 255, 255))
        screen.blit(score_txt, (70, 30))


def show_score_tough_enemy():
    screen.blit(tough_img, (5, 80))
    if game_playing:
        score_txt = score_font.render(" :  " + str(score_TE), True, (255, 255, 255))
        screen.blit(score_txt, (70, 100))


def show_bomb():
    screen.blit(bomb_img, (650, 80))
    bomb_txt = score_font.render(" :  " + str(bomb_remaining), True, (255, 255, 255))
    screen.blit(bomb_txt, (710 , 100))


def fire_bullet(x, y, direction) :
    global bullet_stateU
    global bullet_stateD
    global bullet_stateL
    global bullet_stateR

    if direction == "U":
        bullet_stateU = "fire"
        screen.blit(bullet_imgU, (x + 16, y + 10))

    if direction == "D":
        bullet_stateD = "fire"
        screen.blit(bullet_imgD, (x + 16, y + 10))

    if direction == "L":
        bullet_stateL = "fire"
        screen.blit(bullet_imgL, (x + 16, y + 10))

    if direction == "R":
        bullet_stateR = "fire"
        screen.blit(bullet_imgR, (x + 16, y + 10))


def bomb_range(enemy_x, enemy_y):
    global tank_x
    global tank_y
    global bomb
    global bomb_radius
    dist = math.sqrt(math.pow((enemy_x) - tank_x, 2) +
                            math.pow((enemy_y) - tank_y, 2))
    if bomb_remaining > 0:
        if dist <= bomb_radius:
            return True
        else:
            False
    else:
        False


def enemyM(x, y, i) :
    screen.blit(enemyM_img[i], (x, y))


def tough_enemy(x, y, i, direction) :
    if direction == "U":
        screen.blit(tough_enemyU_img[i], (x, y))
    if direction == "D":
        screen.blit(tough_enemyD_img[i], (x, y))
    if direction == "L":
        screen.blit(tough_enemyL_img[i], (x, y))
    if direction == "R":
        screen.blit(tough_enemyR_img[i], (x, y))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    dist = math.sqrt(math.pow((enemy_x) - bullet_x, 2) +
                     math.pow((enemy_y) - bullet_y, 2))
    if dist < 14:
        return True
    else:
        False


def show_borders():
    pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 225), width=2)
    pygame.draw.line(screen, (255, 255, 255), (300, 375), (300, 600), width=2)

    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 225), width=2)
    pygame.draw.line(screen, (255, 255, 255), (500, 375), (500, 600), width=2)

    pygame.draw.line(screen, (255, 255, 255), (0, 225), (300, 225), width=2)
    pygame.draw.line(screen, (255, 255, 255), (500, 225), (800, 225), width=2)

    pygame.draw.line(screen, (255, 255, 255), (0, 375), (300, 375), width=2)
    pygame.draw.line(screen, (255, 255, 255), (500, 375), (800, 375), width=2)


def health_bar():
    global hitpoints_tank
    green_bar_height, green_bar_width = 25, 200
    pygame.draw.rect(screen, (0, 255, 0), (570, 20, green_bar_width, green_bar_height))
    pygame.draw.rect(screen, (0, 30, 0), (570, 20, green_bar_width, green_bar_height), 2)
    if hitpoints_tank > 0:
        value = hitpoints_tank // 500
    else:
        value = 0
    red_bar_height, red_bar_width = 25, 200
    pygame.draw.rect(screen, (255, 0, 0), (570 + value, 20, red_bar_width - value, red_bar_height))
    pygame.draw.rect(screen, (0, 30, 0), (570 + value, 20, green_bar_width- value, green_bar_height), 2)


def is_tank_collision(enemy_x, enemy_y):
    global tank_x
    global tank_y
    dist = math.sqrt(math.pow((enemy_x + 32) - (tank_x + 32), 2) +
                     math.pow((enemy_y + 32) - (tank_y + 32), 2))
    if dist < 24:
        return True
    else:
        False


def show_health(x, y, hp, type):
    global hitpoints_enemy
    global tough_enemy_HP

    width, height = 56, 6
    pygame.draw.rect(screen, (0, 255, 0), (x + 4, y + 5, width, height))
    pygame.draw.rect(screen, (0, 30, 0), (x + 4, y + 5, width, height) , 2)
    if type == "E":
        if hp > 0:
            value = hp // (hitpoints_enemy // width)
        else:
            value = 0

    if type == "TE":
        if hp > 0:
            value = hp // (tough_enemy_HP // width)
        else:
            value = 0
    pygame.draw.rect(screen, (0, 255, 0), (x + 4, y + 5, width, height))
    pygame.draw.rect(screen, (255, 0, 0), ((x + 4) + value, y + 5, width - value, height))


def if_angel_range(enemy_x, enemy_y, angel_x, angel_y):
    global range_of_attack
    dist = math.sqrt(math.pow(enemy_x - angel_x, 2) + math.pow(enemy_y - angel_y, 2))
    if dist <= range_of_attack:
        return True
    else:
        False


# SCORE SYSTEM
score_E, score_TE, points_M, points_T = 0, 0, 1, 5
hitpoints_enemy = 224

clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 60, 60))
    # BACKGROUND TO BE ADDED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_c += -speed
            if event.key == pygame.K_a:
                x_c += -speed
            if event.key == pygame.K_s:
                y_c += speed
            if event.key == pygame.K_d:
                x_c += speed

            if event.key == pygame.K_b:
                bomb = True


            if event.key == pygame.K_UP:
                if bullet_stateU == "ready":
                    bullet_sound = mixer.Sound('photos/laser.wav')
                    bullet_sound.play()
                    bulletU_x = tank_x
                    bulletU_y = tank_y
                    fire_bullet(bulletU_x, bulletU_y, 'U')

            if event.key == pygame.K_DOWN:
                if bullet_stateD == "ready":
                    bullet_sound = mixer.Sound('photos/laser.wav')
                    bullet_sound.play()
                    bulletD_x = tank_x
                    bulletD_y = tank_y
                    fire_bullet(bulletD_x, bulletD_y, 'D')

            if event.key == pygame.K_LEFT:
                if bullet_stateL == "ready":
                    bullet_sound = mixer.Sound('photos/laser.wav')
                    bullet_sound.play()
                    bulletL_x = tank_x
                    bulletL_y = tank_y
                    fire_bullet(bulletL_x, bulletL_y, 'L')

            if event.key == pygame.K_RIGHT:
                if bullet_stateL == "ready":
                    bullet_sound = mixer.Sound('photos/laser.wav')
                    bullet_sound.play()
                    bulletR_x = tank_x
                    bulletR_y = tank_y
                    fire_bullet(bulletR_x, bulletR_y, 'R')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a \
                    or event.key == pygame.K_s or event.key == pygame.K_d:
                x_c, y_c = 0, 0

    #CENTERTANK MOVEMENTS
    tank_x += x_c
    if tank_x < 300:
        tank_x = 300
    if tank_x > 500 - pix_EM:
        tank_x = 500 - pix_EM
    tank_y += y_c
    if tank_y < 225:
        tank_y = 225
    if tank_y > 375 - pix_EM:
        tank_y = 375 - pix_EM


                            # MELEE ENEMY MOVEMENTS
                                    # UP
    for i in range(num_of_enemies):

        enemyMU_y[i] += enemyM_y_c
        if enemyMU_y[i] > 300 - pix_EM:
            enemyMU_y[i] = 300 - pix_EM
        if enemyMU_y[i] < 0:
            enemyMU_y[i] = 0

        collisionU = is_collision(enemyMU_x[i], enemyMU_y[i], bulletU_x, bulletU_y)
        if collisionU:
            bulletU_x = tank_x
            if hitpoints_enemyU[i] > 0:
                hitpoints_enemyU[i] -= damage_bullet
            elif hitpoints_enemyU[i] <= 0:
                enemyMU_x[i] = random.randint(300, 500 - pix_EM)
                enemyMU_y[i] = 0
                hitpoints_enemyU[i] = 256
                score_E += points_M

        if is_tank_collision(enemyMU_x[i], enemyMU_y[i]):
            hitpoints_tank -= enemy_damage


        enemyM(enemyMU_x[i], enemyMU_y[i], i)
        show_health(enemyMU_x[i], enemyMU_y[i], hitpoints_enemyU[i], "E")

                                      # DOWN
    for i in range(num_of_enemies):

        enemyMD_y[i] -= enemyM_y_c
        if enemyMD_y[i] < 300:
            enemyMD_y[i] = 300
        if enemyMD_y[i] > 600 - pix_EM:
            enemyMD_y[i] = 600 - pix_EM

        collisionD = is_collision(enemyMD_x[i], enemyMD_y[i], bulletD_x, bulletD_y)
        if collisionD:
            bulletD_x = tank_x
            if hitpoints_enemyD[i] > 0:
                hitpoints_enemyD[i] -= damage_bullet
            elif hitpoints_enemyD[i] <= 0:
                enemyMD_x[i] = random.randint(300, 500 - pix_EM)
                enemyMD_y[i] = 600 - pix_EM
                hitpoints_enemyD[i] = 256
                score_E += points_M

        if is_tank_collision(enemyMD_x[i], enemyMD_y[i]):
            hitpoints_tank -= enemy_damage

        enemyM(enemyMD_x[i], enemyMD_y[i], i)
        show_health(enemyMD_x[i], enemyMD_y[i], hitpoints_enemyD[i], "E")

                                    # LEFT
    for i in range(num_of_enemies):

        enemyML_x[i] += enemyM_x_c
        if enemyML_x[i] > 400 - pix_EM:
            enemyML_x[i] = 400 - pix_EM
        if enemyML_x[i] < 0:
            enemyML_x[i] = 0

        collisionL = is_collision(enemyML_x[i], enemyML_y[i], bulletL_x, bulletL_y)
        if collisionL:
            bulletL_y = tank_y
            if hitpoints_enemyL[i] > 0:
                hitpoints_enemyL[i] -= damage_bullet
            elif hitpoints_enemyL[i] <= 0:
                enemyML_x[i] = 0
                enemyML_y[i] = random.randint(225, 375 - pix_EM)
                hitpoints_enemyL[i] = 256
                score_E += points_M

        if is_tank_collision(enemyML_x[i], enemyML_y[i]):
            hitpoints_tank -= enemy_damage


        enemyM(enemyML_x[i], enemyML_y[i], i)
        show_health(enemyML_x[i], enemyML_y[i], hitpoints_enemyL[i], "E")

                                    # RIGHT
    for i in range(num_of_enemies):

        enemyMR_x[i] -= enemyM_x_c
        if enemyMR_x[i] < 400:
            enemyMR_x[i] = 400
        if enemyMR_x[i] > 800 - pix_EM:
            enemyMR_x[i] = 800 - pix_EM

        collisionR = is_collision(enemyMR_x[i], enemyMR_y[i], bulletR_x, bulletR_y)
        if collisionR:
            bulletR_y = tank_y
            if hitpoints_enemyR[i] > 0:
                hitpoints_enemyR[i] -= damage_bullet
            elif hitpoints_enemyR[i] <= 0:
                enemyMR_x[i] = 800 - pix_EM
                enemyMR_y[i] = random.randint(225, 375 - pix_EM)
                hitpoints_enemyR[i] = 256
                score_E += points_M

        if is_tank_collision(enemyMR_x[i], enemyMR_y[i]):
            hitpoints_tank -= enemy_damage

        enemyM(enemyMR_x[i], enemyMR_y[i], i)
        show_health(enemyMR_x[i], enemyMR_y[i], hitpoints_enemyR[i], "E")

                               # TOUGH ENEMY MOVEMENT

                                    #UP

    for i in range(num_of_tough_enemies):
        tough_enemyU_y[i] += tough_enemy_y_c
        if tough_enemyU_y[i] > 225 - pix_EM:
            tough_enemyU_y[i] = 0
        if tough_enemyU_y[i] < 0:
            tough_enemyU_y[i] = 0

        collisionTU = is_collision(tough_enemyU_x[i], tough_enemyU_y[i],
                                            bulletU_x,    bulletU_y)
        if collisionTU:
            #ONLY IF HE IS ENEMY HE GETS DAMAGE
            if status_toughU[i] == "enemy":
                bulletU_x = tank_x
                if hitpoints_Tough_enemyU[i] > 0:
                    hitpoints_Tough_enemyU[i] -= damage_bullet
                else:
                    status_toughU[i] = "ally"
                    hitpoints_Tough_enemyU[i] = tough_enemy_HP
                    score_TE += points_T

        if status_toughU[i] == "enemy":
            if if_angel_range(tank_x, tank_y, tough_enemyU_x[i], tough_enemyU_y[i]):
                hitpoints_tank -= tough_enemy_damage



        if status_toughU[i] == "ally":
            tough_enemyU_img[i] = pygame.image.load('photos/angel.png')
            if angelU_y[i] < 220 - pix_EM:
                angelU_y[i] += angel_speed
            if angelU_y[i] > 220 - pix_EM:
                angelU_y[i] = 220 - pix_EM

            if angel_U_HP[i] > 0:
                pygame.draw.circle(screen, (255, 255, 255), (angelU_x[i] + 32, angelU_y[i] + 32),
                                   range_of_attack, 2)

                if if_angel_range(tank_x, tank_y, angelU_x[i], angelU_y[i]):
                    if hitpoints_tank < 100000:
                        hitpoints_tank += angel_heal
                for auto in range(num_of_enemies):
                    if if_angel_range(enemyMU_x[auto], enemyMU_y[auto], angelU_x[i], angelU_y[i]):
                        if hitpoints_enemyU[auto] > 0:
                            hitpoints_enemyU[auto] -= angel_damage

                        elif hitpoints_enemyU[auto] <= 0:
                            enemyMU_x[auto] = random.randint(300, 500 - pix_EM)
                            enemyMU_y[auto] = 0
                            hitpoints_enemyU[auto] = hitpoints_enemy
                            score_E += points_M


            for auto in range(num_of_enemies):
                if is_collision(enemyMU_x[auto], enemyMU_y[auto], angelU_x[i], angelU_y[i]):
                    if angel_U_HP[i] > 0:
                        angel_U_HP[i] -= (enemy_damage//3)

                    elif angel_U_HP[i] <= 0:
                        tough_enemyU_img[i] = pygame.image.load('photos/demon.png')
                        angelU_x[i], angelU_y[i], angel_U_HP[i] = tough_enemyU_x[i], tough_enemyU_y[i], hitpoints_Tough_enemyU[i]
                        hitpoints_Tough_enemyU[i] = tough_enemy_HP
                        tough_enemyU_x[i] = random.randint(300, 500 - pix_EM)
                        tough_enemyU_y[i] = 0
                        status_toughU[i] = "enemy"


        tough_enemy(tough_enemyU_x[i], tough_enemyU_y[i], i, "U")
        show_health(tough_enemyU_x[i], tough_enemyU_y[i], hitpoints_Tough_enemyU[i], "TE")


                                        # DOWN
    for i in range(num_of_tough_enemies):
        tough_enemyD_y[i] -= tough_enemy_y_c
        if tough_enemyD_y[i] < 375:
            tough_enemyD_y[i] = 600 - pix_EM
        if tough_enemyD_y[i] > 600 - pix_EM:
            tough_enemyD_y[i] = 600 - pix_EM

        collisionTD = is_collision(tough_enemyD_x[i], tough_enemyD_y[i],
                                   bulletD_x,    bulletD_y)
        if collisionTD:
            #ONLY IF HE IS ENEMY HE GETS DAMAGE
            if status_toughD[i] == "enemy":
                bulletD_x = tank_x
                if hitpoints_Tough_enemyD[i] > 0:
                    hitpoints_Tough_enemyD[i] -= damage_bullet
                else:
                    status_toughD[i] = "ally"
                    hitpoints_Tough_enemyD[i] = tough_enemy_HP
                    score_TE += points_T


        if status_toughD[i] == "ally":
            tough_enemyD_img[i] = pygame.image.load('photos/angel.png')
            if angelD_y[i] > 380:
                angelD_y[i] -= angel_speed
            if angelD_y[i] < 380:
                angelD_y[i] = 380

            if angel_D_HP[i] > 0:
                pygame.draw.circle(screen, (255, 255, 255), (angelD_x[i] + 32, angelD_y[i] + 32),
                                   range_of_attack, 2)

                if if_angel_range(tank_x, tank_y, angelD_x[i], angelD_y[i]):
                    if hitpoints_tank < 100000:
                        hitpoints_tank += angel_heal

                for auto in range(num_of_enemies):
                    if if_angel_range(enemyMD_x[auto], enemyMD_y[auto], angelD_x[i], angelD_y[i]):
                        if hitpoints_enemyD[auto] > 0:
                            hitpoints_enemyD[auto] -= angel_damage

                        elif hitpoints_enemyD[auto] <= 0:
                            enemyMD_x[auto] = random.randint(300, 500 - pix_EM)
                            enemyMD_y[auto] = 600 - pix_EM
                            hitpoints_enemyD[auto] = hitpoints_enemy
                            score_E += points_M

            for auto in range(num_of_enemies):
                if is_collision(enemyMD_x[auto], enemyMD_y[auto], angelD_x[i], angelD_y[i]):
                    if angel_D_HP[i] > 0:
                        angel_D_HP[i] -= (enemy_damage//3)

                    elif angel_D_HP[i] <= 0:
                        tough_enemyD_img[i] = pygame.image.load('photos/demon.png')
                        angelD_x[i], angelD_y[i], angel_D_HP[i] = tough_enemyD_x[i], tough_enemyD_y[i], hitpoints_Tough_enemyD[i]
                        hitpoints_Tough_enemyD[i] = tough_enemy_HP
                        tough_enemyD_x[i] = random.randint(300, 500 - pix_EM)
                        tough_enemyD_y[i] = 0
                        status_toughD[i] = "enemy"

        tough_enemy(tough_enemyD_x[i], tough_enemyD_y[i], i, 'D')
        show_health(tough_enemyD_x[i], tough_enemyD_y[i], hitpoints_Tough_enemyD[i], "TE")

                                #LEFT
    for i in range(num_of_tough_enemies):
        tough_enemyL_x[i] += tough_enemy_x_c
        if tough_enemyL_x[i] > 300 - pix_EM:
            tough_enemyL_x[i] = 0
        if tough_enemyL_x[i] < 0:
            tough_enemyL_x[i] = 0

        collisionTL = is_collision(tough_enemyL_x[i], tough_enemyL_y[i],
                                   bulletL_x,    bulletL_y)
        if collisionTL:
            if status_toughL[i] == "enemy":
                bulletL_y = tank_y
                if hitpoints_Tough_enemyL[i] > 0:
                    hitpoints_Tough_enemyL[i] -= damage_bullet
                elif hitpoints_Tough_enemyL[i] <= 0:
                    status_toughL[i] = "ally"
                    hitpoints_Tough_enemyL[i] = tough_enemy_HP
                    score_TE += points_T


        if status_toughL[i] == "ally":
            tough_enemyL_img[i] = pygame.image.load('photos/angel.png')
            if angelL_x[i] < 295 - pix_EM:
                angelL_x[i] += angel_speed
            if angelL_x[i] > 295 - pix_EM:
                angelL_x[i] = 295 - pix_EM

            if angel_L_HP[i] > 0:
                pygame.draw.circle(screen, (255, 255, 255), (angelL_x[i] + 32, angelL_y[i] + 32),
                                   range_of_attack, 2)

                if if_angel_range(tank_x, tank_y, angelL_x[i], angelL_y[i]):
                    if hitpoints_tank < 100000:
                        hitpoints_tank += angel_heal

                for auto in range(num_of_enemies):
                    if if_angel_range(enemyML_x[auto], enemyML_y[auto], angelL_x[i], angelL_y[i]):
                        if hitpoints_enemyL[auto] > 0:
                            hitpoints_enemyL[auto] -= angel_damage

                        elif hitpoints_enemyL[auto] <= 0:
                            enemyML_x[auto] = 0
                            enemyML_y[auto] = random.randint(225, 375 - pix_EM)
                            hitpoints_enemyL[auto] = hitpoints_enemy
                            score_E += points_M

            for auto in range(num_of_enemies):
                if is_collision(enemyML_x[auto], enemyML_y[auto], angelL_x[i], angelL_y[i]):
                    if angel_L_HP[i] > 0:
                        angel_L_HP[i] -= (enemy_damage//3)

                    elif angel_L_HP[i] <= 0:
                        tough_enemyL_img[i] = pygame.image.load('photos/demon.png')
                        angelL_x[i], angelL_y[i], angel_L_HP[i] = tough_enemyL_x[i], tough_enemyL_y[i], hitpoints_Tough_enemyL[i]
                        hitpoints_Tough_enemyL[i] = tough_enemy_HP
                        tough_enemyL_x[i] = 0
                        tough_enemyL_y[i] = random.randint(225, 375 - pix_EM)
                        status_toughL[i] = "enemy"

        tough_enemy(tough_enemyL_x[i], tough_enemyL_y[i], i, "L")
        show_health(tough_enemyL_x[i], tough_enemyL_y[i], hitpoints_Tough_enemyL[i], "TE")


                                #RIGHT
    for i in range(num_of_tough_enemies):
        tough_enemyR_x[i] -= tough_enemy_x_c
        if tough_enemyR_x[i] > 800 - pix_EM:
            tough_enemyR_x[i] = 800 - pix_EM
        if tough_enemyR_x[i] < 500:
            tough_enemyR_x[i] = 800 - pix_EM

        collisionTR = is_collision(tough_enemyR_x[i], tough_enemyR_y[i],
                                   bulletR_x, bulletR_y)
        if collisionTR:
            if status_toughR[i] == "enemy":
                bulletR_y = tank_y
                if hitpoints_Tough_enemyR[i] > 0:
                    hitpoints_Tough_enemyR[i] -= damage_bullet
                elif hitpoints_Tough_enemyR[i] <= 0:
                    status_toughR[i] = "ally"
                    hitpoints_Tough_enemyR[i] = tough_enemy_HP
                    score_TE += points_T


        if status_toughR[i] == "ally":
            tough_enemyR_img[i] = pygame.image.load('photos/angel.png')
            if angelR_x[i] > 505:
                angelR_x[i] -= angel_speed
            if angelR_x[i] < 505:
                angelR_x[i] = 505

            if angel_R_HP[i] > 0:
                pygame.draw.circle(screen, (255, 255, 255), (angelR_x[i] + 32, angelR_y[i] + 32),
                                   range_of_attack, 2)

                if if_angel_range(tank_x, tank_y, angelR_x[i], angelR_y[i]):
                    if hitpoints_tank < 100000:
                        hitpoints_tank += angel_heal

                for auto in range(num_of_enemies):
                    if if_angel_range(enemyMR_x[auto], enemyMR_y[auto], angelR_x[i], angelR_y[i]):
                        if hitpoints_enemyR[auto] > 0:
                            hitpoints_enemyR[auto] -= angel_damage

                        elif hitpoints_enemyR[auto] <= 0:
                            enemyMR_x[auto] = 800 - pix_EM
                            enemyMR_y[auto] = random.randint(225, 375 - pix_EM)
                            hitpoints_enemyR[auto] = hitpoints_enemy
                            score_E += points_M

            for auto in range(num_of_enemies):
                if is_collision(enemyMR_x[auto], enemyMR_y[auto], angelR_x[i], angelR_y[i]):
                    if angel_R_HP[i] > 0:
                        angel_R_HP[i] -= (enemy_damage//3)

                    elif angel_R_HP[i] <= 0:
                        tough_enemyR_img[i] = pygame.image.load('photos/demon.png')
                        angelR_x[i], angelR_y[i], angel_R_HP[i] = tough_enemyR_x[i], tough_enemyR_y[i], hitpoints_Tough_enemyR[i]
                        hitpoints_Tough_enemyR[i] = tough_enemy_HP
                        tough_enemyR_x[i] = 0
                        tough_enemyR_y[i] = random.randint(225, 375 - pix_EM)
                        status_toughR[i] = "enemy"

        tough_enemy(tough_enemyR_x[i], tough_enemyR_y[i], i, "R")
        show_health(tough_enemyR_x[i], tough_enemyR_y[i], hitpoints_Tough_enemyR[i], "TE")

                              #BULLET MOVEMENTS


#BLASTING
    if bomb:
        if bomb_remaining > 0:
            pygame.draw.circle(screen, (255, 255, 255), (tank_x + 32, tank_y + 32),
                           bomb_radius, 2)

            for blast in range(num_of_enemies):
                if bomb_range(enemyMU_x[blast], enemyMU_y[blast]):
                    hitpoints_enemyU[blast] -= bomb_damage
                    if hitpoints_enemyU[blast] < 0:
                        enemyMU_x[blast] = random.randint(300, 500 - pix_EM)
                        enemyMU_y[blast] = 0
                        hitpoints_enemyU[blast] = hitpoints_enemy
                        score_E += points_M

                    bomb = False
                if bomb_range(enemyMD_x[blast], enemyMD_y[blast]):
                    hitpoints_enemyD[blast] -= bomb_damage
                    if hitpoints_enemyD[blast] < 0:
                        enemyMD_x[blast] = random.randint(300, 500 - pix_EM)
                        enemyMD_y[blast] = 600 - pix_EM
                        hitpoints_enemyD[blast] = hitpoints_enemy
                        score_E += points_M
                    bomb = False
                if bomb_range(enemyML_x[blast], enemyML_y[blast]):
                    hitpoints_enemyL[blast] -= bomb_damage
                    if hitpoints_enemyL[blast] < 0:
                        enemyML_x[blast] = 0
                        enemyML_y[blast] = random.randint(225, 375 - pix_EM)
                        hitpoints_enemyL[blast] = hitpoints_enemy
                        score_E += points_M
                    bomb = False
                if bomb_range(enemyMR_x[blast], enemyMR_y[blast]):
                    hitpoints_enemyR[blast] -= bomb_damage
                    if hitpoints_enemyR[blast] < 0:
                        enemyMR_x[blast] = 800 - pix_EM
                        enemyMR_y[blast] = random.randint(225, 375 - pix_EM)
                        hitpoints_enemyR[blast] = hitpoints_enemy
                        score_E += points_M
                    bomb = False
            bomb_remaining -= 1

    # UPWARD BULLET
    if bulletU_y < 0:
        bulletU_y = tank_y
        bullet_stateU = "ready"
    if bullet_stateU == "fire":
        fire_bullet(bulletU_x, bulletU_y, 'U')
        bulletU_y -= bulletU_y_c
    # DOWNWARD BULLET
    if bulletD_y > 600 - 32:
        bulletD_y = tank_y
        bullet_stateD = "ready"
    if bullet_stateD == "fire":
        fire_bullet(bulletD_x, bulletD_y, 'D')
        bulletD_y += bulletD_y_c
    # LEFTWARD BULLET
    if bulletL_x < 0:
        bulletL_x = tank_x
        bullet_stateL = "ready"
    if bullet_stateL == "fire":
        fire_bullet(bulletL_x, bulletL_y, 'L')
        bulletL_x -= bulletL_x_c
    # RIGHTWARD BULLET
    if bulletR_x > 800 - 32:
        bulletR_x = tank_x
        bullet_stateR = "ready"
    if bullet_stateR == "fire":
        fire_bullet(bulletR_x, bulletR_y, 'R')
        bulletR_x += bulletR_x_c


    show_player(tank_x, tank_y)
    show_score_enemy()
    show_score_tough_enemy()
    show_bomb()
    show_borders()
    health_bar()
    pygame.display.update()
    # 60 FPS
    clock.tick(60)
