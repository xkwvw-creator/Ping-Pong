#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer
font.init()
lost = 0
font1 = font.SysFont('Arial', 70)
win_left = font1.render('Jerry won!', True, (50, 255, 50))
win_right = font1.render('Rick won!', True, (50, 255, 50))

font2 = font.SysFont('Arial', 30)



mixer.init()
hit = mixer.Sound('Fox_spit1.ogg.mp3')
hit.set_volume(0.3)

wall_hit = mixer.Sound('Fox_hurt2.ogg.mp3')
wall_hit.set_volume(0.3)

lose = mixer.Sound('Fox_death2.ogg.mp3')
lose.set_volume(0.4)


#создай окно игры
window = display.set_mode((1024, 602))
display.set_caption('Пинг-Понг')
#задай фон сцены
background = transform.scale(image.load('background_forest.png'), (1024, 602))

window.blit(background, (0, 0))

# установка кадров в секунду (fps)
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect() # Получаем прямоугольник на котором лежит эта картинка
        #что-бы можно было обращаться к координате х, у прямоугольника на котором лежит картинка
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 472:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 472:
            self.rect.y += self.speed

        


player_left = Player('Fox2.png', 0, 271, 10, 110, 130)
player_right = Player('Fox1.png', 915, 271, 10, 110 , 130)

sweet_ball = GameSprite('Sweet_ball-1.png.png', 512, 301, 5, 80, 80)
speed_x = 7
speed_y = 7


game = True
finish = False
while game:
    for e in event.get(): # для каждого события в списке всех событий
        if e.type == QUIT: # если нажат крестик, то игра закрывается (game = False)
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player_left.reset()
        player_left.update_left()
        player_right.reset()
        player_right.update_right()
        sweet_ball.reset()
        sweet_ball.rect.x += speed_x
        sweet_ball.rect.y += speed_y
        if sweet_ball.rect.y >= 522:
            speed_y = -7
        if sweet_ball.rect.y <= 0:
            speed_y = 7
        if sweet_ball.rect.colliderect(player_right.rect) or sweet_ball.rect.colliderect(player_left.rect):
            speed_x *= -1

        

    
    
    clock.tick(FPS) # кол-во выполнений цикла while за секунду
    display.update() # обновляем данные на экране (60 раз в секунду)
