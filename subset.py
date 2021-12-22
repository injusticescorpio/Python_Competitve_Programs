def main():
    a=[1,2,3]
    comb=[]
    res=[]
    def subset(i):
        if i==len(a):
            res.append(comb[:])
            return
        comb.append(a[i])
        subset(i+1)
        comb.pop()
        subset(i+1)
    subset(0)
    print(res)
main()