N = int(input())
binary_32bit = format(N, '032b')
flipped = ''.join('1' if bit == '0' else '0' for bit in binary_32bit)
flipped_int = int(flipped, 2) + 1
twos_complement = format(flipped_int, '032b')

cnt = 0
for i in range(32):
    if binary_32bit[i] != twos_complement[i]:
        cnt += 1

print(cnt)