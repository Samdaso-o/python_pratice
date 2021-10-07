#백준 10818
n = int(input())
list1 = list(map(int, input().split()))
max = 0
min = list1[0]

for i in range(n):
    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
print(min, max)

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