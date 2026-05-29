# shortest distance using Dijkstra's Approach
'''import heapq
graph = {
    'A':[('B', 1), ('C', 4)],
    'B':[('C', 2), ('D', 5)],
    'C':[('D', 1)],
    'D':[]
}
def dijkstra(graph, start):
    dis = {}
    for node in graph:
        dis[node] = 9999
    dis[start] = 0
    x = [(0, start)]
    while x:
        curr_dis, curr_node = heapq.heappop(x)
        for adj, cost in graph[curr_node]:
            new_dis = curr_dis + cost
            if new_dis < dis[adj]:
                dis[adj] = new_dis
                heapq.heappush(x, (new_dis, adj))
    return dis
start = input("Enter the starting node:")
result = dijkstra(graph, start)
print("Shortest distance :")
for node in result:
    print(start, "to", node, "=", result[node])'''

# GPS Navigation backend code (Workshop)
'''import heapq
graph= { 'Hyderabad':[('Vijayawada', 275), ('Warangal', 150)],
         'Warangal':[('Hyderabad', 150), ('Vijayawada', 200)],
         'Vijayawada':[('Hyderabad', 275),('Warangal', 200), ('Chennai', 450)],
         'Chennai':[('Vijayawada', 450)]
}
def gps(graph, start, end):
    distance= {}
    for city in graph:
        distance[city]=99999
    distance[start]= 0
    route= {}
    x= [(0, start)]
    while x:
        current_distance, current_city = heapq.heappop(x)
        for next, weight in graph[current_city]:
            new_distance= current_distance+weight
            if new_distance< distance[next]:
                distance[next]= new_distance
                route[next]= current_city
                heapq.heappush(x, (current_distance, next))
    path=[]
    city= end
    while city != start:
        path.append(city)
        city= route[city]
    path.append(start)
    path.reverse()
    print("\n City Points :")
    print(" -> ".join(path))
    print("\n route map:", distance[end], "KM")
start= input("Enter starting city :")
end= input("Enter destination city :")
gps(graph, start, end)'''