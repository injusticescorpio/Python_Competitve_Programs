def power_set(li,i,result=[],subset=[]):
    print(f"res=={result}")
    print(f"subset=={subset}")
    if i>=len(li):
        result.append(subset[:])
        return
    subset.append(li[i])
    power_set(li,i+1,result,subset)
    subset.pop()
    power_set(li,i+1,result,subset)
    return result

li=[1,2,3]
print(power_set(li,0))
