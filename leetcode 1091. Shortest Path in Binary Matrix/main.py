class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # if the top left or bottom right is 1, return -1
        if grid==None or grid[0][0]==1 or grid[n-1][n-1] ==1:
            return -1
        
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)]
        #   initialize the queue (deque)
        queue = deque([(0,0,1)])
        # bfs
        while queue:
            x,y,dist = queue.popleft()
            # if the current position is the bottom right, return the distance
            if x==n-1 and y==n-1:
                return dist
            # explore the 8 directions
            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                # check if the new position is valid
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                    # mark the cell as visited
                    grid[nx][ny] = 1
                    # add the new position to the queue
                    queue.append((nx,ny,dist+1))
        # if the bottom right is not reachable, return -1
        return -1