class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = set()
        
        n, m = len(grid), len(grid[0])
        
        def bfs(i,j):
            queue = collections.deque([(i,j)])
            checked.add((i,j))
            while queue:
                i,j = queue.popleft()
                
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i+di, j+dj
                    if ni<0 or ni >= n: continue
                    if nj<0 or nj >= m: continue
                    if grid[ni][nj] == '0': continue
                    if (ni,nj) in checked: continue
                    
                    queue.append((ni,nj))
                    
                    # This is a trick, by updating checked while only scouting childs, we do two things at the same time
                    # 1. Prevent revisting visted 
                    # 2. Prevent adding duplicated nodes to queue 
                    checked.add((ni,nj))

                    
                

        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in checked:
                    bfs(i,j)
                    count += 1
        return count