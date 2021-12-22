def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr,cb):
    print(f"arr=={arr}")
    if isOdd(arr[0]):
        return True
    elif len(arr) == 0:
        return False
    else:
        someRecursive(arr[1:],cb)

print(someRecursive([2,4,5],isOdd))