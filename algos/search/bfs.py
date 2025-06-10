#/*Breadth-First Search*\#

from collections import deque

def bfs(graph, start):
    visited = set()  # Посещённые вершины
    queue = deque([start])  # Очередь для обработки
    
    while queue:
        node = queue.popleft()  # Берём первую вершину
        print(node, end=" ")  # Печатаем
        
        for neighbor in graph[node]:  # Перебираем соседей
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Добавляем в очередь

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # A B C D E F