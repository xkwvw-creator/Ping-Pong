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
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
#задай фон сцены
background = transform.scale(image.load('background_forest.jpg'), (700, 500))
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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 660:
            self.rect.x += self.speed
        


#player = Player('player2.jpg', 0, 460, 7, 40, 40)





game = True
finish = False
while game:
    for e in event.get(): # для каждого события в списке всех событий
        if e.type == QUIT: # если нажат крестик, то игра закрывается (game = False)
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        # player.reset()
        # player.update()
        

    
    
    clock.tick(FPS) # кол-во выполнений цикла while за секунду
    display.update() # обновляем данные на экране (60 раз в секунду)