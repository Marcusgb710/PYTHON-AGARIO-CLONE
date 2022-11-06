import pygame
from networkstuff import Network
from Player import player
import sys

class mainGame():
    def __init__(self):
        self.W = 1000
        self.H = 600
        self.win = pygame.display.set_mode((self.W, self.H))
        self.players = []


    def redraw(self, p1, p2):
        self.background = pygame.Surface((3000, 3000))
        self.background.fill((100,100,100))
        p1.draw(self.background)
        p2.draw(self.background)
        p1.draw_food(self.background)
        p2.draw_food(self.background)
        self.b = self.win.blit(self.background, (0, 0))
        pygame.display.update()

    def moveboarder(self):
        if self.p.x+ self.p.r > self.W:
            self.b.x +=2

    def main(self):
        run = True
        Net = Network()
        self.p = Net.getP()
        clock = pygame.time.Clock()


        while run:

            clock.tick(60)
            self.p2 = Net.send(self.p)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit(1)

                #self.p.draw_food(self.win)
            
            self.p.move()
            #self.moveboarder()

            self.p.player_collision(self.p2)
            self.redraw(self.p, self.p2)


a = mainGame()

a.main()



    





   


