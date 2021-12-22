def main():
    k=2
    n=[1,2,3,4]
    comb=[]
    res=[]
    def combinations(i):
        if len(comb)==2:
            res.append(comb[:])
            print(res)
            return
        for i in range(i,len(n)):
            print(f"i=={i}")
            comb.append(n[i])
            combinations(i+1)
            print(f"after i=={i}")
            comb.pop()
    combinations(0)
    print(res)





main()