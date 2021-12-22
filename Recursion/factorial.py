# eg:5!=5*4!=>n!=n*(n-1)!
import  sys
sys.setrecursionlimit(1000)
def fact(n):
    assert n>=0 and int(n)==n,"n needs to be positive and no decimal part is present"
    if n in [0,1]:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))

# working
# fact(4)
#     4*fact(3)=>4*6=24 it will return 24 thats the output
#         3*fact(2)=>2*3=6 it will return 6
#             2*fact(1)(it will return 2*1=2)