import sys
N = int(sys.stdin.readline())
rank = []
rank_2 = []
for i in range(N):
    rank.append(int(sys.stdin.readline()))

for i in range(1,N+1):
    rank_2.append(i)

rank.sort()

result=0

for i in range(N):
    result += abs(rank[i]-rank_2[i])

print(result)
