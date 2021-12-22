s=input()
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#ii iiD,
#
#
#
c=0
for i in range(len(s)):
    if s[i]=='M':
        c+=d[s[i]]
    elif s[i]=='D':
            c+=d[s[i]]
    elif s[i]=='C':
        if i==len(s)-1:
            c+=d[s[i]]
            break
        elif s[i+1]=='M' or s[i+1]=='D':
            c-=100
        else:
            c+=d[s[i]]

    elif s[i]=='L':
        c+=d[s[i]]
    elif s[i]=='X':
        if i==len(s)-1:
            c+=d[s[i]]
            break
        elif s[i + 1] == 'L' or s[i + 1] == 'C':
            c -= 10
        else:
            c+=d[s[i]]
    elif s[i]=='V':
        c+=d[s[i]]
    elif s[i]=='I':
        if i==len(s)-1:
            c+=d[s[i]]
            break
        elif s[i + 1] == 'X' or s[i + 1] == 'V':
            c -= 1
        else:
            c+=d[s[i]]
    else:
        break

print(f"c=={c}")


