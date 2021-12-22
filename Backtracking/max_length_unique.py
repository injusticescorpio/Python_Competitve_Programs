def main():
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    res=[]
    comb=[]
    max_length=4
    def dfs(i):
        if i==len(arr) or len(set(''.join(comb)))==max_length:
            if len(set(''.join(comb)))==len(''.join(comb)):
                res.append(''.join(comb[:]))
            return
        comb.append(arr[i])
        dfs(i+1)
        comb.pop()
        dfs(i+1)
    dfs(0)
    print(res)
main()
