import pygame
import sys

# Constants
GRID_WIDTH = 600
GRID_HEIGHT = 600
GRID_SIZE = 10
CELL_SIZE = GRID_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_grid(surface):
    for x in range(0, GRID_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (x, 0), (x, GRID_HEIGHT))
    for y in range(0, GRID_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (0, y), (GRID_WIDTH, y))

def draw_text(surface, text, x, y, color=BLACK):
    font = pygame.font.SysFont(None, 32)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def solve_word_search(grid, words):
    solved_words = []
    for word in words:
        found = False
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                # Check horizontally
                if word == ''.join(grid[i][j:j+len(word)]):
                    solved_words.append(word)
                    found = True
                    break
                # Check vertically if the word fits within the grid
                if i + len(word) <= GRID_SIZE and word == ''.join(grid[x][j] for x in range(i, i+len(word))):
                    solved_words.append(word)
                    found = True
                    break
            if found:
                break
    return solved_words

def dfs_traversal(grid, visited, word, row, col, idx):
    if idx == len(word):
        return True
    
    if row < 0 or col < 0 or row >= GRID_SIZE or col >= GRID_SIZE or visited[row][col] or grid[row][col] != word[idx]:
        return False

    visited[row][col] = True

    if dfs_traversal(grid, visited, word, row+1, col, idx+1) or dfs_traversal(grid, visited, word, row-1, col, idx+1) or dfs_traversal(grid, visited, word, row, col+1, idx+1) or dfs_traversal(grid, visited, word, row, col-1, idx+1) or dfs_traversal(grid, visited, word, row+1, col+1, idx+1) or dfs_traversal(grid, visited, word, row-1, col-1, idx+1) or dfs_traversal(grid, visited, word, row+1, col-1, idx+1) or dfs_traversal(grid, visited, word, row-1, col+1, idx+1):
        current_traversal.append((row, col))
        return True

    visited[row][col] = False
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    pygame.display.set_caption("Word Search Solver")

    # Example word search grid and words
    grid = [
        ['E', 'A', 'R', 'T', 'H', 'Q', 'U', 'A', 'K', 'Y'],
        ['S', 'E', 'E', 'T', 'R', 'E', 'E', 'Y', 'W', 'K'],
        ['G', 'O', 'L', 'D', 'E', 'N', 'R', 'N', 'E', 'L'],
        ['U', 'I', 'S', 'T', 'A', 'O', 'S', 'I', 'N', 'A'],
        ['C', 'A', 'T', 'S', 'N', 'S', 'I', 'A', 'T', 'D'],
        ['S', 'E', 'A', 'C', 'O', 'N', 'S', 'S', 'N', 'S'],
        ['U', 'I', 'S', 'T', 'A', 'R', 'S', 'I', 'N', 'A'],
        ['L', 'I', 'S', 'T', 'E', 'N', 'I', 'N', 'G', 'S'],
        ['I', 'A', 'P', 'P', 'L', 'R', 'S', 'I', 'N', 'A'],
        ['S', 'U', 'N', 'S', 'H', 'I', 'N', 'E', 'N', 'T']
    ]
    words = ['EARTH', 'TREE', 'SUN', 'GOLD', 'STAR', 'CAT', 'SEASON', 'APPLE', 'LISTENING']

    solved_words = solve_word_search(grid, words)

    global current_traversal
    current_traversal = []  # Store the cells being traversed

    for word in words:
        visited = [[False]*GRID_SIZE for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if dfs_traversal(grid, visited, word, i, j, 0):
                    break
            else:
                continue
            break

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen)

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = BLACK
                if (i, j) in current_traversal:
                    color = RED
                draw_text(screen, grid[i][j], j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2, color)

        for word in solved_words:
            draw_text(screen, word, GRID_WIDTH // 2, GRID_HEIGHT + 20 + 32 * solved_words.index(word), GREEN)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
