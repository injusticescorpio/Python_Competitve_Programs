def comb(haystack,needle):
    stack = []
    j = 0
    l = len(needle)
    for i in range(0, len(haystack)+1):
        if haystack[i] == needle[j]:
            stack.append(i)
            j += 1
        else:
            j = 0
            stack = []
        if len(stack) == l or l == 0:
            return stack[0]
    return -1
print(comb('',''))