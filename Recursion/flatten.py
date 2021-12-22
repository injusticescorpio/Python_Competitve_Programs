def flatten(arr,a=[]):
    for i in range(0,len(arr)):
        if type(arr[i])==int:
            a.append(arr[i])
        else:
            a=flatten(arr[i],a)
    return a
# print(flatten([[[[[[[1]]]]],[[[[[[[2]]]]]]]],[[3,4],6]]))
print(flatten([[1],[2],[3]]))

