from collections import Counter
def makeAnagram(a, b):
    d=Counter(a)
    # print(f"d=={d}")
    for i in b:
        if i in d:
            d[i]=d[i]-1
        else:
            d[i]=-1
    print(d)
    return sum([ abs(i) for i in d.values()])


a = input()
b = input()
print(makeAnagram(a, b))

