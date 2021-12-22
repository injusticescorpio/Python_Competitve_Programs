import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
lst = tuple(map(int, input().split()))
answers = [ lst[0] ]
def find(total, index):
    if index == N:
        return total % 101 == 0
    val = lst[index]
    index += 1
    operindex = len(answers)
    answers.append('*')
    answers.append(val)
    if find(total * val, index):
        return True
    answers[operindex] = '+'
    if find(total + val, index):
        return True
    answers[operindex] = '-'
    if find(total - val, index):
        return True
    answers.pop()
    answers.pop()
    return False
find(lst[0], 1)
print(*answers)

#inputs
#5
#55 3 45 33 25