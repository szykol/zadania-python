import pygame, os

# kolory
DARKRED = pygame.color.THECOLORS['darkred']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']


# grafika postać
STAND_R = pygame.image.load(os.path.join('png', 'player_standR.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'player_walkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'player_walkR2.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_standL.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'player_walkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'player_walkL2.png'))
FALL_L = pygame.image.load(os.path.join('png', 'player_fallL.png'))
FALL_R = pygame.image.load(os.path.join('png', 'player_fallR.png'))
JUMP_L = pygame.image.load(os.path.join('png', 'player_jumpL.png'))
JUMP_R = pygame.image.load(os.path.join('png', 'player_jumpR.png'))
IMAGES_R = [WALK_R1, WALK_R2]
IMAGES_L = [WALK_L1, WALK_L2]

# grafika platformy
GRASS_L = pygame.image.load(os.path.join('png', 'grass_L.png'))
GRASS_C = pygame.image.load(os.path.join('png', 'grass_C.png'))
GRASS_R = pygame.image.load(os.path.join('png', 'grass_R.png'))
GRASS_SINGLE = pygame.image.load(os.path.join('png', 'grass_single.png'))
GRASS_LIST = [GRASS_SINGLE, GRASS_L, GRASS_C, GRASS_R]

METAL_L = pygame.image.load(os.path.join('png', 'metal_L.png'))
METAL_C = pygame.image.load(os.path.join('png', 'metal_C.png'))
METAL_R = pygame.image.load(os.path.join('png', 'metal_R.png'))
METAL_SINGLE = pygame.image.load(os.path.join('png', 'metal_single.png'))
METAL_LIST = [METAL_SINGLE, METAL_L, METAL_C, METAL_R]


# grafika, broń i pociski
BULLET_R = pygame.image.load(os.path.join('png', 'bullet_R.png'))
BULLET_L = pygame.image.load(os.path.join('png', 'bullet_L.png'))
SHOTGUN = pygame.image.load(os.path.join('png', 'shotgun.png'))

# okno główne
SIZESCREEN = WIDTH, HEIGHT = 1366, 740