import sys

N = int(sys.stdin.readline())

book=[]
for i in range(N):
    book.append(int(sys.stdin.readline()))

cnt=0
flag = True

while flag:
    for i in range(N-1):    
        if book[i] > book[i+1]:
            book.insert(0,book[i+1])
            book.pop(book[i+1])
            cnt += 1
            # flag = True
            break
        # flag = False
        if i == N-1:
            flag = False

# print(book)
print(cnt)

    



# for i in range(N):
#     if book[0] > book[-1]:
#         continue
#     if book[i] < book[i-1]:
#             buf = book[i-1]
#             book[i-1]=book[i]
#             book[i] = buf
#             cnt += 1
            



