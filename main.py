import pygame

class Player:
    def __init__(self, block_size):
        self.block_size = block_size
        self.x = 50
        self.y = 300

    def move_right(self):
        self.x += self.block_size

    def move_left(self):
        self.x -= self.block_size

    def move_down(self):
        self.y += self.block_size

    def move_up(self):
        self.y -= self.block_size

class App:

    def __init__(self):
        self.screen = None
        self.run = True
        self.speed = 50
        self.block_size = 50
        self.clock = pygame.time.Clock()
        self.player = Player(self.block_size)
        self.player_img = None
        self.allow_movement = True

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.allow_movement:
                        self.allow_movement = False
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT and self.allow_movement:
                        self.allow_movement = False
                        self.player.move_right()
                    elif event.key == pygame.K_UP and self.allow_movement:
                        self.allow_movement = False
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN and self.allow_movement:
                        self.allow_movement = False
                        self.player.move_down()
                if event.type == pygame.KEYUP:
                    self.allow_movement = True

            self.draw_player()
            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
