def solution(phone_number):
    answer = ''
    # p_str = str(phone_number)
    p_list = list(phone_number)
    print(phone_number)
    for i in range(len(p_list)-4):
        answer+='*'
    
    for i in range(len(p_list)-4,len(p_list)):
        answer += p_list[i]
    
    
    return answer