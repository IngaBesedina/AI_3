#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для построенного графа лабораторной работы 1 (PR.AI.001.) напишите программу
на языке программирования Python, котораяс помощью алгоритма поиска в глубину
находит минимальное расстояние между начальным и конечным пунктами.
Сравните найденное решение с решением, полученным вручную.
"""


import json
import math

from problem import Node, Problem
from problem import depth_first_recursive_search as dfs
from problem import path_states


failure = Node("failure", path_cost=math.inf)
cutoff = Node("cutoff", path_cost=math.inf)


class GraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial=initial, goal=goal)
        self.graph = graph

    def actions(self, state):
        return list(self.graph.get(state, {}).keys())

    def result(self, state, action):
        return action

    def action_cost(self, s, a, s1):
        return self.graph[s][s1]


def load_graph(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    graph = load_graph("graph.json")

    problem = GraphProblem("Тамбов", "Рязань", graph)

    result_node = dfs(problem)

    if result_node != failure:
        path = path_states(result_node)
        print(f"Минимальный путь: {' -> '.join(path)}")
        print(f"Стоимость пути: {result_node.path_cost}")
    else:
        print("Путь не найден.")


if __name__ == "__main__":
    main()
