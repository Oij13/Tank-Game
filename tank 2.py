

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:33:38 2024

@author: owen.johnson3
"""

import pygame, simpleGE

class Tank(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Tank.png")
        self.setSize(40,40)
        self.position = (75,250)
        
        

    def process(self):   

            
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
        
            if self.collidesWith(barrier):
                if dir == "right":
                    if self.right > barrier.left:
                        self.right = barrier.left  
                        self.speed = 0
                if dir == "right":
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






"""class Tank2(simpleGE.Sprite):
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
                        self.speed = 0"""



class Bullet(simpleGE.Sprite):
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
                self.reset()
    
    def reset(self):
        self.dx = 0
        self.dy = 0
        self.hide()



class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
        
        
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.tank1 = Tank(self)
        self.bullet1 = Bullet(self, self.tank1)
        self.setImage("RockBG.png")
        self.tank2 = Tank(self)
        self.tank2.setAngle(180)
        self.tank2.setImage("Redtank.png")
        self.tank2.position = (565,250)
        self.score = 0
        self.lblScore = LblScore()
        self.tank2.setSize(40, 40)
        self.bullet2 = Bullet(self, self.tank2)
        
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
        newBarrier = Barrier(self)
        newBarrier.y = 455
        newBarrier.x = 615
        self.barriers.append(newBarrier)
    

        self.sprites = [self.tank1, self.bullet1, self.tank2, self.bullet2, self.barriers]
        
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.bullet1.fire()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.bullet2.fire()    
        
    def process(self):
        if self.tank2.isKeyPressed(pygame.K_j):
            self.tank2.turnBy(3)
        if self.tank2.isKeyPressed(pygame.K_l):
            self.tank2.turnBy(-3)
        if self.tank2.isKeyPressed(pygame.K_i):
            self.tank2.forward(3)
        if self.tank2.isKeyPressed(pygame.K_k):
            self.tank2.forward(-3)
            
        if self.tank1.isKeyPressed(pygame.K_a):
            self.tank1.turnBy(3)
        if self.tank1.isKeyPressed(pygame.K_d):
            self.tank1.turnBy(-3)
        if self.tank1.isKeyPressed(pygame.K_w):
            self.tank1.forward(3)
        if self.tank1.isKeyPressed(pygame.K_s):
            self.tank1.forward(-3)
        

        if self.bullet1.collidesWith(self.tank2):
            self.bullet1.show()
            self.score += 1
            self.bullet1.hide
            self.lblScore.text = f"Score: {self.score}"

class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("yellow", (50, 50))
        










def main():
    game = Game()
    game.start()
    
    
main()
