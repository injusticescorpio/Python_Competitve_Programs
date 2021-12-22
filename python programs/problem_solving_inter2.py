def numPlayers(k, scores):
    scores=sorted(scores,reverse=True)
    d={}
    for i in range(0,len(scores)):
        if scores[i] not in d and scores[i]!=0:
            d[scores[i]]=i+1
        else:
            d[0]=0
    li=[]
    for i in scores:
        li.append(d[i])
    l=0
    for i in li:
        if i<=k:
            l+=1
    return l


print(numPlayers(4,[2,2,3,4,5]))