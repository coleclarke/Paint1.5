import pygame

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
r = 200
b = 200
g = 200
x = 0
pw = 50
px = 350
py = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((px, py, pw, pw))


run = True

while run:
    mx, my = pygame.mouse.get_pos()
    px = player.x + 1/2 * pw
    py = player.y + 1/2 * pw
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        if py < my:
            player.move_ip(0, 1)
        if py > my:
            player.move_ip(0, -1)
        if px > mx:
            player.move_ip(-1, 0)
        if px < mx:
            player.move_ip(1, 0)
    #clock.tick(100)

    pygame.draw.rect(screen, (r,g,b), player)
    pw = player.w

    if key[pygame.K_a] == True:

        if r > 0:
            r = r - 1

    if key[pygame.K_d] == True:

        if g > 0:
            g = g - 1

    if key[pygame.K_w] == True:

        if b > 0:
            b = b - 1

    if key[pygame.K_s] == True:

        if r < 255:
            r = r + 1
        if g < 255:
            g = g + 1
        if b < 255:
            b = b + 1

    if key[pygame.K_e] == True:
        if pw < 100:
            player.scale_by_ip(1.1)
        
    if key[pygame.K_q] == True:
        if pw > 10:
            player.scale_by_ip(0.99)
    print(pw)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if key[pygame.K_x] == True:
        if px != 1260:
            if px > mx:
                player.move_ip(-1, 0)
            elif px < mx:
                player.move_ip(1, 0)
        if py != 540:
            if py < my:
                player.move_ip(0, 1)
            elif py > my:
                player.move_ip(0, -1)
        if pw < 2000:
            
            player.scale_by_ip(1.1)
            r = 0
            b = 0
            g = 0
        
        
            

    pygame.display.update()

pygame.quit()
