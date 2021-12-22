n=int(input())
a=[int(i) for i in input().split(' ')]
l=int(input())
players=list(map(int,input().split(' ')))
a=sorted(set(a),reverse=True)
players=sorted(players,reverse=True)
print(a)
print(players)
p=[]
j=0
for player in players:
    print(f"player=={player}")
    while j<len(a) and player<a[j]:
        j=j+1
        print(f"j=={j}")
    p.append(j+1)
for i in sorted(p,reverse=True):
    print(i)

