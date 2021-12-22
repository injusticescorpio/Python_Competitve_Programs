def pairSum(myList, sum):
    l=[]
    for i in range(0,len(myList)-1):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==sum:
                l.append(f'{myList[i]}+{myList[j]}')
    return l

print(pairSum([2,4,3,5,6,-2,4,7,8,9],7))


