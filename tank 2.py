

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
        self.position = (75,250)
        
    
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
        self.position = (565,250)
        
    
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
        
        self.barriers = [Barrier(self, (25, 455)),
                         Barrier(self, (25, 25)),
                         Barrier(self, (75, 455)),
                         Barrier(self, (75, 25)),
                         Barrier(self, (125, 455)),
                         Barrier(self, (125, 25)),
                         Barrier(self, (175, 455)),
                         Barrier(self, (175, 25)),
                         Barrier(self, (225, 25)),
                         Barrier(self, (225, 455)),
                         Barrier(self, (275, 25)),
                         Barrier(self, (275, 455)),
                         Barrier(self, (325, 25)),
                         Barrier(self, (325, 455)),
                         Barrier(self, (375, 25)),
                         Barrier(self, (375, 455)),
                         Barrier(self, (425, 25)),
                         Barrier(self, (425, 455)),
                         Barrier(self, (475, 25)),
                         Barrier(self, (475, 455)),
                         Barrier(self, (525, 25)),
                         Barrier(self, (525, 455)),
                         Barrier(self, (575, 25)),
                         Barrier(self, (575, 455)),
                         Barrier(self, (625, 25)),
                         Barrier(self, (625, 455)),
                         
                         Barrier(self, (25, 75)),
                         Barrier(self, (615, 75)),
                         Barrier(self, (25, 125)),
                         Barrier(self, (615, 125)),
                         Barrier(self, (25, 175)),
                         Barrier(self, (615, 175)),
                         Barrier(self, (25, 225)),
                         Barrier(self, (615, 225)),
                         Barrier(self, (25, 275)),
                         Barrier(self, (615, 275)),
                         Barrier(self, (25, 325)),
                         Barrier(self, (615, 325)),
                         Barrier(self, (25, 375)),
                         Barrier(self, (615, 375)),
                         Barrier(self, (25, 425)),
                         Barrier(self, (615, 425))
                         ]

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
        self.colorRect("yellow", (50, 50))
        










def main():
    game = Game()
    game.start()
    
    
main()
