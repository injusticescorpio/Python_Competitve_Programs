def hackerrankInString(s):
    p='hackerrank'
    j=0
    k=''
    for i in p:
        while j<len(s) and i!=s[j]:
            j+=1
        if j==len(s) and k!='hackerrank':
            return 'No'
        k+=s[j]
        if k==p:
            return 'Yes'
        j+=1
    return  'No'
a=input()
print(hackerrankInString(a))