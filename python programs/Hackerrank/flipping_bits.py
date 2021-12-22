n=int(input())
a=list(int(input()) for i in range(n))
for i in a:
    bin_value1 = bin(i).replace('0b', '')
    bin_32 = '0' * (32 - len(bin_value1)) + bin_value1
    # flipped_bits = ''.join(['1' if i == '0' else '0' for i in bin_32])
    print(int(''.join(['1' if i == '0' else '0' for i in bin_32]), 2))
