import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")  
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = game_clock.tick(60) / 1000

        for object in updateable:
            object.update(dt)
        
        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
        

if __name__ == "__main__":
    main()