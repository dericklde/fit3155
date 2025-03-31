def bad_char(pattern):
    # preprocessing bad char rule
    n = len(pattern)
    table = [n] * 256 # char not in pattern shift n times

    for i in range(n-1):
        index = ord(pattern[i]) # ord() returns ASCII value of char
        table[index] = n - i - 1
    return table

def gsuff_case1(pattern):
    # preprocessing good suffix rule
    m = len(pattern)
    shift = [0] * (m + 1)

    i = m
    j = m + 1
    bpos = [0] * (m + 1)
    bpos[i] = j

    while i > 0:
        while j <= m and pattern[i-1] != pattern[j-1]:
            if (shift[j] == 0):
                shift[j] = j-i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j

    def gsuff_case2(shift, bpos):
        j = bpos[0]
        for i in range(m):
            if shift[i] == 0:
                shift[i] = j
            if i == j:
                j = bpos[j]    
        return shift, bpos
    
    shift, bpos = gsuff_case2(shift, bpos)

    return shift, bpos

gsuff_case1("abbabab")







