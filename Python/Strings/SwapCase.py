def swap_case(s):
    res = ''
    for x in s:
        if(x >= 'a' and x <= 'z' or x >= 'A' and x <= 'Z'):
            if(x.islower()):
                res = res + x.upper()
            else:
                res = res + x.lower()
        else:
            res = res + x
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
