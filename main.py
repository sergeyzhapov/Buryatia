import sys
import random
import pygame
import pygine as pg
from pygine.scene import Scene, SceneManager

pygame.init()
pygame.mixer.init()


WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (7, 135, 5)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 0)
PURPLE = (130, 100, 162)
BACKGROUND = (135, 206, 235)

space_cooldown = 1.0

game = pg.Game(800, 600, "Игра")

scene_manager = SceneManager()

scenes = ["menu", "game_scene1", "game_scene2", "game_scene3", "game_scene4", "game_scene5"]

def exit():
    pygame.quit()
    sys.exit()

def goto_menu():
    scene_manager.switch_to(scenes[0])

def scene1():
    scene_manager.switch_to(scenes[1])
    
def scene2():
    scene_manager.switch_to(scenes[2])
    
def scene3():
    scene_manager.switch_to(scenes[3])
    
def scene4():
    scene_manager.switch_to(scenes[4])
    
def scene5():
    scene_manager.switch_to(scenes[5])

class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")
        
        self.skybox = pg.AnimatedSprite("assets/menu/skybox.png", (1600, 150), (400, 75))
        self.game_name = pg.AnimatedSprite("assets/menu/name.png", (364, 150), (190, 200))
        self.mother_bur = pg.AnimatedSprite("assets/menu/mother_bur.png", (378, 590), (580, 310))
        
        self.gull = pg.AnimatedSprite("assets/menu/gull.png", (75, 48), (-50, 20))
        self.gull.add_animation("fly", [0, 1, 2, 3, 4, 5, 6, 7], fps=5, loop=True)
        self.gull.play_animation("fly")
        
        self.gull_feed = pg.AnimatedSprite("assets/menu/gull_feed.png", (227, 50), (1500, 70))
        self.gull_feed_visible = False
        self.gull_feed_timer = 0
        
        self.start_btn = pg.Button(8, 340, 150, 50, "НАЧАТЬ", scene1, border_radius=15, text_color=BLACK, color=PURPLE, border_color=PURPLE, font_size=36)
        self.exit_btn = pg.Button(8, 400, 150, 50, "ВЫЙТИ", exit, border_radius=15, text_color=BLACK, color=PURPLE, border_color=PURPLE, font_size=36)
        
        self.sprites = [self.skybox, self.game_name, self.mother_bur, self.gull, self.gull_feed]
        self.ui = [self.start_btn, self.exit_btn]

        game.add_sprite(self.sprites)

    def update(self, dt):
        if self.gull_feed_visible:
            self.gull_feed_timer -= dt
            if self.gull_feed_timer <= 0:
                self.gull_feed_visible = False
                self.gull_feed.x = 1500
        
        for element in self.ui:
            element.update(game.get_delta_time())

        self.gull.x += 3 * dt * 60
        if self.gull.x >= 900:
            self.gull.x = -150
            self.gull.y = random.randint(20, 100)

        self.skybox.x += 0.1 * dt * 240
        if self.skybox.x >= 850:
            self.skybox.x = 50
    
    def draw(self, screen):
        screen.fill(BACKGROUND)

        for element in self.ui:
            element.draw(game.screen)
            
        for element in self.sprites:
            if element == self.gull_feed and not self.gull_feed_visible:
                continue
            screen.blit(element.image, element.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.gull.rect.collidepoint(mouse_pos) and not self.gull_feed_visible:
                self.gull_feed_visible = True
                self.gull_feed.x = 400
                self.gull_feed_timer = 1.5
                
        for element in self.ui:
            element.handle_event(event)

class GameScene1(Scene):
    def __init__(self):
        super().__init__("game_scene1")
        self.sprite = pg.AnimatedSprite("assets/scene1/rinpoche.png", (800, 600), (400, 300))
        self.speaker = pg.AnimatedSprite("assets/scene1/lama.png", (250, 328), (-50, 460))
        self.bao = pg.AnimatedSprite("assets/bao.png", (200, 200), (950, 330))
        self.bao.mirror(True)
        self.bao.add_animation("speak", [0, 1, 2, 3], loop=True, fps=5)
        self.text = pg.AnimatedSprite("assets/scene1/lama_text.png", (490, 95), (-150, 549))
        self.map = pg.AnimatedSprite("assets/map.png", (35, 33), (599, 540))
        
        self.player_text1 = pg.AnimatedSprite("assets/scene1/player_text1.png", (275, 110), (1500, 150))
        self.player_text2 = pg.AnimatedSprite("assets/scene1/player_text2.png", (245, 100), (1500, 150))
        self.player_text3 = pg.AnimatedSprite("assets/scene1/player_text3.png", (195, 100), (1500, 150))
        self.bao_text1 = pg.AnimatedSprite("assets/scene1/bao_text1.png", (200, 124), (1500, 300))        
        self.bao_text2 = pg.AnimatedSprite("assets/scene1/bao_text2.png", (177, 110), (1500, 300))     
        self.bao_text3 = pg.AnimatedSprite("assets/scene1/bao_text3.png", (300, 120), (1500, 300))  
        self.bao_text4 = pg.AnimatedSprite("assets/scene1/bao_text4.png", (213, 110), (1500, 300))  
        self.bao_text5 = pg.AnimatedSprite("assets/scene1/bao_text5.png", (250, 151), (1500, 280))  
        self.bao_text6 = pg.AnimatedSprite("assets/scene1/bao_text6.png", (250, 181), (1500, 260))  

        self.sprites = [self.sprite, self.speaker, self.text, self.map, self.bao,
                        self.player_text1, self.bao_text1, 
                        self.player_text2, self.bao_text2, 
                        self.player_text3, self.bao_text3,
                        self.bao_text4, self.bao_text5, self.bao_text6
                        ]
        
        game.add_sprite(self.sprites)
        
        self.s1_btn = pg.Button(579, 557, 40, 40, "1", text_color=BLACK, border_radius=15, color=GRAY, border_color=GRAY)
        self.s2_btn = pg.Button(624, 557, 40, 40, "2", scene2, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s3_btn = pg.Button(669, 557, 40, 40, "3", scene3, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s4_btn = pg.Button(714, 557, 40, 40, "4", scene4, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s5_btn = pg.Button(758, 557, 40, 40, "5", scene5, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.menu_btn = pg.Button(499, 557, 75, 40, "МЕНЮ", goto_menu, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE, font_size=30)
        self.next_btn = pg.Text(275, 30, "чтобы продолжить нажмите пробел", color=BLACK, size=20)
        self.location = pg.Text(240, 5, "ДАЦАН «РИНПОЧЕ БАГША»", color=BLACK, size=32)
        
        self.ui = [self.s1_btn, self.s2_btn, 
                   self.s3_btn, self.s4_btn, 
                   self.s5_btn, self.menu_btn, 
                   self.next_btn, self.location
                   ]
                
        self.f1_btn = pg.Button(random.randint(10, 350), random.randint(10, 40), 40, 40, "?", self.toggle_f1_text, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        self.f2_btn = pg.Button(random.randint(410, 750), random.randint(10, 40), 40, 40, "?", self.toggle_f2_text, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        
        self.f_btns = [self.f1_btn, self.f2_btn]
        self.f_btns_draw = False
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.show_hello_first_time = True
        
        self.f1_text = pg.AnimatedSprite("assets/scene1/f1_text.png", (287, 200), (270, 280))
        self.f2_text = pg.AnimatedSprite("assets/scene1/f2_text.png", (237, 200), (270, 280))
        self.hello = pg.AnimatedSprite("assets/scene1/hello.png", (275, 229), (260, 270))
        
        self.space_press_count = 0
        self.space_cooldown = 0
        self.bao_moving = False
        self.bao_animation_timer = 0
        self.bao_leave = False
        
        self.fact_system_active = False
        self.current_fact = None

        self.player_text1_sound = pygame.mixer.Sound('assets/scene1/player_text1.wav')
        self.player_text2_sound = pygame.mixer.Sound('assets/scene1/player_text2.wav')
        self.player_text3_sound = pygame.mixer.Sound('assets/scene1/player_text3.wav')
        self.bao_text1_sound = pygame.mixer.Sound('assets/scene1/bao_text1.wav')
        self.bao_text2_sound = pygame.mixer.Sound('assets/scene1/bao_text2.wav')
        self.bao_text3_sound = pygame.mixer.Sound('assets/scene1/bao_text3.wav')
        self.bao_text4_sound = pygame.mixer.Sound('assets/scene1/bao_text4.wav')
        self.bao_text5_sound = pygame.mixer.Sound('assets/scene1/bao_text5.wav')
        self.bao_text6_sound = pygame.mixer.Sound('assets/scene1/bao_text6.wav')

        self.hello_sound = pygame.mixer.Sound("assets/scene1/hello.wav")
        self.f1_sound = pygame.mixer.Sound("assets/scene1/f1_text.wav")
        self.f2_sound = pygame.mixer.Sound("assets/scene1/f2_text.wav")

    def toggle_f1_text(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f1'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f1_text_visible = True
                self.f2_text_visible = False
                self.f1_sound.play()

    def toggle_f2_text(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f2'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f2_text_visible = True
                self.f1_text_visible = False
                self.f2_sound.play()

    def show_fact(self):
        if self.current_fact == 'f1':
            self.f1_text_visible = True
            self.f2_text_visible = False
            self.f1_sound.play()
        else:
            self.f2_text_visible = True
            self.f1_text_visible = False
            self.f2_sound.play()
        self.hello_visible = False
        self.show_hello_first_time = False
        self.hello_sound.stop()

    def hide_facts(self):
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.fact_system_active = False
        self.current_fact = None
        self.f1_sound.stop()
        self.f2_sound.stop()
        self.hello_sound.stop()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.fact_system_active:
            if self.hello_visible:
                self.show_fact()
            else:
                self.hide_facts()
            return
                
        if self.f_btns_draw and not self.fact_system_active:
            for btn in self.f_btns:
                btn.handle_event(event)
  
        for element in self.ui:
            element.handle_event(event)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.space_cooldown > 0:
            self.space_cooldown -= dt

        if keys[pygame.K_SPACE] and self.space_cooldown <= 0:
            self.space_press_count += 1
            self.space_cooldown = space_cooldown
            
            if self.space_press_count == 1:
                self.player_text1_sound.play()
                self.player_text1.x = 150
            elif self.space_press_count == 2:
                self.player_text1.x = 1500
                self.player_text1_sound.stop()
                self.bao_moving = True
                self.bao_animation_timer = 1.0
                self.bao_text1_sound.play()   
            elif self.space_press_count == 3:
                self.bao_moving = False
                self.bao_text1.x = 1500
                self.bao_text1_sound.stop()
                self.bao.stop_animation()
                self.player_text2_sound.play()
                self.player_text2.x = 130
            elif self.space_press_count == 4:
                self.player_text2.x = 1500
                self.player_text2_sound.stop()
                self.bao.play_animation("speak")
                self.bao_text2_sound.play()
                self.bao_text2.x = 400
            elif self.space_press_count == 5:
                self.bao_text2.x = 1500
                self.bao_text2_sound.stop()
                self.bao.play_animation("speak")
                self.bao_text3_sound.play()
                self.bao_text3.x = 350
            elif self.space_press_count == 6:
                self.bao_text3.x = 1500
                self.bao_text3_sound.stop()
                self.bao.stop_animation()
                self.player_text3_sound.play()
                self.player_text3.x = 100
            elif self.space_press_count == 7:
                self.player_text3.x = 1500
                self.player_text3_sound.stop()
                self.bao.play_animation("speak")
                self.bao_text4_sound.play()
                self.bao_text4.x = 400
            elif self.space_press_count == 8:
                self.bao_text4.x = 1500
                self.bao_text4_sound.stop()
                self.bao_text5_sound.play()
                self.bao_text5.x = 380
            elif self.space_press_count == 9:
                self.bao_text5.x = 1500
                self.bao_text5_sound.stop()
                self.bao_text6_sound.play()
                self.bao_text6.x = 380
            elif self.space_press_count == 10:
                self.bao_text6.x = 1500
                self.bao_text6_sound.stop()
                self.bao.stop_animation()
                self.bao_leave = True
                self.f_btns_draw = True
                
        if self.bao_leave:
            if self.bao.x < 1500:
                self.bao.x += 400 * dt
                self.bao.rotate(-20)

        if self.bao_moving:
            if self.bao.x > 600:
                self.bao.x -= 400 * dt
                self.bao.rotate(20)
            if self.bao.x <= 600:
                self.bao.set_rotation(0)
                
            if self.bao_animation_timer > 0:
                self.bao_animation_timer -= dt
            elif not self.bao.is_animation_finished():
                self.bao.play_animation("speak")   
                self.bao_text1.x = 400 
                    
        for element in self.ui:
            element.update(game.get_delta_time())
        
        if self.f_btns_draw:
            for element in self.f_btns:
                element.update(game.get_delta_time())
        
        self.speaker.x += 5 * dt * 60
        if self.speaker.x >= 120:
            self.speaker.x = 120
            
        self.text.x += 8 * dt * 60
        if self.text.x >= 248:
            self.text.x = 248
                    
        if self.f1_text_visible or self.f2_text_visible or self.hello_visible:
            for element in [self.f1_text, self.f2_text, self.hello]:
                element.update(game.get_delta_time())
                    
    def draw(self, screen):
        screen.fill(BACKGROUND)

        for element in self.sprites:
            screen.blit(element.image, element.rect)

        for element in self.ui:
            element.draw(game.screen)

        if self.f_btns_draw:
            for element in self.f_btns:
                element.draw(game.screen)

        if self.hello_visible:
            screen.blit(self.hello.image, self.hello.rect)
        elif self.f1_text_visible:
            screen.blit(self.f1_text.image, self.f1_text.rect)
        elif self.f2_text_visible:
            screen.blit(self.f2_text.image, self.f2_text.rect)

class GameScene2(Scene):
    def __init__(self):
        super().__init__("game_scene2")
        self.sprite = pg.AnimatedSprite("assets/scene2/lenin.png", (800, 600), (400, 300))
        self.speaker = pg.AnimatedSprite("assets/scene2/shutenkov.png", (250, 273), (950, 464))
        self.text = pg.AnimatedSprite("assets/scene2/shutenkov_text.png", (352, 100), (1050, 545))
        self.map = pg.AnimatedSprite("assets/map.png", (35, 33), (145, 540))
    
        self.player_text1 = pg.AnimatedSprite("assets/scene2/player_text1.png", (229, 110), (1500, 400))
        self.player_text2 = pg.AnimatedSprite("assets/scene2/player_text2.png", (291, 120), (1500, 400))
        self.player_text3 = pg.AnimatedSprite("assets/scene2/player_text3.png", (200, 100), (1500, 400))
        self.player_text4 = pg.AnimatedSprite("assets/scene2/player_text4.png", (270, 120), (1500, 400))
        self.lenin_text1 = pg.AnimatedSprite("assets/scene2/lenin_text1.png", (219, 110), (1500, 300))        
        self.lenin_text2 = pg.AnimatedSprite("assets/scene2/lenin_text2.png", (220, 123), (1500, 320))     
        self.lenin_text3 = pg.AnimatedSprite("assets/scene2/lenin_text3.png", (229, 120), (1500, 320))  
        self.lenin_text4 = pg.AnimatedSprite("assets/scene2/lenin_text4.png", (175, 120), (1500, 310))  
    
        self.sprites = [self.sprite, self.speaker, self.text, self.map,
                        self.player_text1, self.lenin_text1, 
                        self.player_text2, self.lenin_text2, 
                        self.player_text3, self.lenin_text3,
                        self.player_text4, self.lenin_text4
                        ]
        
        game.add_sprite(self.sprites)
        
        self.s1_btn = pg.Button(80, 557, 40, 40, "1", scene1, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s2_btn = pg.Button(125, 557, 40, 40, "2", text_color=BLACK, border_radius=15, color=GRAY, border_color=GRAY)
        self.s3_btn = pg.Button(170, 557, 40, 40, "3", scene3, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s4_btn = pg.Button(215, 557, 40, 40, "4", scene4, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s5_btn = pg.Button(260, 557, 40, 40, "5", scene5, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.menu_btn = pg.Button(2, 557, 75, 40, "МЕНЮ", goto_menu, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE, font_size=30)
        self.next_btn = pg.Text(275, 30, "чтобы продолжить нажмите пробел", color=BLACK, size=20)
        self.location = pg.Text(140, 5, "ПЛОЩАДЬ СОВЕТОВ, ПАМЯТНИК В. И. ЛЕНИНУ", color=BLACK, size=32)
        
        self.ui = [self.s1_btn, self.s2_btn, 
                   self.s3_btn, self.s4_btn, 
                   self.s5_btn, self.menu_btn, 
                   self.next_btn, self.location
                   ]
        
        self.f1_btn = pg.Button(random.randint(10, 350), random.randint(90, 120), 40, 40, "?", self.on_f1_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        self.f2_btn = pg.Button(random.randint(410, 750), random.randint(90, 120), 40, 40, "?", self.on_f2_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        
        self.f_btns = [self.f1_btn, self.f2_btn]
        self.f_btns_draw = False
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.show_hello_first_time = True
        self.selected_fact = None
        self.waiting_for_space = False
        self.fact_system_active = False
        self.current_fact = None
        
        self.f1_text = pg.AnimatedSprite("assets/scene2/f1_text.png", (242, 160), (520, 350))
        self.f2_text = pg.AnimatedSprite("assets/scene2/f2_text.png", (241, 150), (520, 350))
        self.hello = pg.AnimatedSprite("assets/scene2/hello.png", (350, 151), (450, 350))
        
        self.space_press_count = 0
        self.space_cooldown = 0
        
        self.player_text1_sound = pygame.mixer.Sound("assets/scene2/player_text1.wav")
        self.player_text2_sound = pygame.mixer.Sound("assets/scene2/player_text2.wav")
        self.player_text3_sound = pygame.mixer.Sound("assets/scene2/player_text3.wav")
        self.player_text4_sound = pygame.mixer.Sound("assets/scene2/player_text4.wav")
        self.lenin_text1_sound = pygame.mixer.Sound("assets/scene2/lenin_text1.wav")
        self.lenin_text2_sound = pygame.mixer.Sound("assets/scene2/lenin_text2.wav")
        self.lenin_text3_sound = pygame.mixer.Sound("assets/scene2/lenin_text3.wav")
        self.lenin_text4_sound = pygame.mixer.Sound("assets/scene2/lenin_text4.wav")
        
        self.hello_sound = pygame.mixer.Sound("assets/scene2/hello.wav")
        self.f1_sound = pygame.mixer.Sound("assets/scene2/f1_text.wav")
        self.f2_sound = pygame.mixer.Sound("assets/scene2/f2_text.wav")
        
    def on_f1_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f1'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f1_text_visible = True
                self.f2_text_visible = False
                self.f1_sound.play()

    def on_f2_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f2'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f2_text_visible = True
                self.f1_text_visible = False
                self.f2_sound.play()

    def show_fact(self):
        if self.current_fact == 'f1':
            self.f1_text_visible = True
            self.f2_text_visible = False
            self.f1_sound.play()
        else:
            self.f2_text_visible = True
            self.f1_text_visible = False
            self.f2_sound.play()
        self.hello_visible = False
        self.show_hello_first_time = False
        self.hello_sound.stop()

    def hide_facts(self):
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.fact_system_active = False
        self.current_fact = None
        self.f1_sound.stop()
        self.f2_sound.stop()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.fact_system_active:
            if self.hello_visible:
                self.show_fact()
            else:
                self.hide_facts()
            return
            
        if self.f_btns_draw and not self.fact_system_active:
            for btn in self.f_btns:
                btn.handle_event(event)
        
        for element in self.ui:
            element.handle_event(event)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if not self.waiting_for_space:
            
            if self.space_cooldown > 0:
                self.space_cooldown -= dt
                
            if keys[pygame.K_SPACE] and self.space_cooldown <= 0:
                self.space_press_count += 1
                self.space_cooldown = space_cooldown

                if self.space_press_count == 1:
                    self.player_text1.x = 120
                    self.player_text1_sound.play()
                elif self.space_press_count == 2:
                    self.player_text1.x = 1500
                    self.player_text1_sound.stop()
                    self.player_text2_sound.play()
                    self.player_text2.x = 150
                elif self.space_press_count == 3:
                    self.player_text2.x = 1500
                    self.player_text2_sound.stop()
                    self.lenin_text1_sound.play()
                    self.lenin_text1.x = 220
                elif self.space_press_count == 4:
                    self.lenin_text1.x = 1500
                    self.lenin_text1_sound.stop()
                    self.player_text3_sound.play()
                    self.player_text3.x = 100
                elif self.space_press_count == 5:
                    self.player_text3.x = 1500
                    self.player_text3_sound.stop()
                    self.lenin_text2_sound.play()
                    self.lenin_text2.x = 220
                elif self.space_press_count == 6:
                    self.lenin_text2.x = 1500
                    self.lenin_text2_sound.stop()
                    self.player_text4_sound.play()
                    self.player_text4.x = 140
                elif self.space_press_count == 7:
                    self.player_text4.x = 1500
                    self.player_text4_sound.stop()
                    self.lenin_text3_sound.play()
                    self.lenin_text3.x = 220
                elif self.space_press_count == 8:
                    self.lenin_text3.x = 1500
                    self.lenin_text3_sound.stop()
                    self.lenin_text4_sound.play()
                    self.lenin_text4.x = 240
                elif self.space_press_count == 9:
                    self.lenin_text4.x = 1500
                    self.lenin_text4_sound.stop()
                    self.f_btns_draw = True
         
        for element in self.ui:
            element.update(game.get_delta_time())
        
        if self.f_btns_draw:
            for element in self.f_btns:
                element.update(game.get_delta_time())
        
        self.speaker.x -= 5 * dt * 60
        if self.speaker.x <= 680:
            self.speaker.x = 680
            
        self.text.x -= 8 * dt * 60
        if self.text.x <= 620:
            self.text.x = 620
    
        if self.f1_text_visible or self.f2_text_visible or self.hello_visible:
            for element in [self.f1_text, self.f2_text, self.hello]:
                element.update(game.get_delta_time())
    
    def draw(self, screen):
        screen.fill(BACKGROUND)
        
        for element in self.sprites:
            screen.blit(element.image, element.rect)
            
        for element in self.ui:
            element.draw(game.screen)

        if self.f_btns_draw:
            for element in self.f_btns:
                element.draw(game.screen)

        if self.hello_visible:
            screen.blit(self.hello.image, self.hello.rect)
        elif self.f1_text_visible:
            screen.blit(self.f1_text.image, self.f1_text.rect)
        elif self.f2_text_visible:
            screen.blit(self.f2_text.image, self.f2_text.rect)

class GameScene3(Scene):
    def __init__(self):
        super().__init__("game_scene3")
        self.sprite = pg.AnimatedSprite("assets/scene3/cathedral.png", (800, 600), (400, 300))
        self.speaker = pg.AnimatedSprite("assets/scene3/cleric.png", (250, 313), (950, 460))
        self.text = pg.AnimatedSprite("assets/scene3/cleric_text.png", (483, 85), (1150, 553))
        self.map = pg.AnimatedSprite("assets/map.png", (35, 33), (190, 540)) 
    
        self.sprites = [self.sprite, self.speaker, self.text, self.map]
        
        game.add_sprite(self.sprites)
        
        self.s1_btn = pg.Button(80, 557, 40, 40, "1", scene1, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s2_btn = pg.Button(125, 557, 40, 40, "2", scene2, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s3_btn = pg.Button(170, 557, 40, 40, "3", text_color=BLACK, border_radius=15, color=GRAY, border_color=GRAY)
        self.s4_btn = pg.Button(215, 557, 40, 40, "4", scene4, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s5_btn = pg.Button(260, 557, 40, 40, "5", scene5, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.menu_btn = pg.Button(2, 557, 75, 40, "МЕНЮ", goto_menu, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE, font_size=30)
        self.next_btn = pg.Text(275, 30, "чтобы продолжить нажмите пробел", color=BLACK, size=20)
        self.location = pg.Text(115, 5, "СВЯТО-ОДИГИТРИЕВСКИЙ КАФЕДРАЛЬНЫЙ СОБОР", color=BLACK, size=32)
        
        self.ui = [self.s1_btn, self.s2_btn, 
                   self.s3_btn, self.s4_btn, 
                   self.s5_btn, self.menu_btn, 
                   self.next_btn, self.location
                   ]

        self.f1_btn = pg.Button(random.randint(10, 350), random.randint(330, 360), 40, 40, "?", self.on_f1_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        self.f2_btn = pg.Button(random.randint(410, 750), random.randint(330, 360), 40, 40, "?", self.on_f2_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        
        self.f_btns = [self.f1_btn, self.f2_btn]
        self.f_btns_draw = True  # Кнопки видны сразу
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.show_hello_first_time = True
        self.fact_system_active = False
        self.current_fact = None

        self.f1_text = pg.AnimatedSprite("assets/scene3/f1_text.png", (258, 200), (480, 300))
        self.f2_text = pg.AnimatedSprite("assets/scene3/f2_text.png", (241, 200), (480, 300))
        self.hello = pg.AnimatedSprite("assets/scene3/hello.png", (225, 100), (500, 350))
        
        self.hello_sound = pygame.mixer.Sound("assets/scene3/hello.wav")
        self.f1_sound = pygame.mixer.Sound("assets/scene3/f1_text.wav")
        self.f2_sound = pygame.mixer.Sound("assets/scene3/f2_text.wav")
        
    def on_f1_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f1'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f1_text_visible = True
                self.f2_text_visible = False
                self.f1_sound.play()

    def on_f2_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f2'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f2_text_visible = True
                self.f1_text_visible = False
                self.f2_sound.play()

    def show_fact(self):
        if self.current_fact == 'f1':
            self.f1_text_visible = True
            self.f2_text_visible = False
            self.f1_sound.play()
        else:
            self.f2_text_visible = True
            self.f1_text_visible = False
            self.f2_sound.play()
        self.hello_visible = False
        self.show_hello_first_time = False
        self.hello_sound.stop()

    def hide_facts(self):
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.fact_system_active = False
        self.current_fact = None
        self.f1_sound.stop()
        self.f2_sound.stop()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.fact_system_active:
            if self.hello_visible:
                self.show_fact()
            else:
                self.hide_facts()
            return
            
        if self.f_btns_draw and not self.fact_system_active:
            for btn in self.f_btns:
                btn.handle_event(event)
        
        for element in self.ui:
            element.handle_event(event)
        
    def update(self, dt):        
        for element in self.ui:
            element.update(game.get_delta_time())
        
        self.speaker.x -= 5 * dt * 60
        if self.speaker.x <= 680:
            self.speaker.x = 680
        
        self.text.x -= 8 * dt * 60
        if self.text.x <= 555:
            self.text.x = 555
        
        if self.f_btns_draw:
            for element in self.f_btns:
                element.update(game.get_delta_time())
    
        if self.f1_text_visible or self.f2_text_visible or self.hello_visible:
            for element in [self.f1_text, self.f2_text, self.hello]:
                element.update(game.get_delta_time())
    
    def draw(self, screen):
        screen.fill(BACKGROUND)
        
        for element in self.sprites:
            screen.blit(element.image, element.rect)
            
        for element in self.ui:
            element.draw(game.screen)

        if self.f_btns_draw:
            for element in self.f_btns:
                element.draw(game.screen)

        if self.hello_visible:
            screen.blit(self.hello.image, self.hello.rect)
        elif self.f1_text_visible:
            screen.blit(self.f1_text.image, self.f1_text.rect)
        elif self.f2_text_visible:
            screen.blit(self.f2_text.image, self.f2_text.rect)

class GameScene4(Scene):
    def __init__(self):
        super().__init__("game_scene4")
        self.sprite = pg.AnimatedSprite("assets/scene4/memorial.png", (800, 600), (400, 300))
        self.speaker = pg.AnimatedSprite("assets/scene4/ludupova.png", (200, 481), (-50, 460))
        self.bao = pg.AnimatedSprite("assets/bao.png", (200, 200), (950, 420))
        self.bao.mirror(True)
        self.bao.add_animation("speak", [0, 1, 2, 3], loop=True, fps=5)
        self.text = pg.AnimatedSprite("assets/scene4/ludupova_text.png", (456, 100), (-250, 548))
        self.map = pg.AnimatedSprite("assets/map.png", (35, 33), (734, 540))
    
        self.player_text1 = pg.AnimatedSprite("assets/scene4/player_text1.png", (205, 140), (1500, 150))
        self.bao_text1 = pg.AnimatedSprite("assets/scene4/bao_text1.png", (203, 120), (1500, 380))        
        self.bao_text2 = pg.AnimatedSprite("assets/scene4/bao_text2.png", (333, 150), (1500, 380))     
        self.bao_text3 = pg.AnimatedSprite("assets/scene4/bao_text3.png", (246, 150), (1500, 380))  
    
        self.sprites = [self.sprite, self.speaker, self.text, self.map, self.bao,
                       self.player_text1, self.bao_text1, 
                       self.bao_text2, self.bao_text3
                       ]
        
        game.add_sprite(self.sprites)
        
        self.s1_btn = pg.Button(579, 557, 40, 40, "1", scene1, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s2_btn = pg.Button(624, 557, 40, 40, "2", scene2, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s3_btn = pg.Button(669, 557, 40, 40, "3", scene3, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s4_btn = pg.Button(714, 557, 40, 40, "4", text_color=BLACK, border_radius=15, color=GRAY, border_color=GRAY)
        self.s5_btn = pg.Button(758, 557, 40, 40, "5", scene5, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.menu_btn = pg.Button(499, 557, 75, 40, "МЕНЮ", goto_menu, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE, font_size=30)
        self.next_btn = pg.Text(275, 30, "чтобы продолжить нажмите пробел", color=BLACK, size=20)
        self.location = pg.Text(140, 5, "ПАМЯТНИК ТРУЖЕНИКАМ ТЫЛА И ДЕТЯМ ВОЙНЫ", color=BLACK, size=32)
        
        self.ui = [self.s1_btn, self.s2_btn, 
                   self.s3_btn, self.s4_btn, 
                   self.s5_btn, self.menu_btn, 
                   self.next_btn, self.location
                   ]

        self.f1_btn = pg.Button(random.randint(10, 350), random.randint(170, 200), 40, 40, "?", self.on_f1_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        self.f2_btn = pg.Button(random.randint(410, 750), random.randint(170, 200), 40, 40, "?", self.on_f2_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        
        self.f_btns = [self.f1_btn, self.f2_btn]
        self.f_btns_draw = False
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.show_hello_first_time = True
        self.fact_system_active = False
        self.current_fact = None

        self.f1_text = pg.AnimatedSprite("assets/scene4/f1_text.png", (199, 130), (220, 260))
        self.f2_text = pg.AnimatedSprite("assets/scene4/f2_text.png", (217, 120), (220, 260))
        self.hello = pg.AnimatedSprite("assets/scene4/hello.png", (300, 160), (270, 250))
        
        self.space_press_count = 0
        self.space_cooldown = 0
        self.bao_moving = False
        self.bao_animation_timer = 0
        self.bao_leave = False

        self.player_text1_sound = pygame.mixer.Sound("assets/scene4/player_text1.wav")
        self.bao_text1_sound = pygame.mixer.Sound("assets/scene4/bao_text1.wav")
        self.bao_text2_sound = pygame.mixer.Sound("assets/scene4/bao_text2.wav")
        self.bao_text3_sound = pygame.mixer.Sound("assets/scene4/bao_text3.wav")

        self.hello_sound = pygame.mixer.Sound("assets/scene4/hello.wav")
        self.f1_sound = pygame.mixer.Sound("assets/scene4/f1_text.wav")
        self.f2_sound = pygame.mixer.Sound("assets/scene4/f2_text.wav")

    def on_f1_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f1'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f1_text_visible = True
                self.f2_text_visible = False
                self.f1_sound.play()

    def on_f2_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f2'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f2_text_visible = True
                self.f1_text_visible = False
                self.f2_sound.play()

    def show_fact(self):
        if self.current_fact == 'f1':
            self.f1_text_visible = True
            self.f2_text_visible = False
            self.f1_sound.play()
        else:
            self.f2_text_visible = True
            self.f1_text_visible = False
            self.f2_sound.play()
        self.hello_visible = False
        self.show_hello_first_time = False
        self.hello_sound.stop()

    def hide_facts(self):
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.fact_system_active = False
        self.current_fact = None
        self.f1_sound.stop()
        self.f2_sound.stop()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.fact_system_active:
            if self.hello_visible:
                self.show_fact()
            else:
                self.hide_facts()
            return
            
        if self.f_btns_draw and not self.fact_system_active:
            for btn in self.f_btns:
                btn.handle_event(event)
        
        for element in self.ui:
            element.handle_event(event)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.space_cooldown > 0:
            self.space_cooldown -= dt

        if keys[pygame.K_SPACE] and self.space_cooldown <= 0:
            self.space_press_count += 1
            self.space_cooldown = space_cooldown
            
            if self.space_press_count == 1:
                self.bao_moving = True
                self.bao_animation_timer = 1.0
                self.bao_text1_sound.play()
            elif self.space_press_count == 2:
                self.bao_moving = False
                self.bao_text1.x = 1500
                self.bao_text1_sound.stop()
                self.bao_text2_sound.play()
                self.bao_text2.x = 420
            elif self.space_press_count == 3:
                self.bao_text2.x = 1500
                self.bao.stop_animation()
                self.bao_text2_sound.stop()
                self.player_text1_sound.play()
                self.player_text1.x = 110
            elif self.space_press_count == 4:
                self.player_text1.x = 1500
                self.player_text1_sound.stop()
                self.bao.play_animation("speak")
                self.bao_text3_sound.play()
                self.bao_text3.x = 460
            elif self.space_press_count == 5:
                self.bao_text3.x = 1500
                self.bao.stop_animation()
                self.bao_text3_sound.stop()
                self.bao_leave = True
                self.f_btns_draw = True

        if self.bao_leave:
            if self.bao.x < 1500:
                self.bao.x += 400 * dt
                self.bao.rotate(-25)

        if self.bao_moving:
            if self.bao.x > 680:
                self.bao.x -= 400 * dt
                self.bao.rotate(25)
            if self.bao.x <= 680:
                self.bao.set_rotation(0)

            if self.bao_animation_timer > 0:
                self.bao_animation_timer -= dt
            elif not self.bao.is_animation_finished():
                self.bao.play_animation("speak")   
                self.bao_text1.x = 480    

        for element in self.ui:
            element.update(game.get_delta_time())
        
        if self.f_btns_draw:
            for element in self.f_btns:
                element.update(game.get_delta_time())
        
        self.speaker.x += 5 * dt * 60
        if self.speaker.x >= 80:
            self.speaker.x = 80
            
        self.text.x += 8 * dt * 60
        if self.text.x >= 233:
            self.text.x = 233
    
        if self.f1_text_visible or self.f2_text_visible or self.hello_visible:
            for element in [self.f1_text, self.f2_text, self.hello]:
                element.update(game.get_delta_time())
    
    def draw(self, screen):
        screen.fill(BACKGROUND)
        
        for element in self.sprites:
            screen.blit(element.image, element.rect)
            
        for element in self.ui:
            element.draw(game.screen)

        if self.f_btns_draw:
            for element in self.f_btns:
                element.draw(game.screen)

        if self.hello_visible:
            screen.blit(self.hello.image, self.hello.rect)
        elif self.f1_text_visible:
            screen.blit(self.f1_text.image, self.f1_text.rect)
        elif self.f2_text_visible:
            screen.blit(self.f2_text.image, self.f2_text.rect)

class GameScene5(Scene):
    def __init__(self):
        super().__init__("game_scene5")
        self.sprite = pg.AnimatedSprite("assets/scene5/baikal.png", (800, 600), (400, 300))
        self.sprite.add_animation("waves", [0, 1, 2, 1], fps=1, loop=True)
        self.sprite.play_animation("waves")
        self.speaker = pg.AnimatedSprite("assets/scene5/tsydenov_speaker.png", (240, 360), (950, 460))
        self.text = pg.AnimatedSprite("assets/scene5/tsydenov_text.png", (490, 99), (1050, 546))
        self.map = pg.AnimatedSprite("assets/map.png", (35, 33), (280, 540))
        self.seal=pg.AnimatedSprite("assets/scene5/seal.png", (415, 256), (200, 300))
        self.seal.set_scale(0.3)
        self.seal.add_animation("swim", [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], loop=True)
        self.seal.play_animation("swim")
    
        self.sprites = [self.sprite, self.speaker, self.text, self.map, self.seal]
        
        game.add_sprite(self.sprites)
        
        self.s1_btn = pg.Button(80, 557, 40, 40, "1", scene1, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s2_btn = pg.Button(125, 557, 40, 40, "2", scene2, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s3_btn = pg.Button(170, 557, 40, 40, "3", scene3, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s4_btn = pg.Button(215, 557, 40, 40, "4", scene4, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE)
        self.s5_btn = pg.Button(260, 557, 40, 40, "5", text_color=BLACK, border_radius=15, color=GRAY, border_color=GRAY)
        self.menu_btn = pg.Button(2, 557, 75, 40, "МЕНЮ", goto_menu, text_color=BLACK, border_radius=15, color=PURPLE, border_color=PURPLE, font_size=30)
        self.next_btn = pg.Text(275, 30, "чтобы продолжить нажмите пробел", color=BLACK, size=20)
        self.location = pg.Text(300, 5, "ОЗЕРО БАЙКАЛ", color=BLACK, size=32)
        
        self.ui = [self.s1_btn, self.s2_btn, 
                   self.s3_btn, self.s4_btn, 
                   self.s5_btn, self.menu_btn, 
                   self.next_btn, self.location
                   ]

        self.f1_btn = pg.Button(random.randint(10, 190), random.randint(250, 280), 40, 40, "?", self.on_f1_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        self.f2_btn = pg.Button(random.randint(410, 750), random.randint(250, 280), 40, 40, "?", self.on_f2_click, 
                               text_color=BLACK, border_radius=15, 
                               color=PURPLE, border_color=PURPLE)
        
        self.f_btns = [self.f1_btn, self.f2_btn]
        self.f_btns_draw = True
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.show_hello_first_time = True
        self.fact_system_active = False
        self.current_fact = None

        self.f1_text = pg.AnimatedSprite("assets/scene5/f1_text.png", (250, 180), (490, 320))
        self.f2_text = pg.AnimatedSprite("assets/scene5/f2_text.png", (215, 120), (500, 370))
        self.hello = pg.AnimatedSprite("assets/scene5/hello.png", (250, 181), (480, 350))

        self.hello_sound = pygame.mixer.Sound("assets/scene5/hello.wav")
        self.f1_sound = pygame.mixer.Sound("assets/scene5/f1_text.wav")
        self.f2_sound = pygame.mixer.Sound("assets/scene5/f2_text.wav")

    def on_f1_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f1'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f1_text_visible = True
                self.f2_text_visible = False
                self.f1_sound.play()

    def on_f2_click(self):
        if not self.fact_system_active:
            self.fact_system_active = True
            self.current_fact = 'f2'
            if self.show_hello_first_time:
                self.hello_visible = True
                self.hello_sound.play()
            else:
                self.f2_text_visible = True
                self.f1_text_visible = False
                self.f2_sound.play()

    def show_fact(self):
        if self.current_fact == 'f1':
            self.f1_text_visible = True
            self.f2_text_visible = False
            self.f1_sound.play()
        else:
            self.f2_text_visible = True
            self.f1_text_visible = False
            self.f2_sound.play()
        self.hello_visible = False
        self.show_hello_first_time = False
        self.hello_sound.stop()

    def hide_facts(self):
        self.f1_text_visible = False
        self.f2_text_visible = False
        self.hello_visible = False
        self.fact_system_active = False
        self.current_fact = None
        self.f1_sound.stop()
        self.f2_sound.stop()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.fact_system_active:
            if self.hello_visible:
                self.show_fact()
            else:
                self.hide_facts()
            return
            
        if self.f_btns_draw and not self.fact_system_active:
            for btn in self.f_btns:
                btn.handle_event(event)
        
        for element in self.ui:
            element.handle_event(event)
        
    def update(self, dt):        
        for element in self.ui:
            element.update(game.get_delta_time())
        
        if self.f_btns_draw:
            for element in self.f_btns:
                element.update(game.get_delta_time())
        
        self.speaker.x -= 5 * dt * 60
        if self.speaker.x <= 680:
            self.speaker.x = 680
    
        self.text.x -= 8 * dt * 60
        if self.text.x <= 550:
            self.text.x = 550
    
        if self.f1_text_visible or self.f2_text_visible or self.hello_visible:
            for element in [self.f1_text, self.f2_text, self.hello]:
                element.update(game.get_delta_time())
    
    def draw(self, screen):
        screen.fill(BACKGROUND)
        
        for element in self.sprites:
            screen.blit(element.image, element.rect)
            
        for element in self.ui:
            element.draw(game.screen)

        if self.f_btns_draw:
            for element in self.f_btns:
                element.draw(game.screen)

        if self.hello_visible:
            screen.blit(self.hello.image, self.hello.rect)
        elif self.f1_text_visible:
            screen.blit(self.f1_text.image, self.f1_text.rect)
        elif self.f2_text_visible:
            screen.blit(self.f2_text.image, self.f2_text.rect)

menu_scene = MenuScene()
game_scene1 = GameScene1()
game_scene2 = GameScene2()
game_scene3 = GameScene3()
game_scene4 = GameScene4()
game_scene5 = GameScene5()

scene_manager.add_scene(menu_scene)
scene_manager.add_scene(game_scene1)
scene_manager.add_scene(game_scene2)
scene_manager.add_scene(game_scene3)
scene_manager.add_scene(game_scene4)
scene_manager.add_scene(game_scene5)

scene_manager.switch_to("menu")


bg_music = pygame.mixer.Sound("assets/Guidence.ogg")
bg_music.set_volume(0.1)
bg_music.play(-1)


def handle_event_menu(event):
    menu_scene.handle_event(event)

game.add_event_callback(handle_event_menu)

def handle_event1(event):
    game_scene1.handle_event(event)

game.add_event_callback(handle_event1)

def handle_event2(event):
    game_scene2.handle_event(event)

game.add_event_callback(handle_event2)

def handle_event3(event):
    game_scene3.handle_event(event)

game.add_event_callback(handle_event3)

def handle_event4(event):
    game_scene4.handle_event(event)

game.add_event_callback(handle_event4)

def handle_event5(event):
    game_scene5.handle_event(event)

game.add_event_callback(handle_event5)


def update():
    dt = game.get_delta_time()
    scene_manager.update(dt)

def draw():
    scene_manager.draw(game.screen)

game.run(update, draw)
