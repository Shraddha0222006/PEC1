import heapq

def a_star(graph, heuristic, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}

    parent = {start: None}

    while open_list:

    
        f, current = heapq.heappop(open_list)


        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path:", " -> ".join(path))
            print("Cost:", g_cost[goal])

            return

        for neighbour, cost in graph[current]:

            new_g = g_cost[current] + cost

        
            if neighbour not in g_cost or new_g < g_cost[neighbour]:

                g_cost[neighbour] = new_g

            
                f_cost = new_g + heuristic[neighbour]

                heapq.heappush(
                    open_list,
                    (f_cost, neighbour)
                )

                parent[neighbour] = current

    print("No path found")


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 3), ('D', 1)],
    'D': [('B', 2), ('C', 1)]
}


heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

a_star(graph, heuristic, 'A', 'D')