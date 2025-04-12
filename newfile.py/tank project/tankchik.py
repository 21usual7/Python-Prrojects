import pygame
import random
###задача проекта архетиктура преокта, изпользование ООП, рефактиринга
#  и струкруности кода, декораторов ошибок и исключений логика взаэмосвязенности класов.  гитхаба

class Tank:
    """Создает танк с заданными параметрами и методами."""
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self._color = color
        self.speed = speed
        self.img = pygame.image.load("tank_img.jpg")
        self.img_rect = self.img.get_rect()
        self.img_rect.x = x
        
    def draw(self, win):
        """Рисует танк на игровом поле."""
        win.blit(self.img, (self.x, self.y))
    
    def move(self, direction):
        """Двигает танк по оси x."""
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += self.speed
 
class Field:
    """Создает игровое поле с заданными параметрами."""
    

class Cannon:
    pass

class Target:
    pass

class Bullet:
    pass

class GameRoundManager:
    """Управляет игровыми раундами, создает и запускает их, также создает танк и игровое поле с цельми."""
    def __init__(self):
        self.tank = Tank(100, 400, (255, 0, 0), 5)

        #Инициализация Pygame и создание окна

        pygame.init()
        self.HEIGHT, self.WIDTH = 600, 1280
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
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
            self.WIN.fill((0, 0, 0))
            self.tank.draw(self.WIN)
            self.tank.move(self.WIN)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = GameRoundManager()
    game.main()


