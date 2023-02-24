import sys

N = int(sys.stdin.readline())

maokai = list(map(int,sys.stdin.readline().split()))

maokai.sort(reverse=True)
day = []
result=[]
for i in range(1,N+1):
    day.append(i)

for i in range(N):
    result.append(maokai[i]+day[i])

result.sort(reverse=True)

print(result[0]+1)