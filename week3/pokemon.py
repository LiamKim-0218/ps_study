def solution(nums):
    answer = 0
    count=0
    dic={}
    #dic[nums[1]]=0
    for i in range(len(nums)):  #range가 있으면 0,1,2,3이런 식으로 들어가고
        dic[nums[i]]=0          #len만있으면 4가 들어간다
            
    # print(len(dic))    
    # for i in range(len(nums)):
    #     i= i+1
    #     print(i)
    # if len(dic)%2 !=0:
    #     answer = len(dic)-1
    # print(i)
    po_nums=len(nums)/2
    nocopy=len(dic)
    if po_nums>nocopy:
        answer= nocopy
    else:
        answer=po_nums
    # if po_nums<nocopy:
    #     answer=po_nums
    # if po_nums==nocopy:
    #     answer=nocopy
    return answer