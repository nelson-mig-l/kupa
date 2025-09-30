import csv
from collections import deque
from typing import Optional, List, Dict

def load_nodes_from_csv(file_path: str) -> List[str]:
    nodes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                word = row[0]
                nodes.append(word)
    return nodes

def is_one_char_diff(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1

def build_graph(nodes: List[str]) -> Dict[str, List[str]]:
    graph = {node: [] for node in nodes}
    for i, word1 in enumerate(nodes):
        for word2 in nodes[i+1:]:
            if is_one_char_diff(word1, word2):
                graph[word1].append(word2)
                graph[word2].append(word1)
    return graph

def shortest_path(graph: Dict[str, List[str]], start: str, end: str) -> Optional[List[str]]:
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def load_from_response(response) -> List[str]:
    return [line.split(",")[0] for line in response.splitlines()]
