import pygame
import random
import math

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

    def move_tank(self, direction):
        """Двигает танк по оси x."""
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += self.speed
        
        self.tank_img_rect.center = (self.x, self.y) #центр танка по оси x и y
        
    def draw_tank(self, win):
        """Рисует танк на игровом поле."""
        win.blit(self.tank_transform_img, self.tank_img_rect)
    

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
    """Создает пушку, которая зависит от танка и управляется мышью."""
    def __init__(self, tank):
        self.tank = tank  # Пушка зависит от танка
        self.angle = 0
        self.max_angle = 45  # Ограничиваем вращение пушки на 45 градусов по обе стороны от центра (всего 90 градусов)

        # Загружаем изображение пушки
        self.cannon_img = pygame.image.load("canon.png")
        self.cannon_img = pygame.transform.smoothscale(self.cannon_img, (100, 100))  # Настройка размера пушки
        self.cannon_rect = self.cannon_img.get_rect(center=(self.tank.x, self.tank.y - 30))  

    def update_cannon(self):
        # Пушка двигается с танком
        self.cannon_rect.center = (self.tank.x, self.tank.y - 30)  # Пушка всегда по центру танка, немного выше

        # Угол между пушкой и мышью (для вращения пушки)
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.tank.x
        dy = my - self.tank.y
        self.angle = math.degrees(math.atan2(dy, dx))

        # Ограничиваем вращение пушки на 90 градусов (по 45 градусов в каждую сторону)
        if self.angle > self.max_angle:
            self.angle = self.max_angle
        elif self.angle < -self.max_angle:
            self.angle = -self.max_angle

    def draw_cannon(self, win):
        # Вращаем пушку на основе угла
        rotated_cannon = pygame.transform.rotate(self.cannon_img, self.angle)
        rotated_cannon_rect = rotated_cannon.get_rect(center=self.cannon_rect.center)
        win.blit(rotated_cannon, rotated_cannon_rect)

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
        self.cannon = Cannon(self.tank) #пушка будет находиться над танком

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
            self.cannon.update_cannon()
            self.cannon.draw_cannon(self.WIN)
            self.tank.move_tank(self.WIN)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = GameRoundManager()
    game.main()


