def solution(s):
    answer = True
    stack_list = list()

    def push(data):
        stack_list.append(data)

    def pop():
        data = stack_list[-1]
        del stack_list[-1]
        return data 
    
    for i in s:
        if '(' == i:
            push(i)
        if i ==')':
            if len(stack_list) == 0:
                return False
            else:
                pop()
                #return False
                
    if len(stack_list) != 0:
        return False
    
            
            
            
            
            
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True