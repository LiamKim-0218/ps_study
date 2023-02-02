def solution(numbers):
    answer = 0
    numbers.sort()
    
    max_index = 0
    second_index = 0
    for i in range(len(numbers)):
        if numbers[max_index]<numbers[i]:
            max_index=i
            
    for j in range(len(numbers)-1):
        if numbers[second_index]<=numbers[j]:
            second_index=j
            
            answer=numbers[max_index]*numbers[second_index]
    return answer





# def solution(numbers):
#     answer = 0
#     max_index = 0
#     second_index = 0
#     for i in range(len(numbers)):
#         if numbers[max_index]<numbers[i]:
#             max_index=i
#             for j in range(len(numbers)):
#                 if numbers[second_index]<numbers[j] and numbers[second_index]!=numbers[max_index]:
#                     second_index=j
#                     print(second_index)
#                     answer=max_index*second_index
#     return answer