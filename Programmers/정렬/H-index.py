#처음
def solution(citations):
    answer = 0
    if len(citations) == 1:
        return 1
    citations.sort(reverse=True)
    if citations[0] == 0:
        return 0
    for i,j in enumerate(citations):
        if i < j:
            pass
        elif i == j:
            answer = j
            return answer
        elif i > j:
            answer = citations[i-1] 
            return answer
        else:
            return len(citations)
    return answer

#해결 
def solution(citations):
    answer = 0
    citations.sort()
    counts = len(citations)

    for i in range(counts):
        if citations[i] >= counts-i:
            return counts-i
    return 0