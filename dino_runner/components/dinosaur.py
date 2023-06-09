import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING


X_POS = 80
Y_POS = 310
Y_POSITION_DUCK = 340
VEL_JUMP = 9.5

class Dinosaur:
    def __init__(self) -> None:
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = VEL_JUMP
        self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] #Operador ternario
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index +=1
        


    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - VEL_JUMP:
            self.dino_jump = False
            self.jump_vel = VEL_JUMP


    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (user_input[pygame.K_DOWN] or self.dino_jump):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POSITION_DUCK
        self.step_index +=1

        
