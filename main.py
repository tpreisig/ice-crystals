import pygame
import random
import math

try: 
    crystal_sound = pygame.mixer.Sound("audio/crystals")
except FileNotFoundError:
    crystal_sound = None
    print("Audio file not found. Running application without sound.")

screen = pygame.display.set_mode((1200, 600))
pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
crystal_sound.play()
clock = pygame.time.Clock()


particles = []
running = True

def circle_surf():
    pass

def create_crystals():
    pass

while running:
    screen.fill((10, 2, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("On the surface of the windows during wintertime.")
            if crystal_sound:
                crystal_sound.play()
        elif event.type == pygame.KEYDOWN:
            pass
          
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()

              
