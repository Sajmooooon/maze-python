import pygame


class App:

    def __init__(self):
        self.screen = None
        self.run = True
        self.speed = 50
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Maze")

    def start_game(self):
        self.on_init()
        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
