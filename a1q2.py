# Name: Douh Ee Leu
# Student ID: 31841716

# Boyer-Moore algorithm implemented using pseudocode taken from http://web.archive.org/web/20200427070016/https://www.inf.hs-flensburg.de/lang/algorithmen/pattern/bmen.htm
# Galil's optimisation implemented using Week 2 Lecture notes by Taylor Kearney

# Function to calculate good suffix shift and matched prefix shift
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

# Optimised boyer moore algorithm for binary strings
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    res = []
    count = 0
    
    shift = good_suffix(pattern)

    # initial start and stop pointers (to make sure false for all j as we haven't match with pattern yet)
    start = m
    stop = -1

    i = 0
    while (i <= n - m):
        j = m - 1
        while j >= 0:
            # check if j is within the matched region after shift
            if start <= j <= stop:  
                j = start - 1 # skip to index one element to the left of the matched region 
                continue 
            count += 1
            if pattern[j] != text[i + j]:
                break
            j -= 1
        # check whether we found a pattern or not and shift pattern accordingly
        if j < 0:
            res.append(i)
            i += shift[0]
        else:
            i += shift[j+1]
        # calculate new start and stop pointers to skip comparisons (all pointers subtracted 1 as 0-indexed)
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










