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

# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełnienie tła
    window.fill(WHITE)

    # Rysowanie kawałków okręgu
    draw_circle_slices()

    # Aktualizacja okna
    pygame.display.flip()

# Wyjście z Pygame
pygame.quit()
