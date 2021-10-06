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