import sys

read = sys.stdin.readline

N = int(read())
cranes = list(map(int, read().split()))

M = int(read())
boxs = list(map(int, read().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]:
    print(-1)
    sys.exit()
else:
    time = 0

    while boxs:
        if not boxs:
            break

        for i in cranes:
            for j in boxs:
                if i >= j:
                    boxs.remove(j)
                    print(boxs)
                    break

        time += 1

    print(time)





# ------------------------------------------------------------------




# from collections import deque
# import sys
# sys.setrecursionlimit(10000)

# N = int(sys.stdin.readline())
# crane = list(map(int,sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# box = list(map(int,sys.stdin.readline().split()))


# visited = [0]*(N+1)

# def bfs(V):
#     q = deque([V])
#     visited[V]=1
#     while q:
#         V=q.popleft(0)
#         print(V, end='')
#         for i in range(N):
#             if graph[V][i]==0 and visited[V]==1:
#                 q.append(i)
#                 visited[i] = 1
#                 bfs(i)



# def bfs(V):
#     q = deque(crane)
#     while q:
#         for i in range(M):
#             if crane[i] >= box[i]:




#  (M//N)+(M%N):

    


# # if graph[V][i] == 1 and visited[i] == 0:
# #                 q.append(i)

# # if queue[i] >= box[i]:

# # queue = [crane]
# # print(queue)
# # # while queue:
# # #     for i in range(len(crane)):
        