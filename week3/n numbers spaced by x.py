def solution(x, n):
    answer = []
    if x!=0:
        for i in range(x,x*(n+1),x):
            answer.append(i)
            print(i)    
    # if x<0:
    #     for i in list(range(x,x*n-1,x)):
    #         answer.append(i)
            # print(i)
    # if x == 0: 
    #     answer.append(x)
    if x == 0: 
        answer = [0] * n
        # for i in range(n):
        #     answer.append(0)
    return answer




# def solution(x, n):
#     answer = []
#     buf = x
#     for x in range(1,n+1):
#         # print(x)
#         answer.append(buf*x)
#     return answer