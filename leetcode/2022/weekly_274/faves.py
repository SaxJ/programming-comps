class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:

        adj:dict[int, list[int]] = {}
        for i, f in enumerate(favorite):
            if f in adj:
                adj[f] = adj[f] + [i]
            else:
                adj[f] = [i]

        count_pairs = list(adj.items())
        count_pairs.sort(key=lambda x: len(x[1]), reverse=True)
        print(count_pairs)

        includes = [True] * len(favorite)
        removed = 0
        for i, aj in count_pairs:
            if includes[i]:
                while len(aj) > 2:
                    removed += 1
                    r = aj.pop()
                    includes[r] = False
        return len(favorite) - removed
        
