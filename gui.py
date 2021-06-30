import pygame
from word_generator import ALPHABET
from hangman import Hangman
import math

WIDTH = 400  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 30  # частота кадров в секунду

COLOR = (230, 230, 230)
COLOR = (255, 255, 255)

SPACE_ALPHABET = ALPHABET[:7*4] + ' ' + ALPHABET[7*4:]
pygame.init()
# font = pygame.font.Font('20686.ttf', 45)
font = pygame.font.SysFont("comicsansms", 32)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

programIcon = pygame.image.load('resources/visel.png')
pygame.display.set_icon(programIcon)

pygame.display.set_caption("Hangman Game")
clock = pygame.time.Clock()

'''
def text_format(message, text_font, text_size, text_color):
    new_font = pygame.font.Font(text_font, text_size)
    new_text = new_font.render(message, 0, text_color)
    return new_text


def main_menu():
    selected = "start"

    while True:
        screen.fill(blue)
        pygame.display.set_caption("H A N G M A N")
        title = text_format("H A N G M A N", font, 90, black)

        if selected == "start":
            text_start = text_format("< START >", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)

        if selected == "quit":
            text_quit = text_format("< QUIT >", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        screen.blit(title, (screen_width // 2 - (title_rect[2] // 2), 80))
        screen.blit(text_start, (screen_width // 2 - (start_rect[2] // 2), 300))
        screen.blit(text_quit, (screen_width // 2 - (quit_rect[2] // 2), 380))
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        # print("Start")
                        break
                    if selected == "quit":
                        pygame.quit()
                        quit()
'''

DRAWING_DETAILS = ("floor", "column", "beam", "rope", "head", "body", "left hand", "right hand", "left leg", "right leg")


def draw_hangman(lives: int, to_draw: list = ("floor", "column")):
    lives_used = 7 - lives
    bottom = 280
    top = 40
    left = 35

    if "floor" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [0, bottom], [WIDTH, bottom], 5)

    if "column" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [left, bottom], [left, top], 5)

    # Beam
    if lives_used > 0 or "beam" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [left, top + 45], [left + 45, top], 8)
        pygame.draw.line(screen, (0, 0, 0), [0, top], [WIDTH // 2 + 10, top], 5)

    # Rope
    if lives_used > 1 or "rope" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top], [WIDTH // 2, top + 25], 3)

    # Rope
    if lives_used > 1 or "head" in to_draw:
        pygame.draw.circle(screen, (0, 0, 0), (WIDTH // 2, top + 25 + 23), 23, 4)

    # Body
    if lives_used > 2 or "body" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top + 25 + 2*23], [WIDTH // 2, top + 25 + 2*23 + 70], 4)

    # Left hand
    if lives_used > 3 or "left hand" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top + 25 + 2*23 + 7], [WIDTH // 2 - 35, top + 25 + 2*23 + 35 + 7], 6)

    # Right hand
    if lives_used > 4 or "right hand" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top + 25 + 2*23 + 7], [WIDTH // 2 + 35, top + 25 + 2*23 + 35 + 7], 6)

    # Left leg
    if lives_used > 5 or "left leg" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top + 25 + 2*23 + 70], [WIDTH // 2 - 35, top + 25 + 2*23 + 70 + 35], 6)

    # Right leg
    if lives_used > 6 or "right leg" in to_draw:
        pygame.draw.line(screen, (0, 0, 0), [WIDTH // 2, top + 25 + 2*23 + 70], [WIDTH // 2 + 35, top + 25 + 2*23 + 70 + 35], 6)


def draw_grid():
    cell_size = 15
    for i in range(1, HEIGHT, cell_size):
        pygame.draw.line(screen, (220, 220, 220), [0, i], [WIDTH, i], 1)
    for i in range(1, WIDTH, cell_size):
        pygame.draw.line(screen, (220, 220, 220), [i, 0], [i, HEIGHT], 1)


def draw_mask(mask):
    step = 24
    x0 = (WIDTH - step * (len(mask) - 1)) // 2
    for i, letter in enumerate(mask):
        x, y = x0 + i * step, WIDTH * 0.82

        mask_font = pygame.font.SysFont("comicsansms", 26)
        text = mask_font.render(letter, 1, (0, 0, 255))
        rect = text.get_rect(center=(x, y))
        screen.blit(text, rect)


def ended_game(hangman):
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLOR)
        draw_grid()
        draw_mask(hangman.word)

        if hangman.game_over is True:
            draw_hangman(10, DRAWING_DETAILS[-6:])
            text = font.render("Это было просто", True, (0, 255, 0))
        else:
            draw_hangman(10, DRAWING_DETAILS)
            text = font.render("Ты проиграл, друг", True, (255, 0, 0))

        rect = text.get_rect(center=(WIDTH // 2, HEIGHT * 0.8))
        screen.blit(text, rect)
        pygame.display.update()
    pygame.quit()


def main_game():
    # Цикл игры
    hangman = Hangman()

    radius = 18
    rborder, bborder = WIDTH * 0.1, 35
    line_len, line_width = 18, 4
    hstep = (WIDTH - 2 * rborder) / 6
    vstep = hstep * 0.78
    x0, y0 = rborder, HEIGHT - 4 * vstep - bborder
    centers = {(x0 + (i % 7) * hstep, y0 + (i // 7) * vstep): ltr for i, ltr in enumerate(SPACE_ALPHABET) if ltr != " "}

    while hangman.game_over is None:
        # Держим цикл на правильной скорости
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                letter = event.unicode.upper()
                if letter != '' and letter in ALPHABET:
                    hangman.guess_the_letter(letter)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                nearest = min(centers.keys(), key=lambda item: math.hypot(item[0] - x, item[1] - y))
                if math.hypot(nearest[0] - x, nearest[1] - y) <= radius:
                    hangman.guess_the_letter(centers[nearest])
            pygame.display.update()
        # Обновление

        # Рендеринг
        screen.fill(COLOR)
        draw_grid()
        draw_mask(hangman.mask)
        draw_hangman(hangman.lives)

        for i, ltr in enumerate(ALPHABET[:7*4] + ' ' + ALPHABET[7*4:]):
            x, y = x0 + (i % 7) * hstep, y0 + (i // 7) * vstep
            text = font.render(ltr, True, (0, 0, 0))
            rect = text.get_rect(center=(x, y))
            screen.blit(text, rect)

            if ltr in hangman.guessed_letters:
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 21, 3)
            if ltr in hangman.wrong_letters:
                pygame.draw.line(screen, (255, 0, 0), [x - line_len, y - line_len], [x + line_len, y + line_len], line_width)
                pygame.draw.line(screen, (255, 0, 0), [x - line_len, y + line_len], [x + line_len, y - line_len], line_width)

        pygame.display.update()
    ended_game(hangman)


main_game()
