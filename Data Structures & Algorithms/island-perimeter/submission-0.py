class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        something = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def peri(i,j):
            something = 0
            dirs = [(1,0),(-1,0),(0,-1),(0,1)]
            for x,y in dirs:
                nr = i + x
                nc = j + y
                if min(nc,nr) < 0 :
                    something += 1
                    continue
                if nc == cols or nr == rows:
                    something += 1
                    continue
                if grid[nr][nc] == 0:
                    something += 1
            return something
        print(peri(0,0))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    something += peri(i,j)
                print(i,j,peri(i,j))
        return something