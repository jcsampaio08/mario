# JOGO DO MARIO

import pygame

width = 1600
height = 900

def load():
    global sys_font, clock, px, py, chao, tubo, montanha, nuvem

    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    chao = pygame.image.load('mario_ground.png')
    tubo = pygame.image.load('mario_pipe.png')
    montanha = pygame.image.load('mario_background.png')
    nuvem = pygame.image.load('mario_cloud.png')

    montanha = pygame.transform.scale(montanha, (montanha.get_width()*1.5, montanha.get_height()*1.5))
    px = 0
    py = 0
    

def draw_screen(screen):
    global px, py
    screen.fill((100,150,250))
    t = sys_font.render(' ', False, (0,0,0))
    screen.blit(t, t.get_rect(top = 290, left = px))
    xmontanha = -70
    while xmontanha < screen.get_width():
        screen.blit(montanha, (xmontanha, 420))
        xmontanha = xmontanha + 300
    xtubo = 350
    while xtubo < screen.get_width():
        screen.blit(tubo, (xtubo, 705))
        xtubo = xtubo + 850
    xchao = 0
    while xchao < screen.get_width():
        screen.blit(chao, (xchao, 772))
        xchao = xchao + 128
    xnuvem = 150
    while xnuvem < screen.get_width():
        screen.blit(nuvem, (xnuvem, 200))
        xnuvem = xnuvem + 900

    

    


def update(dt):
    global px, cl1, cl2, cl3, clock
    px = px - (0.1 * dt)

    
def main_loop(screen):
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        clock.tick(60)        
        dt = clock.get_time()
        draw_screen(screen)
        #update(dt)
        pygame.display.update()
        draw_screen(screen)
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()



