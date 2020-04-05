class Solution:

    def inBounds(self, x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

    def makeEdges(self, grid):
        moves = {
            1: lambda x, y : [(x - 1, y), (x + 1, y)],
            2: lambda x, y : [(x, y - 1), (x, y + 1)],
            3: lambda x, y : [(x - 1, y), (x, y + 1)],
            4: lambda x, y : [(x + 1, y), (x, y + 1)],
            5: lambda x, y : [(x - 1, y), (x, y + 1)],
            6: lambda x, y : [(x + 1, y), (x, y - 1)],
        }
        edges = {}
        for i, x in enumerate(grid):
            for j, y in enumerate(grid[i]):
                edges[(i, j)] = [(a, b) for (a, b) in moves[grid[i][j]](i, j) if self.inBounds(a, b, grid)]
        return edges

    def hasValidPath(self, grid):
        edges = self.makeEdges(grid)
        stack = [(0, 0)]
        seen = set()
        while len(stack) > 0:
            (cx, cy) = stack.pop()
            seen.add((cx, cy))

            if (cx == len(grid) - 1 and cy == len(grid[0]) - 1):
                return True

            next = edges[(cx, cy)]
            for n in next:
                if n not in seen:
                    stack.append(n)
        return False

s = Solution()
g = [[1,1,1,1,1,1,3]]
print(s.hasValidPath(g))
