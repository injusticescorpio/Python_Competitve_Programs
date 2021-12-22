q=int(input(''))
total_time=int(input(''))
li=[tuple(map(int,input().split(' ')))[:2] for j in range(q)]
#Assuming marks for question is provided in an unordered way.
#sorting
li1=sorted(li,key=lambda x:x[1],reverse=True)
marks=0
i=0
while total_time!=0:
    print(li1[i])
    if i==len(li1):
        break
    elif li1[i][1]<=total_time:
        marks+=li1[i][0]*(total_time//li1[i][1])
        total_time=total_time%li1[i][1]
        i+=1

    else:
        i+=1
print(marks)


