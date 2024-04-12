

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:33:38 2024

@author: owen.johnson3
"""

import pygame, simpleGE

class Tank1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Tank.png")
        self.setSize(40,40)
        self.position = (60,250)
        
    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.turnBy(3)
        if self.isKeyPressed(pygame.K_d):
            self.turnBy(-3)
        if self.isKeyPressed(pygame.K_w):
            self.forward(3)
        if self.isKeyPressed(pygame.K_s):
            self.forward(-3)





class Tank2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Redtank.png")
        self.setSize(40,40)
        self.position = (560,250)
        
    
    def process(self):
        if self.isKeyPressed(pygame.K_j):
            self.turnBy(3)
        if self.isKeyPressed(pygame.K_l):
            self.turnBy(-3)
        if self.isKeyPressed(pygame.K_i):
            self.forward(-3)
        if self.isKeyPressed(pygame.K_k):
            self.forward(3)


class Bullet1(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("Bullet.png")
        self.setSize(5,5)
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed = 20

    
class Bullet2(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("Bullet.png")
        self.setSize(5,5)
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed = -20


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.tank1 = Tank1(self)
        self.bullet1 = Bullet1(self, self.tank1)
        self.setImage("RockBG.png")
        self.tank2 = Tank2(self)
        self.bullet2 = Bullet2(self, self.tank2)
        
        self.barriers = [Barrier(self, (325, 470)),
                         Barrier(self, (325, 10))]

        self.sprites = [self.tank1, self.bullet1, self.tank2, self.bullet2, self.barriers]
        
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.bullet1.fire()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.bullet2.fire()    
        
    



class Barrier(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.colorRect("yellow", (650, 25))
        










def main():
    game = Game()
    game.start()
    
    
main()
