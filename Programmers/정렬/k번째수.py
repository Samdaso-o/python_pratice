def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        h = array[i-1:j]
        h.sort()
        q = h[k-1]
        answer.append(q)
    return answer