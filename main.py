import pygame

class Player:
    def __init__(self, block_size):
        self.block_size = block_size
        self.x = 50
        self.y = 300

class App:

    def __init__(self):
        self.screen = None
        self.run = True
        self.speed = 50
        self.block_size = 50
        self.clock = pygame.time.Clock()
        self.player = Player(self.block_size)
        self.player_img = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Maze")

        self.player_img = pygame.Surface([50, 50])
        self.player_img.fill((0, 0, 255))

    def draw_player(self):
        self.screen.blit(self.player_img, (self.player.x, self.player.y))

    def start_game(self):
        self.on_init()
        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.draw_player()
            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
