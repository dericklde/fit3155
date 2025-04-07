# naive pattern matching algorithm (code taken from ChatGPT)

def naive_pattern_match(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):  # slide pattern over text
        match = True
        for j in range(m):  # check character by character
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)  # store the starting index of match
    return matches


# basic boyer moore algorithm

def bad_char(pattern):
    # preprocessing bad char rule
    n = len(pattern)
    table = [n] * 256 # char not in pattern shift n times

    for i in range(n-1):
        index = ord(pattern[i]) # ord() returns ASCII value of char
        table[index] = n - i - 1
    return table

def good_suffix(pattern):
    # preprocessing good suffix rule
    m = len(pattern)
    shift = [0] * (m + 1) # + 1 to account for no match case    

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

    j = bpos[0]
    for i in range(m+1): # + 1 to cover full range of shift and bpos
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]    

    return shift, bpos

good_suffix("abbabab")







