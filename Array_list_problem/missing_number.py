# 1st method
# def missingNumber(myList, totalCount):
#     print(myList)
#     a=[i for i in range(1,totalCount+1)]
#     print(a)
#     for i in a:
#         if i not in myList:
#           print(i)
# 2nd Method


# def missingNumber(myList, totalCount):
#     j=0
#     myList=myList+[None]*(totalCount-len(myList))
#     for i in range(1,totalCount+1):
#         print(f"j=={j}")
#         while(j<=len(myList)):
#             if myList[j]==i:
#                 j+=1
#                 break
#             else:
#                 print(i)
#                 break
#

# Third method

def missingNumber(myList, totalCount):
    print(set([i for i in range(1,totalCount+1)])-set(myList))




missingNumber([1,3,4,6,8],10)
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 6



