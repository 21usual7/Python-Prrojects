import pygame
import random
###задача проекта архетиктура преокта, изпользование ООП, рефактиринга
#  и струкруности кода, декораторов ошибок и исключений логика взаэмосвязенности класов.  гитхаба

class Tank:
    pass

class Cannon:
    pass

class Target:
    pass

class Bullet:
    pass

class GameRoundManager:
    """Управляет игровыми раундами, создает и запускает их, также создает танк и игровое поле с цельми."""
    def __init__(self):
        #Инициализация Pygame и создание окна
        pygame.init()
        self.Height, self.Width = 800, 600
        self.WIN = pygame.display.set_mode((self.Width, self.Height))
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
                pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = GameRoundManager()
    game.main()


