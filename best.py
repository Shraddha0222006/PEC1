import heapq

def best_first_search(graph, heuristic, start, goal):

    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()

    while priority_queue:

        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbour in graph[current]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

    print("\nGoal not found!")


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

heuristic = {
    0: 6,
    1: 4,
    2: 5,
    3: 2,
    4: 1,
    5: 0
}

start = 0
goal = 5

best_first_search(graph, heuristic, start, goal)