from itertools import combinations
def count(d):
    return d.count('0')

m,n=list(map(int,input().split(' ')))
topic=list(input() for i in range(m))
# print(topic)
a=[i for i in range(m)]
team_score=[]
for i in list(combinations(a,2)):
    # print(i)
    team_score.append((bin(int(topic[i[0]],2)| int(topic[i[1]],2))[2:]).count('1'))

# print(team_score)
print(max(team_score))
print(team_score.count(max(team_score)))
