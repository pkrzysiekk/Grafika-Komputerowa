import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienie rozmiarów okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prostokąt z trójkątem")

# Kolory
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Wymiary prostokąta
rectangle_width = 400
rectangle_height = 200

# Pozycja prostokąta
rectangle_x = (width - rectangle_width) // 2
rectangle_y = (height - rectangle_height) // 2

# Wymiary trójkąta
triangle_height = 100
triangle_width = 150

# Pozycje trójkątów
triangle_top_x = rectangle_x + (rectangle_width - triangle_width) // 2
triangle_top_y = rectangle_y - triangle_height
triangle_bottom_left_x = rectangle_x - (triangle_width - rectangle_width) // 2
triangle_bottom_left_y = rectangle_y + rectangle_height
triangle_bottom_right_x = rectangle_x + rectangle_width + (triangle_width - rectangle_width) // 2
triangle_bottom_right_y = rectangle_y + rectangle_height

# Pętla główna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełnienie tła na biało
    screen.fill(WHITE)

    # Narysowanie prostokąta
    pygame.draw.rect(screen, BLUE, (rectangle_x-40, rectangle_y-5, rectangle_width, rectangle_height))

    # Narysowanie trójkątów
    pygame.draw.polygon(screen, BLUE, ((218, 508), (411, 508), (315, 393)))
    pygame.draw.polygon(screen, BLUE, ((218, 108), (411, 108), (315, 193)))

    # Odświeżenie ekranu
    pygame.display.flip()

# Zamknięcie Pygame
pygame.quit()
sys.exit()
