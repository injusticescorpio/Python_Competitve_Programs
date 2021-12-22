graph=[2,1,5,6,2,3]

stack_left=[0]
left=[0]

for i in range(1,len(graph)):
    while stack_left!=[] and graph[i]<=graph[stack_left[-1]]:
        stack_left.pop()
    if stack_left==[]:
        left.append(0)
    else:
        left.append(stack_left[-1]+1)
    stack_left.append(i)
print(left)
##right part
stack_right=[len(graph)-1]
right=[len(graph)-1]
for i in range(len(graph)-2,-1,-1):
    while stack_right!=[] and graph[i]<=graph[stack_right[-1]]:
        stack_right.pop()
    if stack_right==[]:
        right.append(len(graph)-1)
    else:
        right.append(stack_right[-1]-1)
    stack_right.append(i)
right=right[::-1]
print(right)
area=[]
for i in range(0,len(graph)):
    area.append(graph[i]*(abs(left[i]-right[i])+1))
print(area)
print(max(area))








