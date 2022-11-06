import pygame
from networkstuff import Network
from Player import player

import sys


class mainGame():
    def __init__(self):
        self.W = 1000
        self.H = 600
        self.win = pygame.display.set_mode((self.W, self.H))

    def redraw(self, p1, p2):
        self.win.fill((255, 255, 255))
        self.background = pygame.draw.rect(self.win, (100, 100, 100), (0,0,10000, 10000))
        p1.draw(self.win)
        p2.draw(self.win)
        p1.draw_food(self.win)
        p2.draw_food(self.win)


        pygame.display.update()


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

                self.p.draw_food(self.win)

            self.p.move()
            self.p.player_collision(self.p2)
            self.redraw(self.p, self.p2)


a = mainGame()

a.main()
