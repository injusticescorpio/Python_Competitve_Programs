

def wildcard(s1,s2):
    pass


s1=['*','k']
s2=['g','e','e','k','s']

res=[]
li=[]
for i in range(0,len(s1)):
    if s1[i] == '*':
        res.append(s2[i])
        j=i
        while res[-1]!=s1[i+1]:
            j+=1
            res.append(s2[j])
        res.pop()
    li.append(''.join(res))
k=0
while s1.count('*')!=0:
    s1=[li[k] if i=="*" else i for i in s1]
    print(s1)
if ''.join(s1)==''.join(s2):
    print("true")
else:
    print("false")
