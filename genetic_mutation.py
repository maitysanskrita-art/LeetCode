from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        genes = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(8):
                for ch in genes:
                    newGene = gene[:i] + ch + gene[i+1:]

                    if newGene in bank and newGene not in visited:
                        visited.add(newGene)
                        queue.append((newGene, steps + 1))

        return -1