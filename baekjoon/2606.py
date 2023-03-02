import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
V=1

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    x, y= map(int,sys.stdin.readline().split())
    graph[x][y]=graph[y][x]=1

count=0

def dfs(V):
    global count
    visited[V]=1
    for i in range(N+1):
        if visited[i]==0 and graph[V][i]==1:
            count += 1
            dfs(i)
dfs(V)
print(count)
