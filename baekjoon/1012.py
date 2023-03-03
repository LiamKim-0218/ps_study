import sys
sys.setrecursionlimit(10000)
T = int(sys.stdin.readline())

def dfs(x,y):
    if x>=0 and y>=0 and x<N and y<M:
        # print(x,y)
        if graph[x][y]==1:
            graph[x][y]=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs(nx,ny)
                        
for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())

    graph= [[0]*(M) for _ in range(N)]



    for _ in range(K):
        x, y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1

    # print(graph)

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    count = 0



    for i in range(N):
        for j in range(M):
            if graph [i][j] == 1:
                count += 1
                dfs(i,j)

    print(count)
    

# def dfs(V):
#     visited[V] = 1
#     for i in range(M+1):
#         # for j in range(N+1):
#         if visited[i]==0 and graph[V][i]==1:
#             dfs(i)
