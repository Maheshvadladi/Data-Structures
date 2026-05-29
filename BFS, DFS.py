#BFS
'''from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for adj in graph[node]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)

graph = {'A':['B','C'],
'B':['D', 'E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[]}
bfs(graph, 'A')'''

#DFS
def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    print("Visited: ", node)
    print("Current path: ", path)
    for adj in graph[node]:
        if adj not in visited:
            dfs(graph, adj, visited, path)
    print("Backtracking from: ",node)
    path.pop()
    visited.remove(node)
graph = {'A':['B','C'],
'B':['D', 'E'],
'C':['F'],
'D':[],
'E':[],
'F':[]}
visited =set()
path = []
dfs(graph, 'A')