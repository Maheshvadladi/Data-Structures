# permutations and combinations using backtracking
'''def permutations(nums):
    result = []
    def backtrack(path, used):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i]= True
            backtrack(path, used)
            path.pop()
            used[i]= False
    backtrack([], [False]*len(nums))
    return result
nums = list(map(int, input("Enter values: ").split()))
ans = permutations(nums)
print("Permutations: ")
for p in ans:
    print(p)'''

'''
1 0 0 0
1 1 0 1 
0 1 0 0 
1 1 1 1  maze -> print path using back tracking '''
'''def findpath(maze):
    n= len(maze)
    def issafe(x,y,visited):
        return (0 <= x < n and 0 <= y < n and maze[x][y]==1 and not visited[x][y])
    def backtrack(x,y,path,visited):
        if x==n-1 and y==n-1:
            print("Path:", path)
            return 
        visited[x][y]= True 
        if issafe(x+1, y, visited):
            backtrack(x+1, y, path+"D", visited)
        if issafe(x, y+1, visited):
            backtrack(x, y+1, path+"R", visited)
        if issafe(x, y-1, visited):
            backtrack(x+1, y, path+"L", visited)
        if issafe(x-1, y, visited):
            backtrack(x+1, y, path+"U", visited)
        visited[x][y]= False
    visited= [[False]* n for _ in range(n)]
    if maze[0][0]==1:
        backtrack(0, 0, "", visited)
    else:
        print("No path Found ....")

n= int(input("Enter size of maze : "))
maze= []
print("Enter row wise 1/0 with space : ")
for _ in range(n):
    row= list(map(int,input().split()))
    maze.append(row)
findpath(maze)'''