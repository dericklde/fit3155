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

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    res = []
    count = 0
    
    shift = good_suffix(pattern)

    start = m
    stop = -1

    i = 0
    while (i <= n - m):
        j = m - 1
        while j >= 0:
            if start <= j <= stop:  
                j = start - 1 # skip to index one element to the left of the matched region 
                continue 
            count += 1
            if pattern[j] != text[i + j]:
                break
            j -= 1
        if j < 0:
            res.append(i)
            i += shift[0]
        else:
            i += shift[j+1]
        # calculate new start and stop pointers to skip comparisons
        # subtract 1 for 0-index 
        if shift[j] < m - j:
            p = shift[j] + j
            stop = p - 1
            start = p - m + j 
        elif shift[j] == m - j:
            stop = m - shift[j] - 1
            start = 0
        else: # reset it or else it would carry forward start and stop from past shift
            start = m
            stop = -1
    return res










