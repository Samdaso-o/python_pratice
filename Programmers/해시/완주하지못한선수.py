#프로그래머스 hash 1단계
def solution(participant, completion):
    dic = {}
    hashvalue = 0
    
    for i in participant:
        dic[hash(i)] = i
        hashvalue += hash(i)
    for j in completion:
        hashvalue -= hash(j)
    return dic[hashvalue]