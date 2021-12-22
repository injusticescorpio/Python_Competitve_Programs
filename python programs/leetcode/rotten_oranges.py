a=[
    [2,1,1],
    [0,1,0],
    [0,1,1]
]

queue=[]
time=0
fresh=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i][j]==2:
            queue.append((time,i,j))
        elif a[i][j]==1:
            fresh+=1

print(f"queue=={queue}")
print(f"fresh=={fresh}")
while queue!=[]:
    time,i,j=queue.pop(0)
    #top
    if i>0 and a[i-1][j]==1:
        pass


    #bottom
    if j<len(a) and a[i][j-1]==1:
        pass
    #left

    #right

