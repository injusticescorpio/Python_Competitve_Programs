n=int(input())
a=list(map(int,input().split(' ')))
print(len(a))
while(len(a)!=1):
    min_element=min(a)
    a=[i-min_element for i in a]
    a=list(filter(lambda x:x!=0,a))
    if a==[]:
        break
    print(len(a))