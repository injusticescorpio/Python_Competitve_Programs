def valid(val):
    if check_all_same(val):
        return 'YES'
    else:
        c=0
        for i in val:
            if i==1:
                c+=1
                print(f"c=={c}")
        if c==1:
            print(f'len=={len(val)}')
            if (sum(val)-1)%(len(val)-1)==0:
                return 'YES'
            else:
                return 'NO'
        else:
            if sum(val)%len(val)-1==0 and max(val)-1==min(val):
                return 'YES'
            else:
                return 'NO'

def check_all_same(arr):
    p=arr[0]
    c=0
    for i in range(1,len(arr)):
        if p==arr[i]:
            c+=1
    if c==len(arr)-1:
        return True
    else:
        return False



from collections import Counter
counter = Counter(input())
print(f"counter_len=={len(counter)}")
val=list(counter.values())
print(val)
print(valid(val))