def solution(numbers):
    list1 = [str(i) for i in numbers]
    list1.sort(key=lambda num: num*3, reverse=True)
    answer = str(int(''.join(list1)))
    return answer