import math
def squares(a, b):
    a=math.sqrt(a)
    b=math.sqrt(b)
    return (math.floor(b)-math.ceil(a))+1
print(squares(17,24))