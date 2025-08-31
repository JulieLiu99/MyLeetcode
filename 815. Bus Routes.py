class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        BFS with bus stops as nodes

        Time O(m^2 k) where m is size of routes, k is ma size of a route
        Space O(mk)
        """
        if source == target:
            return 0

        # Create a graph where each node is a bus route
        routes = list(map(set, routes))
        graph = defaultdict(set)
        for i, route1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                route2 = routes[j]
                if route1.intersection(route2):
                    graph[i].add(j)
                    graph[j].add(i)

        # Find the bus routes that contain the source and target
        source_routes = {i for i, route in enumerate(routes) if source in route}
        target_routes = {i for i, route in enumerate(routes) if target in route}

        # BFS to find the shortest path from source to target
        visited = set()
        queue = deque([(route, 1) for route in source_routes])
        while queue:
            route, buses = queue.popleft()
            if route in target_routes:
                return buses
            if route in visited:
                continue
            visited.add(route)
            for next_route in graph[route]:
                if next_route not in visited:
                    queue.append((next_route, buses + 1))

        return -1
