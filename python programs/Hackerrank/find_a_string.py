def count_substring(string, sub_string):
    k = len(sub_string)
    c = 0
    for i in range(0, len(string)-k+1):
        print(f"sub=={string[i:k + i]}")
        if string[i:k + i] == sub_string:
            c += 1
    return c

a=input()
b=input()
print(count_substring(a,b))