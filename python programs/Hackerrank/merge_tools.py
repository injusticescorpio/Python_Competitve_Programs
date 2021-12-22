def merge_the_tools(string, k):
    li=[]
    for i in range(0,len(string),k):
        li.append(string[i:i+k])
    for i in li:
        s=''
        for j in i:
            if j not in s:
                s+=j
        print(s)

string, k = input(), int(input())
merge_the_tools(string, k)