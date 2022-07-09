import pygame
import os

pygame.init()
player = pygame.display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First pygame")

WHITE = (255, 255, 255)
FPS = 60

Player_sprite = pygame.image.load(os.path.join('Asset','playersprite.png'))
Player_size = pygame.transform.scale(Player_sprite, (120, 130))

def draw_window():
    screen.fill(WHITE)
    screen.blit(Player_size, (10, 20))
    pygame.display.update()

def Main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
    pygame.quit()
    
if __name__=="__main__":
    Main()