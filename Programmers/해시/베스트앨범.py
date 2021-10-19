def solution(genres, plays):
    answer = []
    dic = {}
    count = 0
    for k,i,j in zip(range(0,len(genres)-1),genres, plays):
        if i in dic:
            dic[i].append([k,j])
        else:
            dic[i] = [k,j]
    
    for i in dic: