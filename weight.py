#string palindrome


s=['A','B','C']
def permute(s,f):
    if f==len(s):
        print(''.join(s))
    for i in range(f,len(s)):
        s[f],s[i]=s[i],s[f]
        permute(s,f+1)
        s[f],s[i]=s[i],s[f]
permute(s,0)


