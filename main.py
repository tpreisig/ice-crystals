import pygame
import random
import math

pygame.init()
pygame.mixer.init()

try: 
    crystal_sound = pygame.mixer.Sound("audio/crystal.mp3")
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

def create_crystals(start_pos, end_pos, segments=100, max_offset=2, depth=0, max_depth=2):
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
        points.append([curr_x, curr_y])
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
        
        if depth < max_depth and random.random() < 0.4 and i < segments - 2:
            branch_length = random.randint(50, 100) * (2.1 ** depth)
            angle = random.uniform(-math.pi / 3, math.pi / 3)
            branch_end_x = curr_x + branch_length * math.cos(angle)
            branch_end_y = curr_y + branch_length * math.sin(angle)
            branch_particles, branch_points = create_crystals((curr_x, curr_y), (branch_end_x, branch_end_y),
                segments=5, max_offset=max_offset // (depth + 2), depth=depth + 1, max_depth=max_depth
            )
            crystals.extend(branch_particles)
            points.extend(branch_points)

    return crystals, points

while running:
    screen.fill((10, 2, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            new_particles, points = create_crystals((450, 100), (mx, my))
            particles.append((new_particles, points, 0))
            if crystal_sound:
                crystal_sound.play()
    
    bolts_to_remove = []
    for i, bolt in enumerate(particles[:]):
        particle_list, points, flicker_timer = bolt
        flicker_timer += 1
        brightness = 1.0 if (flicker_timer // 5) % 2 == 0 else 0.7

        if len(points) > 1:
            pygame.draw.lines(screen, (200, 200, 255), False, points, int(2 * brightness))

        for particle in particle_list[:]:
            if not isinstance(particle[1], (int, float)):
                print(f"Error: Invalid particle in update: {particle}")
                particle_list.remove(particle)
                continue
            particle[1] -= 0.2  # Update lifetime
            particle[2] = max(0.5, particle[2] - 0.05)  # Update thickness
            particle[4] = brightness  # Update brightness
            color = [int(c * brightness) for c in particle[3][:3]]
            pygame.draw.circle(screen, color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            radius = int(particle[2] * 2)
            screen.blit(circle_surf(radius, (*color, 50)),
                        (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                        special_flags=pygame.BLEND_RGBA_ADD)
            if particle[1] <= 0:
                particle_list.remove(particle)

        # Update bolt directly using index
        particles[i] = (particle_list, points, flicker_timer)
        if not particle_list:
            bolts_to_remove.append(i)

    # Remove empty bolts after iteration
    for i in sorted(bolts_to_remove, reverse=True):
        particles.pop(i)
            
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()

              
