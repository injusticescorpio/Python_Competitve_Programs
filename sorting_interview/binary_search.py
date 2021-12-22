a=list(map(int,input().split(" ")))
f=0
l=len(a)-1
search=int(input('enter element to search'))
while f<=l:
    mid=(f+l)//2
    if a[mid]==search:
        print(f"element found at pos {mid+1}")
        break
    elif search>a[mid]:
        f=mid+1
    else:
        l=mid-1