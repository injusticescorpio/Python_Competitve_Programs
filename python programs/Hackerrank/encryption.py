import math
def compute(row,col,a):
    str=' '+a
    k=[]
    res=[]
    for i in range(1,len(str)):
        if i%col==0:
            k.append(str[i])
            res.append(k)
            k=[]
        else:
            k.append(str[i])
    t=len(k)
    while t!=col:
        k.append('')
        t+=1
    res.append(k)
    for i in list(zip(*res)):
        print(''.join(list(i)),end=' ')
str=input()
a=str.replace(' ','')
row=math.floor(len(a)**0.5)
col=math.ceil(len(a)**0.5)
print(f"row={row}")
print(f"col={col}")
if row*col>=len(a):
    compute(row, col,a)
elif row<col:
    compute(row+1, col, a)
else:
    compute(row, col+1, a)