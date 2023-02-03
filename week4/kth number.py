def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i == j:
            answer.append(array[i-1])
            continue

        n = array[i-1:j]
        n.sort()

        result = n[k-1]
        answer.append(result)

    return answer