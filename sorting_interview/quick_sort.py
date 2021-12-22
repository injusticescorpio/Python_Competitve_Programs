def quick_sort(a,first,last):
    if first<last:
        p = partition(a, first, last)
        quick_sort(a, first, p - 1)
        quick_sort(a, p + 1, last)
    return a
def partition(a,first,last):
    pivot=a[first]
    left=first+1
    right=last
    while True:
        while left <=right and a[left]<=pivot:
            left=left+1
        while left<=right and a[right]>=pivot:
            right=right-1
        if left>right:
            a[first],a[right] = a[right],a[first]
            break
        else:
            a[left],a[right] = a[right],a[left]
    return right

a=[5,4,3,2,1,1,3]
print(quick_sort(a,0,len(a)-1))