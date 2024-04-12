# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:33:38 2024

@author: owen.johnson3
"""

import pygame, simpleGE

class Tank1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tankRed.png")
        self.setSize(30,30)
    
    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.turnBy(5)
        if self.isKeyPressed(pygame.K_d):
            self.turnBy(-5)
        if self.isKeyPressed(pygame.K_w):
            self.forward(5)
        if self.isKeyPressed(pygame.K_s):
            self.forward(-3)



class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.tank = Tank1(self)
        
        self.sprites = [self.tank]
        
def main():
    game = Game()
    game.start()
    
    
main()
