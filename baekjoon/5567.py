import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
count=0

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1 


def bfs(V):
	global count
	q=deque()
	q.append(V)
	for i in friends:
		q.append(i)
	while q:
		V = q.popleft()
		for i in range(1,n+1):
			if (visited[i] == 0 and graph[V][i] == 1):
				visited[i]=1
				count +=1

friends = []
for i in range(1,n+1):
    if graph[1][i] == 1:
        friends.append(i)
bfs(1)

if count != 0:
	count -= 1
	
print(count)


			

# def dfs(i):
#     visited[i]=1
#     for i in range(1,n+1):
#         if visited == 0 and  graph[a][b] == 1:
#             dfs(i)
    
# dfs(1)


# from sys import stdin

# n = int(stdin.readline().strip())
# graph = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)
# for _ in range(int(stdin.readline().strip())):
# 	x, y = map(int, stdin.readline().split())
# 	graph[y].append(x)
# 	graph[x].append(y)

# cnt = 0
# visited[1] = 1
# for i in graph[1]:
# 	if not visited[i]:
# 		visited[i] = 1
# 		cnt += 1
# 	for j in graph[i]:
# 		if not visited[j]:
# 			visited[j] = 1
# 			cnt += 1

# print(cnt)	