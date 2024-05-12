import pygame

pygame.init()

back = (200, 255, 255)  # цвет фона (background)
mw = pygame.display.set_mode((500, 500))  # окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()

# переменные, отвечающие за координаты платформы
racket1_x = 200
racket1_y = 50

racket2_x = 200
racket2_y = 450

level = 1

# флаг окончания игры
game_over = False


# класс из предыдущего проекта
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# создание мяча и платформы
ball = Picture('ball.png', 25, 200, 50, 50)
platform1 = Picture('platform.png', racket1_x, racket1_y, 70, 25)
platform2 = Picture('platform.png', racket2_x, racket2_y, 70, 25)

speed_x = 3
speed_y = 3
move_right1, move_left1 = False, False
move_right2, move_left2 = False, False
#игровой цикл
while not game_over:
    mw.fill(back)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right1 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right1 = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left1 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left1 = False




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right2 = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left2 = False

        if move_right1:
            platform1.rect.x += 6
        elif move_left1:
            platform1.rect.x -= 6

        if move_right2:
            platform2.rect.x += 6
        elif move_left1:
            platform2.rect.x -= 6

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.x < 0:
            speed_y *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_x *= -1

        if platform1.rect.y > 450 - 50:
            platform1.rect.y -= 6

        if platform1.rect.y < 0:
            platform1.rect.y += 6

        if platform2.rect.y > 450 - 50:
            platform2.rect.y -= 6

        if platform2.rect.y < 0:
            platform2.rect.y += 6

        if ball.rect.y > (racket1_y + 20):
            time_text = Label(150, 150, 50, 50, back)
            time_text.set_text('YOU LOSE', 60, (255, 0, 0))
            time_text.draw(10, 50)
            #game_over = True

        if ball.rect.y > (racket2_y + 20):
            time_text = Label(150, 150, 50, 50, back)
            time_text.set_text('YOU LOSE', 60, (255, 0, 0))
            time_text.draw(10, 50)
            #game_over = True

        ball.fill()
        platform1.fill()
        platform2.fill()

        platform1.draw()
        platform2.draw()
        ball.draw()

        pygame.display.update()
        clock.tick(40)