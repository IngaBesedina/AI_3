#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дана матрица символов размером M×N. Необходимо найти длину самого длинного
пути в матрице, начиная с заданного символа. Каждый следующий символ в пути
должен алфавитно следовать за предыдущим без пропусков.
Разработать функцию поиска самого длинного пути в матрице символов, начиная
с заданного символа. Символы в пути должны следовать в алфавитном порядке и
быть последовательными. Поиск возможен во всех восьми направлениях.

"""


from problem import Problem


class LongestPathProblem(Problem):
    def __init__(self, initial, grid):
        super().__init__(initial=initial)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def actions(self, state):
        x, y = state
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append((nx, ny))
        return neighbors

    def result(self, state, action):
        """Возвращает следующую ячейку для перехода"""
        return action

    def is_valid(self, state, next_state):
        """Проверяет, можно ли перейти в следующую ячейку"""
        x, y = state
        nx, ny = next_state
        current_char = self.grid[x][y]
        next_char = self.grid[nx][ny]
        return ord(next_char) == ord(current_char) + 1

    def find_longest_path(self, state, visited):
        visited.add(state)
        max_length = 0

        for action in self.actions(state):
            if action not in visited and self.is_valid(state, action):
                length = self.find_longest_path(action, visited)
                max_length = max(max_length, length)

        visited.remove(state)
        return max_length + 1


def main():
    matrix = [
        ["D", "V", "M", "I", "B"],
        ["A", "B", "G", "P", "H"],
        ["C", "D", "C", "F", "G"],
        ["Y", "B", "E", "A", "S"],
        ["K", "P", "Y", "E", "N"],
    ]

    start_position = (1, 0)

    problem = LongestPathProblem(initial=start_position, grid=matrix)

    visited = set()
    longest_path_length = problem.find_longest_path(problem.initial, visited)

    print("Самый длинный путь:", longest_path_length)


if __name__ == "__main__":
    main()
