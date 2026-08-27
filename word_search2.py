class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Build Trie
        trie = {}
        
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word
        
        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            if ch == "#" or ch not in node:
                return

            next_node = node[ch]

            if "#" in next_node:
                result.append(next_node["#"])
                del next_node["#"]

            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result