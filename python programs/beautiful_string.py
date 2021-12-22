a='0100101010100010110100100110110100011100111110101001011001110111110000101011011111011001111100011101'
# one method
# c=''
# k=0
# i=0
# while i<len(a)-2:
#     for j in range(i,i+3):
#         c+=a[j]
#     if c=='010':
#         k+=1
#         i=j+1
#     else:
#         i+=1
#     c=''
# print(k)
c=0
j=0
b="010"
for i in range(0,len(a)):
    if j<len(b) and a[i]==b[j]:
        j+=1
    elif b[0]==a[i]:
        j=1
    else:
        j=0
    if j==len(b):
        c+=1
        j=0
print(c)







