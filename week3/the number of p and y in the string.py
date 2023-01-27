# import queue
def solution(s):
    answer = True
#     data_queue=queue.Queue()
#     for i in s:
#         data_queue.pop(i)
        
#     while data_queue
    
    # s.lower() s를 소문자로 출력  s.upper() s를 대문자로 출력
    # 예를 들어 return s.lower().count('p') == s.lower().count('y')
    
    p_nums=0
    y_nums=0
    for i in s:
        if i == 'p' or i == 'P':
            p_nums=p_nums+1
        if i == 'y' or i == 'Y':
            y_nums=y_nums+1    
    print(p_nums)
    if p_nums!=y_nums:
        return False
    else:
        return True
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True