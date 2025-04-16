import pygame
import random
import math

# Constants variables
WIDTH, HEIGHT = 1280, 600


class Tank:
    """Создает танк с заданными параметрами и методами."""
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.tank_img = pygame.image.load("tank.png")
        self.new_size = (self.tank_img.get_width() // 5, self.tank_img.get_height() // 5)
        self.tank_transform_img = pygame.transform.scale(self.tank_img, self.new_size)  # изменяем размер танка
        self.tank_img_rect = self.tank_transform_img.get_rect(center=(self.x, self.y))  # центр танка по оси x и y
        self.tank_img_rect.x = x

    def move_tank(self):
        """Двигает танк по оси x."""
        if pygame.key.get_pressed()[pygame.K_a]:
            self.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += self.speed
        
        self.tank_img_rect.center = (self.x, self.y)  # центр танка по оси x и y
        
    def draw_tank(self, win):
        """Рисует танк на игровом поле."""
        win.blit(self.tank_transform_img, self.tank_img_rect)


class Field:
    """Создает игровое поле с заданными параметрами."""
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.filed_img = pygame.image.load("ground.png")
        self.field_img = pygame.transform.scale(self.filed_img, (self._width, self._height))
    
    def draw_field(self, win):
        """Рисует игровое поле."""
        win.blit(self.field_img, (0, 0))
    
    def draw_border(self, tank:Tank):
        """Создает границы игрового поля."""
        if tank.x < 0 or tank.x > self._width - tank.tank_img_rect.width:  # проверяем выход за границы
            tank.x = max(0, min(tank.x, self._width - tank.tank_img_rect.width))
        
    def remove_offscreen_bullets(self, bullets):
         for bullet in bullets[:]:
            if bullet.pos_x < 0 or bullet.pos_x > self._width or bullet.pos_y < 0 or bullet.pos_y > self._height:
                bullet.active = False
    
    def change_targets_direction_if_needed(self, target):
       if target.rect.left <= 0 or target.rect.right >= self._width:
            target.speed_x *= -1


class Cannon:
    """Создает пушку, которая зависит от танка и управляется мышью."""
    def __init__(self, tank:Tank):
        self.tank = tank  # Пушка зависит от танка
        self.angle = 0
        self.max_angle = 45  # Ограничиваем вращение пушки на 45 градусов по обе стороны от центра (всего 90 градусов)

        # Загружаем изображение пушки
        self.cannon_img = pygame.image.load("canon.png")
        self.cannon_img = pygame.transform.smoothscale(self.cannon_img, (60, 60))  # Настройка размера пушки
        self.cannon_rect = self.cannon_img.get_rect(center=(self.tank.x, self.tank.y - 30))  

    def update_cannon(self):
        # Пушка двигается с танком
        self.cannon_rect.center = (self.tank.x, self.tank.y - 30)  # Пушка всегда по центру танка, немного выше

        # Угол между пушкой и мышью (для вращения пушки)
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.tank.x
        dy = my - self.tank.y
        self.angle = math.degrees(math.atan2(dy, dx))

    def draw_cannon(self, win):
        # Вращаем пушку на основе угла
        rotated_cannon = pygame.transform.rotate(self.cannon_img, -self.angle)  # инвертируем угол, так как pygame работает по-другому
        rotated_cannon_rect = rotated_cannon.get_rect(center=self.cannon_rect.center)
        win.blit(rotated_cannon, rotated_cannon_rect)


class Targets(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed_x=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x  # скорость движения по оси X
        self.direction = 1  # 1 - вправо, -1 - влево

    def update(self):
        # Изменяем позицию цели по оси X на основе скорости и направления
        self.rect.x += self.speed_x * self.direction

    def draw(self, win):
        win.blit(self.image, self.rect)  # Рисуем цель
    

class Bullet:
    """Спавнит пули танчка"""
    def __init__(self, x, y, angle, speed=5):
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

        # Angle
        self.angle = angle
        self.dir_x = math.cos(math.radians(angle))
        self.dir_y = math.sin(math.radians(angle))

        # PNG
        self.yadro_img = pygame.image.load("yadro.png")
        self.yadro_img = pygame.transform.scale(self.yadro_img, (20, 20))
        self.yadro_img_rect = self.yadro_img.get_rect(center=(x, y))

        self.active = True

    def update_bullet(self):
        """Получение координат и угла полета"""
        if not self.active:
            return
        self.pos_x += self.dir_x * self.speed
        self.pos_y += self.dir_y * self.speed
        self.yadro_img_rect.center = (self.pos_x, self.pos_y)

    def check_collision(self, target_group):
        for target in target_group:
            if self.yadro_img_rect.colliderect(target.rect):
                self.active = False
                target.kill()
                return True
        return False

    def draw_bullet(self, win):
        if self.active:
            win.blit(self.yadro_img, self.yadro_img_rect)


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

class GameRoundManager:
    """Управляет игровыми раундами, создает и запускает их, также создает танк и игровое поле с целями."""
    def __init__(self):
        # Создание экземпляров классов
        self.tank = Tank(x=100, y=400, speed =2)
        self.field = Field(WIDTH, HEIGHT)
        self.cannon = Cannon(self.tank)

        # Инициализация Pygame
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TANK GAME")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

        #FONT
        self.font = pygame.font.SysFont("Arial", 30)

        #Varibles
        self.score = 0

        # 🎯 Загружаем картинки целей
        self.filenames = [
            "turret_targets0.png",
            "turret_targets1.png",
            "turret_targets2.png",
        ]
        # Уменьшение каждого изображения
        self.target_images = [
            pygame.transform.scale(pygame.image.load(name).convert_alpha(), (60, 60))
            for name in self.filenames
        ]

        self.targets_group = pygame.sprite.Group()

        # 🎯 Спавним все цели
        target_positions = [(300, 50), (600, 100), (900, 150)] 
        for img, pos in zip(self.target_images, target_positions):
            target = Targets(pos[0], pos[1], img)
            self.targets_group.add(target)

        # Список пуль
        self.bullets = []

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.WIN.blit(score_text, (20, 20))

    def main(self):
        while self.running:
            self.clock.tick(self.FPS)

            # Обрабатываем события
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not any(b.active for b in self.bullets):  # нет активных пуль
                        cx, cy = self.cannon.cannon_rect.center
                        angle = self.cannon.angle
                        new_bullet = Bullet(cx, cy, angle)
                        self.bullets.append(new_bullet)

            # Обновляем экран
            self.WIN.fill((0, 0, 0))
            self.field.draw_field(self.WIN)
            self.field.draw_border(self.tank)
            
            for target in self.targets_group: #меняем траекторию целей если они соприкасаються с границей поля
                self.field.change_targets_direction_if_needed(target)

            # Двигаем и рисуем танк
            self.tank.move_tank()
            self.tank.draw_tank(self.WIN)

            # Обновляем и рисуем пушку
            self.cannon.update_cannon()
            self.cannon.draw_cannon(self.WIN)

            # Обновляем и рисуем пули
            for bullet in self.bullets[:]:
                bullet.update_bullet()
                if not bullet.active:
                    self.bullets.remove(bullet)
                bullet.draw_bullet(self.WIN)
                if bullet.check_collision(self.targets_group):
                    self.score += 1
            self.field.remove_offscreen_bullets(self.bullets)

            used_positions = set()

             #Респавн целей       
            while len(self.targets_group) < 3: #изначально три цели, если группа становиться меньше значит начинаем добавлять новую пнг с новими кординатами
                x = random.randint(50, 300)  
                y = random.randint(50, 150)  
                speed = random.uniform(1, 3)
                if (x, y) in used_positions:
                    continue

                used_positions.add((x, y))
                img = random.choice(self.target_images)
                self.targets_group.add(Targets(x, y, img, speed))

            self.targets_group.update()
            self.targets_group.draw(self.WIN)
            self.draw_score()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = GameRoundManager()
    game.main()
