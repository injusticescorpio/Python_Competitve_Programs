def main():
    res=[]
    part=[]
    s='aab'
    def palin(s):

        if s==s[::-1]:
            print(f"s=={s} True")
            return True
        else:
            print(f"s=={s} False")
            return False
    def dfs(i):
        if i==len(s):
            res.append(part[:])
            return
        for j in range(i,len(s)):
            print(f"i=={i} and j=={j}",end=' ')
            if palin(s[i:j+1]):
                part.append(s[i:j+1])
                print(f"part=={part}")
                dfs(j+1)
                part.pop()
            print(f"else i=={i} and j=={j} part={part}")

    dfs(0)
    print(res)
main()