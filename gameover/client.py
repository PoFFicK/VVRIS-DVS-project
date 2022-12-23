
# client 
from msilib.schema import Font
import socket
import pygame
import sys
import random
server_ip = '192.168.1.39'
SIZE = (800, 700)
TITLE = "hardest game analog"
PLAYER_SIZE = 10
FPS = 60
global count 
global win
count = 0
count2 = 0
global next_level
next_level = False
gamerunning_1 = False
gamerunning_2 = False
win = '5'
#server_ip = 'localhost'
''' окно '''
window = pygame.display.set_mode((800, 700))
colors={'0':(255,255,0),'1':(255,0,0),'2':(0,255,0),'3':(0,255,255),'4':(128,0,128)}
color_me = colors['0']
color_2 = colors['2']
''' холст '''
screen = pygame.Surface((800, 700))
''' строка состояния '''
info_string = pygame.Surface((800, 30))
START = (30, 30)
TRAPS = [(770, 560, 20, 30)]
         #(770, 10, 20, 30)]
TRAP_SIZE = 10
WALLS2 = [
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 590, 800, 10],
    [40, 100, 100, 5],
    [40, 200, 160, 5],
    [10, 280, 160, 5],
    [0, 100, 180, 5],
    [30, 390, 390, 5],
    [0, 500, 100, 5],
    [70, 440, 400, 5],
    [70, 540, 100, 5],
    [200, 0, 5, 370],
    [270, 40, 5, 350],
    [120, 220, 5, 40],
    [400, 40, 5, 300],
    [500, 0, 5, 400],
    [600, 40, 5, 400],
    [700, 0, 5, 400],
    [170, 390, 5, 210],
    [300, 500, 5, 60],
    [400, 470, 5, 130],
    [500, 500, 5, 60],
    [600, 500, 5, 100],
    [700, 500, 5, 100],
    [200, 100, 5, 100],
    [200, 200, 5, 100],
    [200, 500, 300, 5],
    [70, 0, 5, 60],
    [120, 120, 5, 60],
    [300, 40, 170, 5],
    [320, 180, 150, 5],
    [510, 420, 370, 5]
]
WALLS = [
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 590, 800, 10],
    [390, 280, 260, 5],
    [10, 280, 260, 5],
    [550, 435, 5, 100],
    [485, 225, 5, 100],
    [550, 535, 5, 60],
    [500, 435, 5, 120],
    [450, 140, 5, 120],
    [230, 340, 5, 120],
    [380, 170, 200, 5],
    [700, 380, 300, 5],
    [110, 30, 5, 200],
    [400, 85, 160, 5],
    [380, 320, 5, 200],
    [280, 510, 330, 5],
    [420, 320, 5, 150],
    [380, 30, 5, 180],
    [30, 420, 200, 5],
    [30, 220, 200, 5],
    [10, 100, 80, 5],
    [60, 0, 5, 70],
    [70, 340, 250, 5],
    [100, 310, 5, 85],
    [160, 250, 5, 70],
    [135, 120, 210, 5],
    [300, 240, 50, 5],
    [300, 120, 5, 80],
    [325, 240, 5, 80],
    [500, 0, 5, 60],
    [450, 30, 5, 55],
    [200, 0, 5, 80],
    [300, 0, 5, 80],
    [100, 150, 100, 5],
    [200, 180, 130, 5],
    [340, 150, 40, 5],
    [40, 450, 5, 110],
    [80, 450, 5, 110],
    [120, 450, 5, 110],
    [160, 450, 5, 110],
    [200, 450, 5, 110],
    [405, 380, 200, 5],
    [265, 380, 80, 5],
    [265, 410, 80, 5],
    [265, 440, 80, 5],
    [265, 470, 80, 5],
    [600, 0, 5, 250],
    [650, 230, 170, 5],
    [670, 400, 5, 200],
    [525, 350, 5, 80],
    [700, 420, 60, 5],
    [700, 450, 60, 5],
    [700, 480, 60, 5],
    [700, 510, 60, 5],
    [700, 540, 60, 5],
    [728, 540, 5, 30],
    [740, 50, 5, 300],
    [700, 50, 5, 300],
    [650, 10, 5, 190],
    [650, 280, 5, 100],
    [600, 325, 5, 160],
    [380, 400, 5, 150],
    [420, 550, 5, 40],
    [320, 550, 5, 40]
]
ENEMIES = [
    (50, 200, 10, 10, 5, (255, 255, 255), True),
    (200, 200, 10, 10, 5, (255, 255, 255), True),
    (275, 310, 10, 10, 5, (255, 255, 255), True),
    (500, 340, 10, 10, 5, (255, 255, 255), True),
    (480, 490, 10, 10, 5, (255, 255, 255), True),
    (600, 550, 10, 10, 5, (255, 255, 255), True),
    (550, 250, 10, 10, 5, (255, 255, 255), True),
    (50, 100, 10, 10, 5, (255, 255, 255), True)
]
class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
 
    def draw(self, color):
        self.screen.fill(color)
 
    def update(self):
        pygame.display.update()
        

      
class Menu:
    def __init__(self, punkts = [120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
    def menu(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0,0)
        font_menu = pygame.font.Font('fonts/Purisa.otf', 100)
        punkt = 0
        while done:
            info_string.fill((0, 0, 0))
            screen.fill((0, 0, 0))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            
                            #if gamerunning:
                            done = False
                        if punkt == 1:
                            sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    
                    if punkt == 0:
                        
                        
                        #if gamerunning:
                        done = False
                            
                    if punkt == 1:
                        sys.exit()
            
            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))
            # заливка окна
            screen.fill((0, 0, 0))
            pygame.display.update()
             
            
    
    # функция для вывода сообщения на экран
    def message(self, text, color, x, y):
        screen.blit(font.render(text, True, color), (x, y))
        pygame.display.update()
        
        
 
# класс для движущегося квадрата
class Player2:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        # create circle as rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
 
class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        # create circle as rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
    def move(self, x, y):
        self.x += x
        self.y += y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
    def collide(self, rect):
        return self.rect.colliderect(rect)
 
    # score collide player with enemy
    def score(self, rect, SCORE=None):
        if self.rect.colliderect(rect):
            SCORE += 1
            return SCORE
        
class Enemy:
    def __init__(self, x, y, width, height, vel=5, color=(0, 0, 255), right=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.right = right
 
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.width + 2, self.height + 2)
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.width, self.height)
 
    # move enemy
    def move(self):
        if self.right:
            self.x += self.vel
        else:
            self.x -= self.vel
 
    # the death of the player from the enemy and respawn him to the starting point
    def collide(self, player):
        if player.x + player.width >= self.x - self.width and player.x <= self.x + self.width:
            if player.y + player.height >= self.y - self.height and player.y <= self.y + self.height:
                player.x = START[0]
                player.y = START[1]
                player.rect = pygame.Rect(player.x, player.y, player.width, player.height)
                global next_level
                if not next_level :
                    global count
                    count +=1
                if next_level:
                    global count2
                    count2 +=1

        
# class of window filled with background with text
        
 
class Wall:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
 
    def collide(self, rect):
        return self.rect.colliderect(rect)
 
class Game2:
    def __init__(self, width, height, title):
        self.collide_enemy = None
        self.width = width
        self.height = height
        self.title = title
        self.window = Window(self.width, self.height, self.title)
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.run = True
        self.trap_collided = False
        self.score = 0
 
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE,color_me)
        self.player2 = Player2(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE,color_2)
 
        # make traps and walls
        self.walls2 = []
        self.traps = []
        self.create_walls2()
        self.create_traps()
 
        # make enemies
        self.enemies = []
        self.create_enemies()
 
        # make player
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
        # make player2
        self.player2 = Player2(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
 
        self.font = pygame.font.SysFont('freesansbold.ttf', 30, True)
 
    def create_enemies(self, list_of_enemies=ENEMIES):
        for enemy in list_of_enemies:
            self.enemies.append(Enemy(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4], enemy[5], enemy[6]))
 
    def create_walls2(self, list_of_coords=WALLS2):
        for coords in list_of_coords:
            self.walls2.append(Wall(coords[0], coords[1], coords[2], coords[3], (0, 0, 255)))
 
    def create_traps(self, list_of_coords=TRAPS):
        for coords in list_of_coords:
            self.traps.append(Wall(coords[0], coords[1], coords[2], coords[3], (200, 150, 0)))
 
    # counting the number of collisions player with the enemy

    def score(self):
        for enemy in self.enemies:
            if enemy.collide(self.player) :
                # self.collide_enemy = True
                self.score += 1
                return self.score
 
    def draw(self):
        self.window.draw((0, 0, 0))
        self.player.rect = pygame.draw.rect(self.window.screen, self.player.color, self.player.rect)
        self.player2.rect = pygame.draw.rect(self.window.screen, self.player2.color, self.player2.rect)
        
 
        # draw walls
        for wall in self.walls2:
            wall.draw(self.window.screen)
 
        if (self.trap_collided):
            self.print_text("You finished", 30, 30, (255, 0, 0), font_size=64)
            
        #if win=="0":
            #self.print_text("You lose", 30, 30, (255, 0, 0), font_size=64)
 
        # draw traps
        for trap in self.traps:
            trap.draw(self.window.screen)
 
        # draw enemies
        for enemy in self.enemies:
            enemy.draw(self.window.screen)
 
        # draw score
        # if not self.trap_collided:
        #  self.print_text(f"Score: {self.score}", 30, 620, (255, 255, 255))
        global count2
        self.print_text("Death: " + str(count2), 30, 620, (255, 0, 0), font_size=64)
    # функция соединения с сервером
    def connect(self):
        global gamerunning_2
        global client
        client.send(str.encode(str(game.player.x) + ";" + str(game.player.y)))
        data_1 = client.recv(64).decode()
        if ";" in data_1:
            # разбиваем координаты игрока по переменным x y
            
            cord = data_1.split(";")
            x = int(cord[0])
            y = int(cord[1])
            if ( int(y) >= 556) and (int(x) >=756):
                win == False
            # обновляем координаты Player2
            game.player2.x = int(cord[0])
            game.player2.y = int(cord[1])
            #print("Player2: ", x, y)
        
        # получаем от сервера состояние переменой  gamerunning
        client.send('?'.encode())
        data_2 = client.recv(64).decode()
        print(data_2)
        if data_2 == "0":
            gamerunning_2 = False
        if data_2 == "1":
            gamerunning_2 = True

        ''' if "&" in data_2 :
            g, n = data_2.split("&")
            print(g, n)
            if g=="1":
                gamerunning_2 = True
            else:
                gamerunning_2 = False
            if n == "1":
                win = "1"
               
            if n == "0":
                win = "0"'''
 
    def update(self):
        self.window.update()
        self.clock.tick(self.fps)
 
        prev_coords = (self.player.x, self.player.y)
        # обновляем положение 2 игрока
        self.player2.move(self.player2.x, self.player2.y)
        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-4, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(4, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -4)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 4)
 
        # enemy movement from left to right with collision
        for enemy in self.enemies:
            enemy.move()
            if enemy.x > self.width - enemy.width:
                enemy.right = False
            if enemy.x < enemy.width:
                enemy.right = True
 
        # the death of the player from the enemy and respawn him to the starting point
        for enemy in self.enemies:
            enemy.collide(self.player)
 
        # score collides with enemy
        for enemy in self.enemies:
            if enemy.collide(self.player):
                #self.collide_enemy = True
                global count2
                count2 += 1
                self.draw()
                return self.score
 
 
        # if player collides with wall move player to previous position
        if self.collision(self.player.rect, self.walls2):
            self.player.move(prev_coords[0] - self.player.x, prev_coords[1] - self.player.y)
 
        # if player collides with trap move player to start
        if self.collision(self.player.rect, self.traps):
            self.player.move(30 - self.player.x, 30 - self.player.y)
            self.trap_collided = True
 
    def print_text(self, message, x, y, font_color=(0, 0, 0), font_type='freesansbold.ttf', font_size=32):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.window.screen.blit(text, (x, y))
 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
 
    def run_game2(self):
        global gamerunning_2, win
        win = False
        gamerunning_2 = True
        print("connected")
        
        while self.run and gamerunning_2:
            #print(gamerunning_2)
            self.events()
            self.update()
            self.draw()
            self.connect()
            if ( game.player.y >= 556) and (game.player.x >=756):
                win == True
 
    def move_player(self, x, y):
        self.player.move(x, y)
        
    def move_player2(self, x, y):
        self.player2.move(x, y)
 
    def collision(self, rect, rects):
        for r in rects:
            if r.collide(rect):
                return True
        return False
 
    def get_player_rect(self):
        return self.player.rect
 
class Game:
    def __init__(self, width, height, title):
        self.collide_enemy = None
        self.width = width
        self.height = height
        self.title = title
        self.window = Window(self.width, self.height, self.title)
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.run = True
        self.trap_collided = False
        self.score = 0
 
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE,color_me)
        self.player2 = Player2(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE,color_2)
 
        # make traps and walls
        self.walls = []
        self.traps = []
        self.create_walls()
        self.create_traps()
 
        # make enemies
        self.enemies = []
        self.create_enemies()
 
        # make player
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, color_me)
        # make player2
        self.player2 = Player2(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, color_2)
 
        self.font = pygame.font.SysFont('freesansbold.ttf', 30, True)
 
    def create_enemies(self, list_of_enemies=ENEMIES):
        for enemy in list_of_enemies:
            self.enemies.append(Enemy(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4], enemy[5], enemy[6]))
 
    def create_walls(self, list_of_coords=WALLS):
        for coords in list_of_coords:
            self.walls.append(Wall(coords[0], coords[1], coords[2], coords[3], (0, 0, 255)))
 
    def create_traps(self, list_of_coords=TRAPS):
        for coords in list_of_coords:
            self.traps.append(Wall(coords[0], coords[1], coords[2], coords[3], (200, 150, 0)))
 
    # counting the number of collisions player with the enemy

    def score(self):
        for enemy in self.enemies:
            if enemy.collide(self.player) :
                # self.collide_enemy = True
                self.score += 1
                return self.score
 
    def draw(self):
        self.window.draw((0, 0, 0))
        self.player.rect = pygame.draw.rect(self.window.screen, self.player.color, self.player.rect)
        self.player2.rect = pygame.draw.rect(self.window.screen, self.player2.color, self.player2.rect)
        
 
        # draw walls
        for wall in self.walls:
            wall.draw(self.window.screen)
 
        if (self.trap_collided):
            self.print_text("You finished", 30, 30, (255, 0, 0), font_size=64)
 
        # draw traps
        for trap in self.traps:
            trap.draw(self.window.screen)
 
        # draw enemies
        for enemy in self.enemies:
            enemy.draw(self.window.screen)
 
        # draw score
        # if not self.trap_collided:
        #  self.print_text(f"Score: {self.score}", 30, 620, (255, 255, 255))
        global count
        self.print_text("Death:" + str(count), 30, 620, (255, 0, 0), font_size=64)
    # функция соединения с сервером
    def connect(self):
        global gamerunning_1, gamerunning_2, next_level, next_level_flag
        client.send(str.encode(str(game.player.x) + ";" + str(game.player.y)))
        data_1 = client.recv(64).decode()
        print('1')
        if ";" in data_1:
            # разбиваем координаты игрока по переменным x y
            
            cord = data_1.split(";")
            x = int(cord[0])
            y = int(cord[1])
            if ( int(y) >= 556) and (int(x) >=756):
                win == False
            # обновляем координаты Player2
            game.player2.x = int(cord[0])
            game.player2.y = int(cord[1])
        # отправляем серверу количество смертей
        client.send(str.encode(str(str(count)+"#"+"0")))
        #print("send count")
        #data_4 = client.recv(512).decode()
        # получаем от сервера состояние переменой  gamerunning
        client.send('?'.encode())
        data_2 = client.recv(64).decode()
        print('2')
        print(data_2)
        if ";" in data_2 :
            g, n = data_2.split(";")
            print(g, n)
            if g=="1":
                gamerunning_1 = True
            else:
                gamerunning_1 = False
            if n == "1":
                next_level = True
                next_level_flag = False
            if n == "0":
                next_level = False
                next_level_flag = False
        
        
 
    def update(self):
        self.window.update()
        self.clock.tick(self.fps)
 
        prev_coords = (self.player.x, self.player.y)
        # обновляем положение 2 игрока
        self.player2.move(self.player2.x, self.player2.y)
        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-4, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(4, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -4)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 4)
 
        # enemy movement from left to right with collision
        for enemy in self.enemies:
            enemy.move()
            if enemy.x > self.width - enemy.width:
                enemy.right = False
            if enemy.x < enemy.width:
                enemy.right = True
 
        # the death of the player from the enemy and respawn him to the starting point
        for enemy in self.enemies:
            enemy.collide(self.player)
 
        # score collides with enemy
        for enemy in self.enemies:
            if enemy.collide(self.player):
                #self.collide_enemy = True
                global count
                count += 1
                self.draw()
                return self.score
 
 
        # if player collides with wall move player to previous position
        if self.collision(self.player.rect, self.walls):
            self.player.move(prev_coords[0] - self.player.x, prev_coords[1] - self.player.y)
 
        # if player collides with trap move player to start
        if self.collision(self.player.rect, self.traps):
            self.player.move(30 - self.player.x, 30 - self.player.y)
            self.trap_collided = True
 
    def print_text(self, message, x, y, font_color=(0, 0, 0), font_type='freesansbold.ttf', font_size=32):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.window.screen.blit(text, (x, y))
 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
 
    def run_game(self):
        global color_me, color_2
        global gamerunning_1, gamerunning_2, next_level_flag
        gamerunning_1 = True
        next_level_flag = True
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, 10000))
        #client.send('*'.encode())
        #data_1 = client.recv(64).decode()
        """if ";" in data_1:
            colorr = data_1.split(";")
            print(colorr)
            color_me = colors[(colorr[0])]
            color_2 = colors[(colorr[1])]
            # меняем цвет игрока
            game.player.color = color_me
            # меняем цвет второго игрока
            game.player2.color = color_2
            print("color_me: ", color_me)
            print("color_2: ", color_2)
        print("connected")"""
        while self.run  and next_level_flag:
            #print(gamerunning)
            self.events()
            self.update()
            self.draw()
            self.connect()
            if ( game.player.y >= 556) and (game.player.x >=756):
                win == True
 
    def move_player(self, x, y):
        self.player.move(x, y)
        
    def move_player2(self, x, y):
        self.player2.move(x, y)
 
    def collision(self, rect, rects):
        for r in rects:
            if r.collide(rect):
                return True
        return False
 
    def get_player_rect(self):
        return self.player.rect


pygame.init()
#game = Game(SIZE[0], SIZE[1], TITLE)

#подключение к серверу
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#sock.connect((server_ip,10000))

if __name__ == '__main__':
    print("start")
    punkts = [(285, 180, u'Game', (250, 250, 30), (250, 30, 250), 0),
              (310, 310, u'Quit', (250, 250, 30), (250, 30, 250), 1)]
    game = Menu(punkts)
    game.menu()
    win = False
    game = Game(SIZE[0], SIZE[1], TITLE)
    game.run_game()
    #game= Game2(SIZE[0], SIZE[1], TITLE)
    if next_level:
        win = False
        game = Game2(SIZE[0], SIZE[1], TITLE)
        game.run_game2()
    if win ==  True:
        str_over = "You win!"
    else:
        str_over = "You lose!"
    ready = False
    print("ready")
    sc = pygame.display.set_mode((800, 700))
    sc.fill((0,0,0))
 
    f1 = pygame.font.SysFont('serif', 100)
    text1 = f1.render('Game over', True,(255,255,0))
 
    f2 = pygame.font.SysFont('serif',100)
    text2 = f2.render(str_over, False,(0,255,0))
 
    sc.blit(text1, (235,180))
    sc.blit(text2, (250, 310))
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
    #if game.punkts == 0:
        #ready = True
  
        
    
   
    
    
    
    
    
    










