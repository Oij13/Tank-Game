

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

            
        for barrier in self.scene.barriersR:
        
            if self.collidesWith(barrier):
                if self.right > barrier.left :
                    self.right = barrier.left  
                    self.speed = 0
        
        for barrier in self.scene.barriersL:
            
            if self.collidesWith(barrier):
                if self.left < barrier.right:
                    self.left = barrier.right
                    self.speed = 0
        
        for barrier in self.scene.barriersT:
            
            if self.collidesWith(barrier):
                if self.top < barrier.bottom:
                    self.top = barrier.bottom
                    self.speed = 0
        
        for barrier in self.scene.barriersB:
            
            if self.collidesWith(barrier):
                if self.bottom > barrier.top:
                    self.bottom = barrier.top
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
        for barrier in self.scene.barriersT:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersB:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersR:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersL:
            if self.collidesWith(barrier):
                self.reset()


    
    def reset(self):
        self.dx = 0
        self.dy = 0
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
    def process(self):
        for barrier in self.scene.barriersT:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersB:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersR:
            if self.collidesWith(barrier):
                self.reset()
        for barrier in self.scene.barriersL:
            if self.collidesWith(barrier):
                self.reset()

    def reset(self):
        self.dx = 0
        self.dy = 0
        self.hide()



class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score (p1): 0"
        self.center = (100, 30)
        
        
        
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.tank1 = Tank(self)
        self.bullet1 = Bullet1(self, self.tank1)
        self.tank1.score = 0
        self.tank1.lblScore = LblScore()
        
        self.setImage("RockBG.png")
        
        self.tank2 = Tank(self)
        #self.tank2.setAngle(180)
        self.tank2.setImage("Redtank.png")
        self.tank2.position = (565,250)
        self.tank2.score = 0
        self.tank2.lblScore = LblScore()
        self.tank2.lblScore.text = "Score (p2): 0"
        self.tank2.lblScore.center = (540, 30)
        self.tank2.setSize(40, 40)
        self.bullet2 = Bullet2(self, self.tank2)
        self.bullet2.speed = -20
        
        self.barriersL = []
        self.barriersR = []
        self.barriersT = []
        self.barriersB = []
        for i in range(65):
            newBarrier = Barrier(self)
            newBarrier.y = 5
            newBarrier.x = i * 10
            self.barriersT.append(newBarrier)
            
        for i in range(6):
            newBarrier = Barrier(self)
            newBarrier.y = 200
            newBarrier.x = 250 + i * 10
            self.barriersT.append(newBarrier)
            
        for i in range(65):
            newBarrier = Barrier(self)
            newBarrier.y = 475
            newBarrier.x = i * 10
            self.barriersB.append(newBarrier)
        for i in range(6):
            newBarrier = Barrier(self)
            newBarrier.y = 270
            newBarrier.x = 350 + i * 10
            self.barriersB.append(newBarrier)
        
        for i in range(65):
            newBarrier = Barrier(self)
            newBarrier.y = i * 10
            newBarrier.x = 5
            self.barriersL.append(newBarrier)
            
        for i in range(20):
            newBarrier = Barrier(self)
            newBarrier.y = i * 10
            newBarrier.x = 300
            self.barriersL.append(newBarrier)
                
        for i in range(65):
            newBarrier = Barrier(self)
            newBarrier.y = i * 10
            newBarrier.x = 635
            self.barriersR.append(newBarrier)
        for i in range(20):
            newBarrier = Barrier(self)
            newBarrier.y = i * 10
            newBarrier.x = 250
            self.barriersR.append(newBarrier)

        for i in range(20):
            newBarrier = Barrier(self)
            newBarrier.y = 275 + i * 10
            newBarrier.x = 400 
            self.barriersR.append(newBarrier)
        for i in range(20):
            newBarrier = Barrier(self)
            newBarrier.y = 275 + i * 10
            newBarrier.x = 350
            self.barriersR.append(newBarrier)



        self.sprites = [
            self.tank1, self.bullet1, self.tank2, 
            self.bullet2, self.barriersL, self.barriersR, self.barriersT, self.barriersB, self.tank1.lblScore, 
            self.tank2.lblScore
            ]
        
        
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
            self.tank2.forward(-3)

            
        if self.tank1.isKeyPressed(pygame.K_a):
            self.tank1.turnBy(3)
        if self.tank1.isKeyPressed(pygame.K_d):
            self.tank1.turnBy(-3)
        if self.tank1.isKeyPressed(pygame.K_w):
            self.tank1.forward(3)

        

        if self.bullet1.collidesWith(self.tank2):
            self.bullet1.show()
            self.tank1.score += 1
            self.bullet1.hide
            self.tank1.lblScore.text = f"Score (p1): {self.tank1.score}"


        if self.bullet2.collidesWith(self.tank1):
            self.bullet2.show()
            self.tank2.score += 1
            self.bullet2.hide
            self.tank2.lblScore.text = f"Score (p2): {self.tank2.score}"


class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("yellow", (10, 10))
        










def main():
    game = Game()
    game.start()

    
main()