import sys

N=int(sys.stdin.readline())

graph=[[' ']*((2*N)-1) for _ in range(N)]
# graph[0][N-1]='*'
for i in range(N):
    if i == 0:
#        graph[i][N-1]='*'
        print(" "*(N-1), "*", sep="")
    elif 0<i<N-1:
        # graph[i][N-i-1]='*'
        print(" "*(N-i-1),"*", " "*((2*i)-1),"*",sep="")
        # graph[i][N+i-1]='*'
        # print(" "*(N+i-1),"*",sep="")
    elif i==(N-1):
        # for j in range((2*N)-1):
        #     graph[i][j]='*'
        print("*"*((2*N)-1))


# for i in range(N):
#     for x in graph[i]:
#         print(x, sep='', end='')
#     print('')





# if
#  N == 1:
#     print("*")
# elif N>1:
# for i in range(N):


    # for j in range(i):
    #     if j==0:
    #         graph[i][N-1]='*'
    #     elif 0<j<N-1:
    #         graph[i][N-j-1]='*'
    #         graph[i][N+j-1]='*'
    #     elif i==(N-1):
    #         graph[i][i]='*'
