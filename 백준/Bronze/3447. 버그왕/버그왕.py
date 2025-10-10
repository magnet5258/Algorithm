while True:
    try:
        code = input()
        while 'BUG' in code:
            for i in range(len(code) - 2):
                if code[i:i + 3] == 'BUG':
                    code = code[:i] + code[i + 3:]
        print(code)
    except EOFError:
        break