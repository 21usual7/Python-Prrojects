import pygame
import random

"""задача проекта архетиктура преокта, изпользование ООП, рефактиринга
и струкруности кода, декораторов ошибок и исключений логика взаэмосвязенности класов.  гитхаба"""

#Constants variables
WIDTH, HEIGHT = 1280, 600

class Tank:
    """Создает танк с заданными параметрами и методами."""
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.tank_img = pygame.image.load("tank.png")
        self.new_size = (self.tank_img.get_width() // 4, self.tank_img.get_height() // 4)
        self.tank_transform_img = pygame.transform.scale(self.tank_img, self.new_size) #изменяем размер танка
        self.tank_img_rect = self.tank_transform_img.get_rect(center = (self.x, self.y)) #центр танка по оси x и y
        self.tank_img_rect.x = x
        
    def draw_tank(self, win):
        """Рисует танк на игровом поле."""
        win.blit(self.tank_transform_img, (self.x, self.y))
    
    def move_tank(self, direction):
        """Двигает танк по оси x."""
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += self.speed
        
        self.tank_img_rect.center = (self.x, self.y) #центр танка по оси x и y
 

class Field:
    """Создает игровое поле с заданными параметрами."""
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.ground_img = pygame.image.load("ground.png")
        self.ground_img = pygame.transform.scale(self.ground_img, (self._width, self._height))
    
    def draw_field(self, win):
        """Рисует игровое поле."""
        win.blit(self.ground_img, (0, 0))
    
    def draw_border(self, tank, target, bullet):
        """Создает границы игрового поля."""
        if tank.x < 0 or tank.x > self._width - tank.tank_img_rect.width: #проверяем выход за границы учитвая x првый танка и ширину танка
            #если выход за границы то танк не может выйти за границы
            tank.x = max(0, min(tank.x, self._width - tank.tank_img_rect.width)) 
        #if target.x < 0 or self.target.x > self._width - self.target.target_img_rect.width:
           # target.x = max(0, min(self.target.x, self._width - self.target.target_img_rect.width))
        #if bullet.x < 0 or bullet.x > self._width - bullet.bullet_img_rect.width:
            #bullet.x = max(0, min(bullet.x, self._width - bullet.bullet_img_rect.width))
        

class Cannon:
    """Создает пушку с заданными параметрами."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cannon_img = pygame.image.load("canon.png")
        self.cannon_img = pygame.transform.scale(self.cannon_img, (self.cannon_img.get_width() // 4, self.cannon_img.get_height() // 4))
        self.cannon_rect = self.cannon_img.get_rect()
        self.cannon_rect.x = x

    def updte_cannon(self, tank):
        """Обновляет положение пушки."""
        self.cannon_rect.center = (tank.x, tank.y - 50) #пушка будет находиться над танком

    def draw_cannon(self, win):
        """Рисует пушку на игровом поле."""
        win.blit(self.cannon_img, (self.x, self.y))

class Target:
    pass


class Bullet:
    pass


class GameRoundManager:
    """Управляет игровыми раундами, создает и запускает их, также создает танк и игровое поле с цельми."""
    def __init__(self):
        self.tank = Tank(100, 400,  5)
        self.field = Field(1280, 600)
        self.target = Target()
        self.bullet = Bullet()
        self.cannon = Cannon(100, 400 - 50) #пушка будет находиться над танком

        #Инициализация Pygame и создание окна

        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TANK GAME")

        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

    
    def main(self):
        while self.running:
            #self.run_game_round()
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #Рисуем объект на экране
            self.WIN.fill((0, 0, 0))
            self.field.draw_field(self.WIN)
            self.field.draw_border(self.tank, self.target, self.bullet)
            self.tank.draw_tank(self.WIN)
            self.cannon.updte_cannon(self.tank)
            self.cannon.draw_cannon(self.WIN)
            self.tank.move_tank(self.WIN)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = GameRoundManager()
    game.main()


