# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:09:09 2024

@author: cmj17
"""

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
        self.setSize(30,30)
        
        self.gun = Gun(self.scene, self)
        self.gun.setPosition(0, -15)
    
    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.turnBy(5)
        if self.isKeyPressed(pygame.K_d):
            self.turnBy(-5)
        if self.isKeyPressed(pygame.K_w):
            self.forward(5)
        if self.isKeyPressed(pygame.K_s):
            self.forward(-3)




class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("Bullet.png")
        self.setSize(5,5)
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        self.show()
        self.position = self.parent.position
        self.moveAngle = self.parent.imageAngle
        self.speed = 20


class Gun(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("GunTurret.png")
        self.setBoundAction(self.HIDE)
        




class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.tank = Tank1(self)
        self.gun = Gun(self)
        
        self.sprites = [self.tank, self.gun]

        self.NUM_BULLETS = 100
        self.currentBullet = 0
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.tank))
                                
        self.sprites = [self.tank, self.bullets]

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentBullet += 1
                if self.currentBullet >= self.NUM_BULLETS:
                    self.currentBullet = 0
                self.bullets[self.currentBullet].fire()
        
        
        
        
        
def main():
    game = Game()
    game.start()
    
    
main()
