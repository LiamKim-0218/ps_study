import sys

N,M= map(int,sys.stdin.readline().split())
Book = list(map(int,sys.stdin.readline().split()))


m_list = []
p_list = []
max = 0
result = []

for i in Book:
    if i < 0:
        m_list.append(abs(i))
    elif i > 0:
        p_list.append(i)
    if abs(i)>abs(max):
        max = abs(i)



m_list.sort(reverse=True)
p_list.sort(reverse=True)
for i in range(len(p_list)):
    if i % M == 0:
        result.append(p_list[i])
for i in range(len(m_list)):
    if i % M == 0:
        result.append(m_list[i])

# print(result)
result = (sum(result)*2) - max
print(result)

