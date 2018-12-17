TITLE = "The Jumping Bird"
# screen dims
WIDTH = 480
HEIGHT = 600
# frames per second
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,55,66)
YELLOW = (255, 255, 0)
GREEN = (25, 198, 60)
DARKBLUE = (14, 9, 59)
SKY_BLUE = (143, 185, 252)
DARK_RED = (112, 19, 19)
FONT_NAME = '&quot'
SPRITESHEET = "spritesheet_jumper.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 23
# game settings
CLOUD_POWER = 85
BOOST_POWER = 100
BOOM_POWER = 70
POW_SPAWN_PCT = 7
BOOM_SPAWN_PCT = 7
MOB_FREQ = 70000
# layers - adds order on what is in front of one another
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
CLOUD_LAYER = 0
POW_LAYER = 1
BOOM_LAYER = 1
MOB_LAYER = 2
SPIKES_LAYER = 2

# platform settings
''' old platforms from drawing rectangles'''
'''
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (65, HEIGHT - 300, WIDTH-400, 40),
                 (20, HEIGHT - 350, WIDTH-300, 40),
                 (200, HEIGHT - 150, WIDTH-350, 40),
                 (200, HEIGHT - 450, WIDTH-350, 40)]
'''
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (65, HEIGHT - 300),
                 (20, HEIGHT - 350),
                 (200, HEIGHT - 150),
                 (200, HEIGHT - 450)]
