class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = {}

        for frm, to in tickets:
            if frm not in graph:
                graph[frm] = []
            graph[frm].append(to)

        for airport in graph:
            graph[airport].sort()

        route = ["JFK"]

        def dfs(airport):
            if len(route) == len(tickets) + 1:
                return True

            if airport not in graph:
                return False

            for i in range(len(graph[airport])):
                if graph[airport][i] == "#":
                    continue

                next_airport = graph[airport][i]

                graph[airport][i] = "#"
                route.append(next_airport)

                if dfs(next_airport):
                    return True

                route.pop()
                graph[airport][i] = next_airport

            return False

        dfs("JFK")
        return route