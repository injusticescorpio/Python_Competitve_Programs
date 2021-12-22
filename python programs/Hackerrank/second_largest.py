#method 1
a=list(map(int,input().split(' ')))
max_element=min(a)
for i in range(0,len(a)):
    if max_element<a[i] and a[i]!=max(a):
        max_element=a[i]
print(f"second max_element using approach 1 is {max_element}")
#method 2
a=sorted(a,reverse=True)
p=a[0]
j=0
while(a[j]==p):
    j+=1
print(f"second max_element using approach 2 is {a[j]}")