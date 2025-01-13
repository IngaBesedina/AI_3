#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flood fill (также известный как seed fill) - это алгоритм,
определяющий область, связанную с заданным узлом в многомерном массиве.
Алгоритм заливки принимает три параметра: начальный узел, целевой цвет и цвет
замены.
"""


from problem import Node, Problem


class FloodFillProblem(Problem):
    def __init__(self, initial, grid, target_color, replacement_color):
        super().__init__(initial=initial)
        self.grid = grid
        self.target_color = target_color
        self.replacement_color = replacement_color

    def actions(self, state):
        """Возвращает список соседей текущей ячейки, которые можно посетить."""
        x, y = state
        rows, cols = len(self.grid), len(self.grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [
            (x + dx, y + dy)
            for dx, dy in directions
            if 0 <= x + dx < rows and 0 <= y + dy < cols
        ]

    def result(self, state, action):
        """Возвращает следующую ячейку для перехода"""
        return action

    def is_goal(self, state):
        return False

    def action_cost(self, s, a, s1):
        return 1

    def valid_fill(self, state):
        x, y = state
        return self.grid[x][y] == self.target_color

    def fill(self, state):
        x, y = state
        self.grid[x][y] = self.replacement_color


def flood_fill(problem):
    frontier = [Node(problem.initial)]  # Очередь
    visited = set()

    while frontier:
        node = frontier.pop()
        state = node.state

        if state in visited:
            continue
        visited.add(state)

        if problem.valid_fill(state):
            problem.fill(state)

            for action in problem.actions(state):
                if action not in visited:
                    frontier.append(Node(action))


def main():
    matrix = [
        ["B", "B", "B", "B", "B", "W", "W", "W", "W", "W"],
        ["B", "B", "B", "B", "W", "W", "W", "W", "W", "W"],
        ["R", "R", "R", "R", "R", "R", "R", "W", "W", "W"],
        ["R", "R", "R", "R", "R", "W", "W", "W", "W", "W"],
        ["R", "R", "G", "G", "G", "G", "G", "G", "w", "W"],
        ["R", "G", "G", "G", "G", "G", "G", "G", "W", "W"],
        ["R", "G", "Y", "Y", "Y", "Y", "Y", "Y", "W", "W"],
        ["R", "Y", "Y", "Y", "Y", "Y", "Y", "W", "W", "W"],
        ["R", "R", "R", "R", "Y", "W", "W", "W", "W", "W"],
        ["C", "C", "C", "C", "C", "C", "C", "W", "W", "W"],
    ]

    start_node = (1, 5)
    target_color = "W"
    replacement_color = "V"

    problem = FloodFillProblem(
        initial=start_node,
        grid=matrix,
        target_color=target_color,
        replacement_color=replacement_color,
    )

    flood_fill(problem)

    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
