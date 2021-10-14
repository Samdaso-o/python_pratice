def solution(priorities, location):
    answer = 0
    dic = {}
    for i, j in enumerate(priorities):
        dic[i] = j
        
    maxmum = max(dic.values())
    while dic[location] != 0:
        for k in dic:
            if dic[k] == maxmum:
                answer += 1
            
                if k == location:
                    return answer
            
                dic[k] = 0
                maxmum = max(dic.values())
    
                    
    return answer