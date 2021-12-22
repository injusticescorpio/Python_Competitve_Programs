a=[1, 1, 1, 0, 1, 1, 0,0, 0, 0]
energy=100
k=3

i=0
while(i<len(a) and (i==0 or i%len(a)!=0)):
    if a[i]==0:
        energy-=1
    else:
        energy-=3
    i+=k
    print(f"i=={i}")
    print(f"energy=={energy}")

