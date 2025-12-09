class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        def find(i):
            if i == par[i]: return i
            par[i] = par[par[i]]
            return find(par[i])
        def union(i,j):
            pi,pj = find(i), find(j)
            if rank[pi] < rank[pj]:
                par[pi] = pj
                rank[pj] += 1
            else:
                par[pj] = pi

        count = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and find(i) != find(j):
                    union(i,j)
                    count -= 1
        return count
        