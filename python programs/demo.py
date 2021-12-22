def stringAnagram(dictionary, query):
    d=[]
    q=[]
    di={}
    res=[]
    for i in dictionary:
        d.append(''.join(sorted(i)))
    for j in query:
        q.append(''.join(sorted(j)))
    print(f"d=={d}")
    print(f"q=={q}")
    for i in d:
        if i not in di:
            di[i]=1
        else:
            di[i]+=1
    for i in q:
        if i in di:
            res.append(di[i])
        else:
            res.append(0)
    return res

print(stringAnagram(['hack','a','nark','a'],['a']))