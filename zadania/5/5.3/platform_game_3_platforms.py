import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()


## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Prosta gra platformowa...')
clock = pygame.time.Clock()


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.lifes = 3
        self.level = None
        self.direction_of_movement = 'right'

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 5
        self.direction_of_movement = 'right'

    def turn_left(self):
        self.movement_x = -5
        self.direction_of_movement = 'left'

    def stop(self):
        self.movement_x = 0

    def update(self):
        self.rect.x += self.movement_x

        if self.movement_x > 0:
            self._move(gm.IMAGES_R)

        if self.movement_x < 0:
            self._move(gm.IMAGES_L)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_a:
                self.turn_left()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
                self.image = gm.STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
                self.image = gm.STAND_L

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]
        if self.count >= 8:
            self.count = 0
        else:
            self.count += 1

class Platform(pygame.sprite.Sprite):

    def __init__(self,colour,width,height,rect_x,rect_y):
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image,self.rect)

class Level():
    def __init__(self,Player):
        self.player = Player
        self.set_of_platforms = set()

    def update(self):
        for i in self.set_of_platforms:
            i.update()
        
    def draw(self,surface):
        for i in self.set_of_platforms:
            i.draw(surface)

class Level_1(Level):
    def __init__(self,player):
        super().__init__(player)
        list_p = ((7000,70,0,gm.HEIGHT-70),(280,70,800,350),(140,70,200,350))
        for i in list_p:
            p = Platform(gm.DARKGREEN,*i)
            self.set_of_platforms.add(p)
        

# konkretyzacja obiektów
player = Player(gm.STAND_R)
player.rect.center = screen.get_rect().center
level_1 = Level_1(player)
player.level = level_1

# głowna pętla gry
window_open = True
while window_open:
    screen.fill(gm.LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        player.get_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False

    # rysowanie i aktualizacja obiektów
    player.update()
    player.draw(screen)
    level_1.update()
    level_1.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()