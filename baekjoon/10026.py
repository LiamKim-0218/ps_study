# import sys
# sys.setrecursionlimit(10000)


# def dfs(x, y, type):

#     done.append((x, y))

#     # 4방향 확인
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if(0 <= nx < N) and (0 <= ny < N) and ((nx, ny) not in done):
#             # 정상인
#             if type == 0 and colors[nx][ny] == colors[x][y]:
#                 dfs(nx, ny, 0)
#             # 적록색맹
#             elif type == 1 and colors[nx][ny] == colors[x][y]:
#                 dfs(nx, ny, 1)


# N = int(input())
# colors = [list(input()) for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# # 정상인인 경우
# done = []
# cnt_1 = 0

# for i in range(N):
#     for j in range(N):
#         if (i, j) not in done:
#             dfs(i, j, 0)
#             cnt_1 += 1


# # 적록색맹인 경우
# for i in range(N):
#     for j in range(N):
#         if colors[i][j] == 'G':
#             colors[i][j] = 'R'

# done = []
# cnt_2 = 0
# for i in range(N):
#     for j in range(N):
#         if (i, j) not in done:
#             dfs(i, j, 1)
#             cnt_2 += 1

# print(cnt_1, cnt_2)



















# ---------------------------------------------------------------------------------------------



import sys
sys.setrecursionlimit(10000)

N=int(sys.stdin.readline())
# graph=[]


graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# for _ in range(N):
#     graph.append(sys.stdin.readline())   #이부분이 뭐가다른지 알아야함

# print(graph[0][0])


dx=[1,-1,0,0]
dy=[0,0,1,-1]
# global count

checklist = [[0]*N for _ in range(N)]
result = [0]*N


def dfs_R(x,y):
    if x>=0 and x<N and y>=0 and y<N:   #0<X<N
        if graph[x][y] == 'R' and checklist[x][y]==0:
            checklist[x][y]=1
            # print(x,y)
            # print(graph[x][y])
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs_R(nx,ny)

def dfs_G(x,y):
    if x>=0 and x<N and y>=0 and y<N:   #0<X<N
        if graph[x][y] == 'G' and checklist[x][y]==0:
            checklist[x][y]=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs_G(nx,ny)

def dfs_B(x,y):
    if x>=0 and x<N and y>=0 and y<N:   #0<X<N
        if graph[x][y] == 'B' and checklist[x][y]==0:
            checklist[x][y]=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs_B(nx,ny)

# def dfs_RG(x,y):
#     if x>=0 and x<N and y>=0 and y<N:   #0<X<N
#         if graph[x][y] == 'R' or graph[x][y] == 'G' and checklist[x][y]==0:
#             checklist[x][y]=1
#             for i in range(4):
#                 nx=x+dx[i]
#                 ny=y+dy[i]
#                 dfs_RG(nx,ny)


count_1 = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' and checklist[i][j]==0:
            # count += 1
            # result[i]+=1
            dfs_R(i,j) 
            count_1+=1
            # print(1)
        elif graph[i][j] == 'G' and checklist[i][j]==0:
            # count += 1
            # result[i]+=1
            dfs_G(i,j) 
            count_1+=1
            # print(2)
        elif graph[i][j] == 'B' and checklist[i][j]==0:
            # count += 1
            # result[i]+=1
            dfs_B(i,j) 
            count_1+=1
            # print(3)

# print(count)
# print(result)
count_2 = 0
checklist = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if graph[i][j] =='G' and checklist[i][j]==0:
            dfs_G(i,j)
            count_2+=1
        elif graph[i][j] == 'B' and checklist[i][j]==0:
            # count += 1
            # result[i]+=1
            dfs_B(i,j) 
            count_2+=1
            # print(3)
    
print(count_1, count_2)

# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 'R' or graph[i][j] == 'G' and checklist[i][j]==0:
#             # count += 1
#             # result[i]+=1
#             dfs_RG(i,j) 
#             count+=1
#             # print(1)
#         elif graph[i][j] == 'B' and checklist[i][j]==0:
#             # count += 1
#             # result[i]+=1
#             dfs_B(i,j) 
#             count+=1
#             # print(3)

# print(count)




# -----------------------------------------------------------------------------------------------------------------------


# import sys
# sys.setrecursionlimit(10000)

# N=int(sys.stdin.readline())
# graph=[]

# for _ in range(N):
#     graph.append(sys.stdin.readline())

# # print(graph[0][0])


# dx=[1,-1,0,0]
# dy=[0,0,1,-1]
# count = 0

# checklist = [[0]*N for _ in range(N)]



# def dfs(x,y,Z):
#     global count
#     print(graph[x][y])
#     if graph[x][y] == Z and checklist[x][y]==0:
#         checklist[x][y]=1
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             dfs(nx,ny)

#     # if graph[x][y] == 'G' and checklist[x][y]==0:
#     #     checklist[x][y]=1
#     #     for i in range(4):
#     #         nx=x+dx[i]
#     #         ny=y+dy[i]
#     #         dfs(nx,ny)

#     # if graph[x][y] == 'B' and checklist[x][y]==0:
#     #     checklist[x][y]=1
#     #     for i in range(4):
#     #         nx=x+dx[i]
#     #         ny=y+dy[i]
#     #         dfs(nx,ny)

# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 'R':
#             count += 1
#             dfs(i,j,'R')      
# print(count)

