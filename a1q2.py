# naive pattern matching algorithm (code taken from ChatGPT)

def naive_pattern_match(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)
    count = 0
    for i in range(n - m + 1):  # slide pattern over text
        match = True
        for j in range(m):  # check character by character
            count += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)  # store the starting index of match
    print("naive comparisons:",count)
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

# # search for pattern in text
# def boyer_moore(text, pattern):
#     m = len(pattern)
#     n = len(text)
    
#     res = []
#     count = 0
    
#     shift = good_suffix(pattern)
#     print("shift array:", shift)
#     # initial start and stop pointers to make sure all i is false for start <= i <= stop
#     start = m
#     stop = -1

#     k = m # k is the current element align with right end of the pattern
#     while k <= n:
#         i = m   # i is current element in pattern
#         h = k   # h is the element in text align with the current i 
#         while i > 0:
#             # check whether i is in matched region after shift
#             if start <= i <= stop:  
#                 i = start - 1 # skip to index one element to the left of the matched region 
#                 continue 
#             count += 1
#             if pattern[i-1] != text[h-1]:
#                 break
#             i = i - 1
#             h = h - 1
#         # either match full pattern or mismatch in the string
#         if i == 0:
#             res.append(h)
#             k = k + m - shift[i]
#         else:
#             k += shift[i]
#         # calculate new start and stop pointers to skip comparisons
#         # subtract 1 for 0-index 
#         if shift[i] < m - i:
#             p = shift[i] + i
#             stop = p - 1
#             start = p - m + i 
#         elif shift[i] == m - i:
#             stop = m - shift[i] - 1
#             start = 0
#     print("boyer moore comparisons:",count)
#     return res 

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
    print("boyer moore comparisons:",count)
    return res


# print("boyer moore:",boyer_moore('0011010101111001001101100','010'))
# print("test1",boyer_moore("10101010","1010"))
# print("test2",boyer_moore("000000000","111"))
# print("test3",boyer_moore("010101","010101"))
# print("test4",boyer_moore("01","010"))
# print("test5",boyer_moore("0101010101","0"))

# print("naive:",naive_pattern_match('0011010101111001001101100','010'))








