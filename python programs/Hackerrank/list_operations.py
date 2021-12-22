li=[]
def append(data):
    li.append(data)
def sorting(li):
    li.sort()
def display(li):
    print(li)
def reversed(li):
    li.reverse()
def pop():
    li.pop()
def remove(item):
    li.remove(item)
def insert(data,index):
    li.insert(data,index)
n=int(input())
for i in range(n):
    l=input().split(' ')
    if l[0]=='append':
        append(int(l[1]))
    elif l[0]=='sort':
        sorting(li)
    elif l[0]=='reverse':
        reversed(li)
    elif l[0]=='print':
        display(li)
    elif l[0]=='pop':
        pop()
    elif l[0]=='insert':
        insert(int(l[1]),int(l[2]))
    elif l[0]=='remove':
        remove(int(l[1]))


