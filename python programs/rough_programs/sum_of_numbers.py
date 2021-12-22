import time
a=12312312312312312312312311233737338373737837378377387373175715275217512527515151551751765117
def sum_loop(a):
    start_time = time.time()
    s=0
    while(a>0):
        d=a%10
        s+=d
        a//=10
    end_time = time.time()
    elapsed_time = end_time-start_time
    print(f"time taken :", elapsed_time)
    return(s)

def getSum(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)



def sum_list(n):
    strr = str(n)
    return sum((int(i) for i in strr))

print(sum_loop(a))
t = time.process_time()
print(getSum(a))
elapsed_time = time.process_time() - t
print(f"time taken :",elapsed_time)
print(getSum(a))
print(sum_list(a))