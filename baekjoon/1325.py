from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)
result = []
max_cnt = 0
for i in range(1, n + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)



# -----------------------------------------------------------------------------------------------------------------





# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m = map(int,input().split())

# def bfs(start):
# 	cnt = 1
# 	queue = deque([start])
# 	visit = [0 for _ in range(n+1)]
# 	visit[start] = 1

# 	while queue:
# 		cur = queue.popleft()

# 		for nx in graph[cur]:
# 			if visit[nx]==0:
# 				visit[nx] = 1
# 				cnt += 1
# 				queue.append(nx)

# 	return cnt

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
# 	a,b = map(int,input().split())
# 	graph[b].append(a)

# maxCnt = 1
# ans = []

# for i in range(1,n+1):
# 	cnt = bfs(i)
# 	if cnt > maxCnt:
# 		maxCnt = cnt
# 		ans.clear()
# 		ans.append(i)
# 	elif cnt == maxCnt:
# 		ans.append(i)

# print(*ans)



# ------------------------------------------------------------------------

#내가 한 풀이

from collections import deque
import sys
# sys.setrecursionlimit(10000)

N, M = map(int,sys.stdin.readline().split())

graph=[[0]*(N+1) for _ in range(N+1)]
checklist=[0]*(N+1)
result = []
# count = 0
num = 0

for _ in range(M):
    x, y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1

for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    graph[y].append(x)

def bfs(V):
    global num

    q = deque([V])
    checklist[V] = 1
    while q:
        V = q.pop()
        for i in range(1,N+1):  #더 공부하귀
            if checklist[i] == 0 and graph[i][V]==1:
                q.append(i)
                num+=1
    return num


list_num = [0]*(N+1)
for i in range(1,N+1):
    list_num[i] = bfs(i)
    # print(i, list_num[i])
    checklist=[0]*(N+1)
    num=0

for i in range(len(list_num)):
    if list_num[i] == max(list_num):
        print(i,end=' ')
        
# print(result)

# -----------------------------------------------------------------------------------------------


# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if graph[i][j] == 1:
#             checklist[i] += 1


# for i in range(1,N+1):
#     if graph[checklist.index(max(checklist))][i] == 1:
#         print(i,end=' ')

            




# max(checklist)
# print(checklist.index(max(checklist))
# )






# def bfs(V):
#     queue = deque([V])
#     checklist[V] = 1
#     while queue:
#         for i in range(1, N+1):
#             if checklist[V] == 0 and graph[V][i] == 1:
#                 queue.append(i)



    











# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if graph[i][j]==

# def dfs(V):
#     checklist[V]=1
#     for i in range(1,N+1):
#         if checklist[V] == 0 and graph[V][i] == 1:
#             result.append
#             dfs(i)

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if graph[i][j] == 1:
