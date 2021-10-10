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