def main():
    a=[1,1,1,4]
    comb=[]
    def combination(i,ele):
        if len(comb)>len(a):
            return
        if sum(comb)==ele:
            return True
        for i in range(i,len(a)):
            comb.append(a[i])
            if combination(i+1,ele):
                return True
            comb.pop()
        return False
    print(combination(0,5))
main()


