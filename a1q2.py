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


# optimised boyer moore algorithm for binary strings

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

    # matched prefix shift
    j = bpos[0]
    for i in range(m+1): # + 1 to cover full range of shift and bpos
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]    

    return shift

# search for pattern in text
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    res = []

    shift = good_suffix(pattern)

    k = m
    while k <= n:
        i = m
        h = k
        while i > 0 and pattern[i-1] == text[h-1]:
            i = i - 1
            h = h - 1
        if i == 0:
            res.append(h)
            k = k + m - shift[i]
        else:
            k += shift[i]

    return res 

print(boyer_moore('0011010101111001001101100','010'))







