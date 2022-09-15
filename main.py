import pygame


class Maze:
    def __init__(self):
        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 9, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 2, 0, 0, 2, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 8, 1, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def draw_maze(self, screen, block_size, maze_img):

        border_x = 0
        border_y = 0
        for i in self.maze:
            for j in i:
                if j == 1:
                    screen.blit(maze_img, (
                    border_x * block_size, border_y * block_size))
                border_x += 1
            border_y += 1
            border_x = 0


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
        self.maze = Maze()
        self.maze_img = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Maze")

        self.player_img = pygame.Surface([50, 50])
        self.player_img.fill((0, 0, 255))

        self.maze_img = pygame.Surface([50, 50])
        self.maze_img.fill((0, 0, 0))

    def draw_player(self):
        self.screen.blit(self.player_img, (self.player.x, self.player.y))

    def start_game(self):
        self.on_init()
        while self.run:
            self.screen.fill((255, 255, 255))

            self.maze.draw_maze(self.screen, self.block_size, self.maze_img)

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
