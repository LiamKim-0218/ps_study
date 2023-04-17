import sys

N, K = map(int,sys.stdin.readline().split())
money=[]
for _ in range(N):
    money.append(int(sys.stdin.readline())) 

count=0
# money.sort(reverse=True)
# for i in range(N-1,0,-1):

for i in range(N-1,-1,-1):
    if money[i]<=K:
        buf=K//money[i]
        K= K-(buf*money[i])
        count+=buf
    elif K==0:
        # print(count)
        break




# for i in money[::-1]:
#     if i<K:
#         buf=K//i
#         K= K-(buf*i)
#         count+=buf
#     # if K==0:
#     #     # print(count)
#     #     break




# for i in range(N-1,0,-1):
#     if money[i]<K:
#         buf=K//money[i]
#         K= K-(buf*money[i])
#         count+=buf
#     if K==0:
#         # print(count)
#         break

print(count)