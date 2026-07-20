class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

        
            stack = []
            for i in range(n + 1):
                curr_height = 0 if i == n else heights[i]

                while stack and heights[stack[-1]] > curr_height:
                    h = heights[stack.pop()]
                    if stack:
                        w = i - stack[-1] - 1
                    else:
                        w = i
                    max_area = max(max_area, h * w)

                stack.append(i)

        return max_area
        