n=int(input())
a=[]
while(n>0):
   a.append(int(input()))
   n-=1
candies1=[1]*(len(a))
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        candies1[i]=candies1[i-1]+1
a=a[::-1]
candies2=[1]*len(a)
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        candies2[i]=candies2[i-1]+1
candies2=candies2[::-1]
print(sum([max(i,j) for i,j in zip(candies1,candies2)]))

