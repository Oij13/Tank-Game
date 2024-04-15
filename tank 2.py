

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
        

        

            
        for barrier in self.scene.barriers:
                       
            angle = self.moveAngle % 360
            if angle < 90 and angle > -90 :
                dir = "right"
            elif angle < 180 and angle > 0:
                dir = "up"
            elif angle < 270 and angle > 90:
                dir = "left"
            elif angle < 360 and angle >180:
                dir = "down"
            else:
                dir = "right"
        
            if self.collidesWith(self.barrier.color("yellow")):
                if dir == "right" and self.isKeyPressed(pygame.K_w):
                    if self.right > barrier.left:
                        self.right = barrier.left  
                        self.speed = 0
                if dir == "right" and self.isKeyPressed(pygame.K_s):
                    if self.left < barrier.right:
                        self.left = barrier.right  
                        self.speed = 0
                if dir == "left":
                    if self.left < barrier.right:
                        self.left = barrier.right 
                        self.speed = 0    
                if dir == "left":
                    if self.right > barrier.left:
                        self.right = barrier.left 
                        self.speed = 0    
                if dir == "down":
                    if self.bottom > barrier.top:
                        self.bottom = barrier.top 
                        self.speed = 0
                if dir == "down":
                    if self.top < barrier.bottom:
                        self.top = barrier.bottom 
                        self.speed = 0
                if dir == "up":
                    if self.top < barrier.bottom:
                        self.top = barrier.bottom 
                        self.speed = 0
                if dir == "up":
                    if self.bottom > barrier.top:
                        self.bottom = barrier.top 
                        self.speed = 0






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
            
        for barrier in self.scene.barriers:
            angle = self.moveAngle % 360
            if angle <= 45:
                dir = "right"
            elif angle <= 135:
                dir = "up"
            elif angle <= 225:
                dir = "left"
            elif angle <= 315:
                dir = "down"
            else:
                dir = "right"
            
        
            if self.collidesWith(barrier):
                if dir == "right":
                    if self.right > barrier.left:
                        self.right = barrier.left
                        self.speed = 0
                if dir == "left":
                    if self.left < barrier.right:
                        self.left = barrier.right
                        self.speed = 0
                if dir == "down":
                    if self.bottom > barrier.top:
                        self.bottom = barrier.top
                        self.speed = 0
                if dir == "up":
                    if self.top < barrier.bottom:
                        self.top = barrier.bottom
                        self.speed = 0



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
    def process(self):
        for barrier in self.scene.barriers:
            if self.collidesWith(barrier):
                self.hide()

    
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
        
        self.barriers = []
        for i in range(13):
            newWall = Barrier(self)
            newWall.y = 25
            newWall.x = i * 50
            self.barriers.append(newWall)
        for i in range(13):
            newBarrier = Barrier(self)
            newBarrier.y = 455
            newBarrier.x = i * 50
            self.barriers.append(newBarrier)
        for i in range(13):
            newBarrier = Barrier(self)
            newBarrier.y = i * 50
            newBarrier.x = 25
            self.barriers.append(newBarrier)
        for i in range(13):
            newBarrier = Barrier(self)
            newBarrier.y = i * 50
            newBarrier.x = 615
            self.barriers.append(newBarrier)
        #self.barriers.append(Barrier(self, (625, 455)))
        newBarrier = Barrier(self)
        newBarrier.y = 455
        newBarrier.x = 615
        self.barriers.append(newBarrier)
    
        
        
        """self.barriers = [Barrier(self, (25, 455)),
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
                         Barrier(self, (615, 425)),
                         
                         Barrier(self, (200, 125)),
                         Barrier(self, (200, 175)),
                         Barrier(self, (200, 75)),
                         Barrier(self, (250, 175)),
                         Barrier(self, (450, 405)),
                         Barrier(self, (450, 355)),
                         Barrier(self, (450, 305)),
                         Barrier(self, (400, 305)),
                         Barrier(self, (200, 305)),
                         Barrier(self, (450, 175)),

                         
                         ]"""

        self.sprites = [self.tank1, self.bullet1, self.tank2, self.bullet2, self.barriers]
        
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.bullet1.fire()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.bullet2.fire()    
        
    



class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("yellow", (50, 50))
        










def main():
    game = Game()
    game.start()
    
    
main()
