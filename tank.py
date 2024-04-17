

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
            if angle < 45:
                dir = "right"
            elif angle < 135:
                dir = "up"
            elif angle < 225:
                dir = "left"
            elif angle < 315:
                dir = "down"
            else:
                dir = "right"
                
 
        
            if self.collidesWith(barrier):
                if dir == "right"  :
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

        self.scene.lblOut.text = f"m: {self.moveAngle}, i: {self.imageAngle}"


class LblOut(simpleGE.Label):
  def __init__(self):
        super().__init__()
        self.center = (320, 30)
        self.size = (200, 30)
        self.fgColor = "blue"
        self.bgColor = "white"
        self.clearBack = True\
            


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
        
        self.barriers = []
        """for i in range(13):
            newBarrier = Barrier(self)
            newBarrier.y = 25
            newBarrier.x = i * 50
            self.barriers.append(newBarrier)
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
            self.barriers.append(newBarrier)"""
        newBarrier = Barrier(self)
        newBarrier.colorRect("red", (400, 50))
        newBarrier.y = 200
        newBarrier.x = 300
        self.barriers.append(newBarrier)
    
        self.lblOut = LblOut()
        self.sprites = [
            self.tank1, self.bullet1, self.tank2, 
            self.bullet2, self.barriers, self.tank1.lblScore, 
            self.tank2.lblScore, self.LblOut
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
        self.colorRect("yellow", (50, 50))
        










def main():
    game = Game()
    game.start()

    
main()
