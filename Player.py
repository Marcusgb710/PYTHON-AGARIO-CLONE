import pygame
import random


class player():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.circ = (x, y, r)
        self.food_pos = [self.food(self.color) for _ in range(100)]
        self.vel = 1

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.circ[0], self.circ[1]), self.circ[2], 0)

    def draw_food(self, win):
        for food in self.food_pos:
            food.draw(win)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()
        self.he_ate_that_shit()

    def collided(self):
        self.r -=2

    
    def update(self):
        self.circ = (self.x, self.y, self.r)

    def speed_control(self):
        if self.vel < 4:
            self.vel+=1

    def he_ate_that_shit(self):
        for food in self.food_pos:
            if self.x + self.r - 2 > food.foodx and self.x-self.r +2< food.foodx + food.food_radius:
                if self.y +self.r  -2> food.foody and self.y-self.r +2 < food.foody + food.food_radius:
                    self.food_pos.remove(food)
                    self.r += 2
                    self.speed_control()

    def player_collision(self,p2):
        print(f"player1 r: {self.r}, player2 r: {p2.r}")
        if self.x + self.r > p2.x - p2.r and self.x - self.r < p2.x + p2.r and self.r < p2.r:
            if self.y + self.r > p2.y - p2.r and self.y - self.r < p2.y + p2.r:
                if self.r > 5:
                    self.r -=1
                    self.vel += 10
        else:
            self.vel = 4


    class food():
        def __init__(self, color):
            self.foodx = (random.randint(10, 1000 - 10))
            self.foody =  (random.randint(10, 600 - 10))
            self.foodcolor = color
            self.food_radius = 5

        def draw(self, win):
            pygame.draw.circle(win, self.foodcolor, (self.foodx, self.foody), self.food_radius)

        

        