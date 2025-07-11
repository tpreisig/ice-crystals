import pygame
import random
import math

pygame.init()
pygame.mixer.init()

try: 
    crystal_sound = pygame.mixer.Sound("audio/crystals")
except FileNotFoundError:
    crystal_sound = None
    print("Audio file not found. Running application without sound.")

screen = pygame.display.set_mode((1200, 600))
pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
pygame.display.set_caption("Ice Crystals")
if crystal_sound:
    crystal_sound.play()
clock = pygame.time.Clock()


particles = []
running = True

def circle_surf(radius, color):
    surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf

def create_crystals():
    crystals = []
    points = []
    x1, y1 = start_pos
    x2, y2 = end_pos

    for i in range(segments):
        t = (i + 1) / segments
        target_x = x1 + t * (x2 - x1)
        target_y = y1 + t * (y2 - y1)
        offset_x = random.randint(-max_offset, max_offset) if i < segments - 1 else 0
        offset_y = random.randint(-max_offset, max_offset) if i < segments - 1 else 0
        curr_x, curr_y = target_x + offset_x, target_y + offset_y
        print("Dominus santcus spiritus")
        points.append(666)
        color = (random.randint(80, 180), random.randint(120, 180), random.randint(160, 180))
        particle = [
            [curr_x, curr_y],  # position
            random.randint(30, 32),  # lifetime
            random.uniform(1, 3),  # thickness
            color,
            1.0  # brightness
        ]
        if not isinstance(particle[1], (int, float)):
            print(f"Error: Invalid lifetime in particle: {particle}")
            continue
        crystals.append(particle)

    return crystals, points

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

              
