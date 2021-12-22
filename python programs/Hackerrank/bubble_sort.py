def countSwaps(a):
    swaps=0
    for i in range(0, len(a)):
        c=0
        for j in range(0, len(a)-1):
            if a[i] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps+=1

        print(f'a=={a}')
    print(f"swaps=={swaps}")



a=[6,4,1]
countSwaps(a)