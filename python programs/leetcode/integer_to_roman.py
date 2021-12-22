a=int(input())
s=''
p=['','I','II','III','IV','V','VI','VII','VIII','IX']
while(a!=0):
    if a>=1000:
        d=a%1000
        k=a-d
        s+='M'*(k//1000)
        a=d
    elif a>=900:
        d=a%900
        k=a-d
        s+='CM'
        a=d
    elif a>=500:
        d=a%500
        k=a-d
        s+='D'
        a=d
    elif a>=400:
        d=a%400
        k=a-d
        s+='CD'
        a=d
    elif a>=100:
        d=a%100
        k=a-d
        s+='C'*(k//100)
        a=d
    elif a>=90:
        d=a%90
        k=a-d
        s+='XC'
        a=d
    elif a>=50:
        d=a%50
        k=a-d
        s+='L'
        a=d
    elif a>=40:
        d=a%40
        k=a-d
        s+='XL'
        a=d
    elif a>=10:
        d=a%10
        k=a-d
        s+='X'*(k//10)
        a=d
    else:
        s+=p[a]
        a=0
print(f"string=={s}")








