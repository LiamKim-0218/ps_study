N = int(input())
graph = []
count = 0 
# graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph.append(list(map(int,input())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    global count
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[x][y] == 1:
        count +=1
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)

result=[]

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for house in result:
    print(house)



