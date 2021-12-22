#newyear chaos
a=[int(i) for i in input().split(' ')]
swaps=0
for i in range(len(a)-1,-1,-1):
    if a[i]!=i+1:
        if a[i-1]==(i+1):
            a[i],a[i-1]=a[i-1],a[i]
            swaps+=1
        elif a[i-2]==(i+1):
            a[i],a[i-1]=a[i-1],a[i]
            a[i],a[i-2]=a[i-2],a[i]
            swaps+=2
        else:
            print("Too chaoitic")
            break
    print(f"a=={a}")
print(f"swaps=={swaps}")






