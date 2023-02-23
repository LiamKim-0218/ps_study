n, W = map(int,input().split())
graph= []
for i in range(n):
    graph.append(int(input()))


# value = 0
# remainder = 0
coin = 0

for i in range(n-1):
    if graph[i] < graph[i+1]:
        coin += W // graph[i]
        W = W % graph[i]

    elif graph[i] > graph[i-1]:
        W += coin*graph[i]
        coin = 0

if coin != 0:
    W += coin*graph[-1]

print(W)
    

