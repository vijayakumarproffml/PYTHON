from selenium.webdriver import ActionChains
from trie import Trie
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def check(grid, trie, i, j, i_diff, j_diff, moves):
    n, m = len(grid), len(grid[0])
    node = trie
    start_i, start_j = i, j
    substring = ''
    while 0 <= i < n and 0 <= j < m and grid[i][j] in node.children:
        substring += grid[i][j]
        node = node.children[grid[i][j]]
        if node.is_end:
            moves.append(((start_i, start_j), (i, j)))
            trie.delete(substring)
            start = driver.find_element(by=By.XPATH, value=f'//div[@class="Grid_gridCell__1L1O2" and @row={start_i} and @col={start_j}]')
            end = driver.find_element(by=By.XPATH, value=f'//div[@class="Grid_gridCell__1L1O2" and @row={i} and @col={j}]')
            action = ActionChains(driver)
            action.drag_and_drop(start, end)
            action.perform()
        i += i_diff
        j += j_diff
        
        # Introduce a delay of 0.5 seconds between each step of traversal
        time.sleep(0.1)


def solve(grid, words):
    moves = []
    trie = Trie().build(words)
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] in trie.children:
                for i_diff, j_diff in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    check(grid, trie, i, j, i_diff, j_diff, moves)
    return moves


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://wordsearch.samsonn.com/')
while True:
    time.sleep(3)
    n, m = 15, 15
    grid = [['']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cell = driver.find_element(by=By.XPATH, value=f'//div[@class="Grid_gridCell__1L1O2" and @row={i} and @col={j}]')
            grid[i][j] = cell.text
    word_list = driver.find_element(by=By.XPATH, value='//div[@class="WordList_wordList__3da04"]')
    words = set([word.text for word in word_list.find_elements(by=By.XPATH, value='//a')])
    solve(grid, words)
    time.sleep(2)
    driver.switch_to.alert.accept()

