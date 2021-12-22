# here time complexity is O(n) and space complexity is O(1)
def sum_of_num(n):
    sum=0
    for i in range(n+1):
        sum+=pairsum(i,i+1)
        print(f"sum=={sum}")
    return sum
def pairsum(a,b):
    return a+b
print(sum_of_num(3))