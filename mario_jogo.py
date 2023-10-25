 # JOGO DO MARIO

import pygame

width = 1600
height = 900

def load():
    global sys_font, clock, px, py, chao, tubo, montanha, nuvem, i, icon_1up, icon_super, audio_1up

    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    chao = pygame.image.load('mario_ground.png')
    tubo = pygame.image.load('mario_pipe.png')
    montanha = pygame.image.load('mario_background.png')
    nuvem = pygame.image.load('mario_cloud.png')
    icon_1up = pygame.image.load("1up.png")
    icon_super = pygame.image.load("super.png")



    audio_1up = pygame.mixer.Sound("1up.mp3")
    pygame.mixer.music.load("super.mp3")



    montanha = pygame.transform.scale(montanha, (montanha.get_width()*1.5, montanha.get_height()*1.5))
    px = 0
    py = 0
    i = 0

def draw_screen(screen):
    global px, py
    screen.fill((100,150,250))

    
    t = sys_font.render(' ', False, (0,0,0))
    screen.blit(t, t.get_rect(top = 290, left = px))

    
    xmontanha = -70
    while xmontanha < screen.get_width():
        screen.blit(montanha, (xmontanha, 420))
        xmontanha = xmontanha + 300

        
    xtubo = 320
    while xtubo < screen.get_width():
        screen.blit(tubo, (xtubo, 705))
        xtubo = xtubo + 850

        
    xchao = 0
    while xchao < screen.get_width():
        screen.blit(chao, (xchao, 772))
        xchao = xchao + 128

        
    screen.blit(nuvem, (px, 200))





def start(screen):
    screen.fill((255,255,255))
    screen.blit(icon_1up, (500, 400))
    screen.blit(icon_super, (950, 400))
    t = sys_font.render("Clique para 1up", True, (0,0,0))
    screen.blit(t, (495,370))
    t = sys_font.render("Clique Música", True, (0,0,0))
    screen.blit(t, (945,370))
    t = sys_font.render("Música: i para iniciar, p para pausar, r para despausar, s para parar", True, (0,0,0))
    screen.blit(t, t.get_rect(top = 800, left=1600/2 - t.get_width()/2)) 


def update(dt):
    global px, clock, i 

    if i < 815:
        px = px + (0.1 * dt)
        i += 1
    elif i >= 815:
        px = px - (0.1 * dt)
        i += 1
    if i == 1630:
        px = 0
        i = 0
    
    #print(i)


def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1



def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    if mouse_buttons[0]: # left
        if check_click(950, 400, 128, 128, px_mouse, py_mouse):
            pygame.mixer.music.play()
            play = True
        if check_click(500,400,128,128, px_mouse, py_mouse):
            pygame.mixer.Sound.play(audio_1up)
    elif mouse_buttons[2]: # right
        if check_click(950, 400, 128, 128, px_mouse, py_mouse):
            pygame.mixer.music.stop()
            play = False
        if check_click(500,400,128,128, px_mouse, py_mouse):
            audio_1up.stop() 

def mouse_click_up(px_mouse, py_mouse, mouse_buttons):
    pass


def keyboard_keydown(keys):
    global play

    if keys[pygame.K_i]:
        pygame.mixer.music.play()
        play = True
    elif keys[pygame.K_p]:
        pygame.mixer.music.pause()
        play = False
    elif keys[pygame.K_r]:
        pygame.mixer.music.unpause()
        play = True
    elif keys[pygame.K_s]:
        pygame.mixer.music.stop()
        play = False
        


def keyboard_keyup(keys):
    pass


def main_loop(screen):
    global clock, play
    running = True
    play = False
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break

            elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.MOUSEBUTTONUP: #detecta o fim do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_up(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.KEYDOWN: #detecta o inicio do clique do teclado
                keys = pygame.key.get_pressed()
                keyboard_keydown(keys)
            elif e.type == pygame.KEYUP: #detecta o fim do clique do teclado
                keys = pygame.key.get_pressed()
                keyboard_keyup(keys)
            
        
        clock.tick(60)        
        dt = clock.get_time()
        #update(dt)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        keyboard_keydown(keys)
        if play == True:
            draw_screen(screen)
            update(dt)
        if play == False:
            start(screen)
        pygame.display.update()


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()



