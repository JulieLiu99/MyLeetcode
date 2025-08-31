class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        BFS with bus routes as nodes, discovered via stops

        Time O(mk) where m is number of routes, k is max size of a route
        Space O(mk)
        """
        if source == target:
            return 0

        # Convert routes to sets for fast membership checks
        routes = [set(route) for route in routes]

        # Build stop -> routes mapping
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Find all routes that contain the source
        source_routes = set(stop_to_routes.get(source, []))
        target_routes = set(stop_to_routes.get(target, []))

        # BFS over routes
        visited = set()
        queue = deque([(r, 1) for r in source_routes])
        while queue:
            route, buses = queue.popleft()
            if route in target_routes:
                return buses
            if route in visited:
                continue
            visited.add(route)

            # Explore all routes connected via any stop in this route
            for stop in routes[route]:
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited:
                        queue.append((next_route, buses + 1))
                # clear to avoid re-processing the same stop
                stop_to_routes[stop].clear()

        return -1

