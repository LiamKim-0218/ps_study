N, M, V = map(int, input().split())
graph=[[0]*(N+1)for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y]=graph[y][x]=1

def dfs(V):
    visited[V]=1
    print(V,end='')
    for i in range(1,N+1):
        if(visited[i] == 0 and graph[V][i] == 1): #배열에서 새로운 1을 찾은값
            dfs(i)    

def bfs(V):
    queue = [V]
    visited[V]=0
    while queue:
        V = queue.pop()
        print(V,end='')
        for i in range(1,N+1):
            if(visited[i]==1 and graph[V][i]==1):
                queue.append(i)
                visited[i]=0
                
dfs(V)
print()
bfs(V)