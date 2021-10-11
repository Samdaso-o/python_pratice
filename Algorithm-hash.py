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


#프로그래머스 hash 2단계
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True

#프로그래머스 hash 2-2단계 위장
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = value
            
    for j in dic.key():
        answer = answer * (len(dic[j])+1)
    return answer-1

# hash 2-2 성공 로직 
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
            
    for j in dic.values():
        answer *= len(j) + 1
    return answer-1