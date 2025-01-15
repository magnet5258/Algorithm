T = int(input())
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for test_case in range(1, T + 1):
    x = input()
    bin_str = ""
    dec_str = ""
    for i in range(len(x)):
        val = lst.index(x[i])
        bin_str += f"{val:06b}"
    for i in range(0, len(bin_str), 8):
        byte = bin_str[i:i+8]
        if len(byte) == 8:
            dec_str += chr(int(byte, 2))
    print(f"#{test_case} {dec_str}")
