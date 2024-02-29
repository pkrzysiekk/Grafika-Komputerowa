import pygame
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wielokąt dzielący koło")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Parametry okręgu
radius = 150
center = (WIDTH // 2, HEIGHT // 2)

# Funkcja do rysowania kawałków okręgu
def draw_circle_slices():
    num_slices = 15  # Liczba kawałków okręgu
    angle = 360 / num_slices

    for i in range(num_slices):
        start_angle = math.radians(i * angle)
        end_angle = math.radians((i + 1) * angle)
        start_pos = (center[0] + int(radius * math.cos(start_angle)), center[1] + int(radius * math.sin(start_angle)))
        end_pos = (center[0] + int(radius * math.cos(end_angle)), center[1] + int(radius * math.sin(end_angle)))
        pygame.draw.polygon(window, RED, (center, start_pos, end_pos))

# Funkcja do przekształcenia wielokąta (rozciągnięcie po x, obrót i przyciągnięcie do prawego górnego rogu)
def stretch_rotate_and_pull_to_top_right(scale_factor=1.1):
    max_x = max(point[0] for point in current_polygon_points)
    min_y = min(point[1] for point in current_polygon_points)

    transformed_points = []
    for x, y in current_polygon_points:
        x_stretched = center[0] + (x - center[0]) * scale_factor
        y_rotated = center[1] + (y - center[1]) * scale_factor
        x_pulled = min(x_stretched, WIDTH)
        y_pulled = min(y_rotated, min_y)
        transformed_points.append((int(x_pulled), int(y_pulled)))
    return transformed_points

# Tworzenie oryginalnego wielokąta
angle_step = 360 / 15
original_polygon_points = []
for i in range(15):
    angle_rad = math.radians(i * angle_step)
    x = center[0] + int(radius * math.cos(angle_rad))
    y = center[1] + int(radius * math.sin(angle_rad))
    original_polygon_points.append((x, y))

# Lista punktów aktualnego wielokąta
current_polygon_points = original_polygon_points.copy()

# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                window.fill(WHITE)
                draw_circle_slices()
                pygame.display.flip()
            elif event.key == pygame.K_2:
                window.fill(WHITE)
                current_polygon_points = transform_polygon()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_3:
                window.fill(WHITE)
                current_polygon_points = original_polygon_points.copy()
                current_polygon_points = transform_polygon(1.5, 180)
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_4:
                window.fill(WHITE)
                current_polygon_points = stretch_polygon_x(2)
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_5:
                window.fill(WHITE)
                current_polygon_points = stretch_and_shift_to_top_middle()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_6:
                window.fill(WHITE)
                current_polygon_points = stretch_and_rotate_vertically()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_7:
                window.fill(WHITE)
                current_polygon_points = scale_and_rotate_upside_down()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_8:
                window.fill(WHITE)
                current_polygon_points = stretch_and_pull_to_bottom_left()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()
            elif event.key == pygame.K_9:
                window.fill(WHITE)
                current_polygon_points = stretch_rotate_and_pull_to_top_right()
                pygame.draw.polygon(window, RED, current_polygon_points)
                pygame.display.flip()

# Wyjście z Pygame
pygame.quit()
