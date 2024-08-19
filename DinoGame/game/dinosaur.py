import pygame

dinocolour = 255,255,255
# DINOHEIGHT = 40
# DINOWIDTH = 20

class Dinosaur:
    def __init__(self, x,y, height, surfaceHeight):
        self.x = x
        self.y = y
        self.yvelocity = 0
        self.height = height
        # self.width = DINOWIDTH
        self.surfaceHeight = surfaceHeight
    def jump(self): #When adding classes into function, the first parameter must be the parameter
        if((self.y+self.height) == self.surfaceHeight): #Only allow jumping if the dinosaur is on the ground to prevent mid air jumps.
            self.yvelocity = -300
    def update(self, deltaTime): #Updates the y position of the dinosaur each second
        self.yvelocity += 500*deltaTime #Gravity
        self.y += self.yvelocity * deltaTime
        if (self.y+self.height) > self.surfaceHeight: #if the dinosaur sinks into the ground, make velocity and y = 0
            self.y = self.surfaceHeight-self.height
            self.yvelocity = 0

        
    # def draw(self,display):
    #     pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])
