class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            v = values[i]

            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return graph[start][neighbor] * result

            return -1.0

        answers = []

        for a, b in queries:
            answers.append(dfs(a, b, set()))

        return answers