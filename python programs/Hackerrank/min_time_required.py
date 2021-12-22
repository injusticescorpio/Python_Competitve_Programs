a=[2,3,2]
goal=10

day=min(a)
div_sum=0
while(True):
    div_sum=sum(day//i for i in a)
    if div_sum==goal:
        print(day)
        break
    else:
        div_sum=0
        day+=1
