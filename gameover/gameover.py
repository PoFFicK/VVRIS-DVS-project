from itertools import count
import pygame

 
START = (30, 30)
TRAPS = [(770, 560, 20, 30),
         (770, 10, 20, 30)]
TRAP_SIZE = 10
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
 
SIZE = (800, 700)
TITLE = "hardest game analog"
PLAYER_SIZE = 10
FPS = 60
count = 0
 

    
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
                global count
                count +=1
            
 
 
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
 
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
 
        # make traps and walls
        self.walls = []
        self.traps = []
        self.create_walls()
        self.create_traps()
 
        # make enemies
        self.enemies = []
        self.create_enemies()
 
        # make player
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
 
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
        self.print_text("Score: " + str(count), 30, 620, (255, 0, 0), font_size=64)
 
    def update(self):
        self.window.update()
        self.clock.tick(self.fps)
 
        prev_coords = (self.player.x, self.player.y)
 
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
        while self.run:
            self.events()
            self.update()
            self.draw()
 
    def move_player(self, x, y):
        self.player.move(x, y)
 
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
 
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
 
        # make traps and walls
        self.walls = []
        self.traps = []
        self.create_walls()
        self.create_traps()
 
        # make enemies
        self.enemies = []
        self.create_enemies()
 
        # make player
        self.player = Player(PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE, (255, 0, 0))
 
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
        self.print_text("Score: " + str(count), 30, 620, (255, 0, 0), font_size=64)
 
    def update(self):
        self.window.update()
        self.clock.tick(self.fps)
 
        prev_coords = (self.player.x, self.player.y)
 
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
        while self.run:
            self.events()
            self.update()
            self.draw()
 
    def move_player(self, x, y):
        self.player.move(x, y)
 
    def collision(self, rect, rects):
        for r in rects:
            if r.collide(rect):
                return True
        return False
 
    def get_player_rect(self):
        return self.player.rect
 
if __name__ == '__main__':

    pygame.init()
    game = Game(SIZE[0], SIZE[1], TITLE)
    game.run_game()
    if game.trap_collided:
        game = Game2(SIZE[0], SIZE[1], TITLE)
        game.run_game()
    pygame.quit()
