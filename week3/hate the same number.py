import queue

def solution(arr):
    answer = []
    #answer.append(arr[0])
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i])
            
#     answer.append(arr[len(arr)-1])
        
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

    data_queue = queue.Queue()
    for i in arr:
        data_queue.put(i)
    
    buf = data_queue.get()
    answer.append(buf)
    val=0
    for i in range(len(arr)-1):
        val=data_queue.get()
        if buf!=val:
            answer.append(val)
            buf=val
        
    
    return answer