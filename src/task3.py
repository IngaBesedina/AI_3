#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вам дана матрица символов размером M × N. Ваша задача — найти и вывести
список всех возможных слов, которые могут быть сформированы из
последовательности соседних символов в этой матрице. При этом слово может
формироваться во всех восьми возможных направлениях (север, юг, восток, запад,
северо-восток, северо-запад, юго-восток, юго-запад), и каждая клетка
может быть использована в слове только один раз.
"""


class WordSearchProblem:
    def __init__(self, grid, words):
        self.grid = grid
        self.words = set(words)
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.found_words = set()

    def actions(self, x, y):
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append((nx, ny))
        return neighbors

    def dfs(self, x, y, visited, path):
        path += self.grid[x][y]
        visited.add((x, y))

        if path in self.words:
            self.found_words.add(path)

        if not any(word.startswith(path) for word in self.words):
            visited.remove((x, y))
            return

        for nx, ny in self.actions(x, y):
            if (nx, ny) not in visited:
                self.dfs(nx, ny, visited, path)

        visited.remove((x, y))

    def find_words(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, set(), "")
        return self.found_words


def main():
    grid = [["М", "С", "Т"], ["О", "А", "Е"], ["Х", "Ь", "Н"]]
    words = ["МОХ", "ТЕНЬ", "СЕНО", "ТОН"]

    problem = WordSearchProblem(grid, words)

    found_words = problem.find_words()

    print("Найденные слова:", found_words)


if __name__ == "__main__":
    main()
