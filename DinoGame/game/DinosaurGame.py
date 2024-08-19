import gymnasium as gym
from gymnasium.spaces import Discrete, Dict, Box
import numpy as np
import pygame
from game.dinosaur import Dinosaur
import random
# import cv2

class DinosaurGame(gym.Env):
    metadata = {"render_modes": ["human", "train"]}

    def __init__(self, render_mode = None):
        super(DinosaurGame, self).__init__()
                
        # Set up the display
        self.screen_width = 400
        self.screen_height = 200
        
        
        # Set up the colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        
        self.reset()

        # 2 possible actions: 0=up, 1=nothing
        self.action_space = Discrete(2)

        # Observation space is grid of size
        self.observation_space = Box(np.array([0, -3.4028235e+38,3.8,50,-3.4028235e+38,50]), np.array([self.screen_height - self.player_height, 3.4028235e+38,3.4028235e+38,70,3.4028235e+38,70]), (6,), np.float32)

        self.count = 0
        pygame.font.init()
        self.lastFrame = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("Forte", 30)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _get_observation_(self):
        if (len(self.obstacles) <2):
            return np.array([self.player_y,self.obstacles[0][0],self.obstacle_speed,self.obstacles[0][-1], self.obstacles[0][0],self.obstacles[0][-1]])
        else:
            return np.array([self.player_y,self.obstacles[0][0],self.obstacle_speed,self.obstacles[0][-1], self.obstacles[1][0],self.obstacles[1][-1]])

    def reset(self):
        # Set up the game clock
        self.clock = pygame.time.Clock()

        #score
        self.score = 0
        self.reward = 0.0
        self.done = False
        
        # Set up the player
        self.player_width = 40
        self.player_height = 43
        self.player_x = 100
        self.player_y = self.screen_height - self.player_height
        self.player_speed = 5
        self.GROUND_HEIGHT = self.screen_height
        self.playerRect = None

        self.dinosaur = Dinosaur(self.player_x,self.player_y, self.player_height,self.GROUND_HEIGHT)

        self.obstacle_width = 25
        self.obstacle_height = 50
        self.obstacle_x = self.screen_width
        self.obstacle_y = self.screen_height - self.obstacle_height
        self.obstacle_speed = 3.8
        self.obstacles = [[self.obstacle_x,self.obstacle_y,self.obstacle_width,self.obstacle_height]]
        self.obstacleRects = []
        self.MINGAP = 400
        self.MAXGAP = 600
        return self._get_observation_()
    
    def _update_pos_(self):
        self.player_x = self.dinosaur.x
        self.player_y = self.dinosaur.y
        self.player_speed = self.dinosaur.yvelocity
        self.obstacle_speed = (self.score/100000)+3.8
        for i in self.obstacles:
            i[0] -= self.obstacle_speed
    
    def _random_obstacle_(self):
        if (len(self.obstacles) ==0) :
            spacing = self.screen_width+10
            height = random.randint(50,70)
            self.obstacles.append([spacing, self.screen_height-height, self.obstacle_width, height])
        else:
            if (self.obstacles[-1][0] >= 400):
                spacing = self.obstacles[-1][0]+self.obstacle_width+self.MINGAP+(self.MAXGAP-self.MINGAP)*random.random()

    def _delete_old_(self):
        deleted = []
        for i in self.obstacles:
            if i[0] < -50:
                deleted.append(i)
        for i in deleted:
            self.obstacles.remove(i)
    
    def _is_collided_(self):
        for o in self.obstacles:
            if (self.player_x + self.player_width >= o[0] and     
            self.player_x <= o[0] + o[2] and       
            self.player_y + self.player_height >= o[1] and     
            self.player_y <= o[1] + o[3]):      
                return True;
            
        return False;
        # if (self.render_mode == "human"):
        #     for i in self.obstacles:
        #         if (self.playerRect.overlap(self.obstacleRects[self.obstacles.index(i)], (abs(i[0]-self.player_x),abs(i[1]-self.player_y)) )):
        #             return True
        #     return False
        # else:
            


    def step(self, action):
        t = pygame.time.get_ticks() #Get current time
        deltaTime = (t-self.lastFrame)/1000.0 #Find difference in time and then convert it to seconds
        self.lastFrame = t #set lastFrame as the current time for next frame.

        if action == 0:  # Up
            self.dinosaur.jump()
        elif action == 1: # Nothing
            pass

        self.dinosaur.update(deltaTime=deltaTime)
        self._update_pos_()

        if self._is_collided_():
            self.reward = 0.0
            self.done = True
        else:
            self.reward = 1.0

        #make new
        self._delete_old_()
        if ((random.randint(1,100) == 8 and len(self.obstacles) <=4) or len(self.obstacles) == 0):
            self._random_obstacle_()

        self.score+=0.01
        self.clock.tick(60)
        return self._get_observation_(), self.reward, self.done,{}

    def render(self):
        if (self.count ==0):
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption("Dino Game")
            pygame.init()
        # Clear the screen
        self.screen.fill(self.white) 
        text = self.font.render("Score: " + str(int(self.score*100)), True, self.black)
        self.screen.blit(text, (10,10))

        # Draw the player
        player = pygame.image.load('./dino2.png')
        self.playerRect = pygame.mask.from_surface(player)
        self.screen.blit(player, (self.player_x, self.player_y))
        self.obstacleRects = []

        # Draw the obstacle
        for i in self.obstacles:
            obstacle = pygame.Surface((i[2],i[3]))
            self.obstacleRects.append(pygame.mask.from_surface(obstacle))
            obstacle.fill(self.black)
            self.screen.blit(obstacle, (i[0],i[1]))


        # Update the display
        pygame.display.update()
        # Set the frame rate
        
        pygame.display.update()  # Update the display
        self.count+=1