def z_array(text):
    n = len(text)
    Z = [0] * n # contains longest substring starting at i that matches prefix
    L, R = 0, 0

    for i in range(1, n):
        if i > R:
            L,R = i,i
            while R < n and text[R] == text[R - L]: 
                R += 1
            Z[i] = R - L 
            R -= 1  # R goes one past last matching index
        else: # i <= R
            k = i - L
            m = R - i + 1
            if Z[k] < m: 
                Z[i] = Z[k]
            else: # Z[k] >= m
                L = i
                while R < n and text[R] == text[R - L]:
                    R += 1
                Z[i] = R - L 
                R -= 1  # R goes one past last matching index
    
    return Z

def z_algo(pattern, text):
    n = len(text)
    m = len(pattern)

    # early exit conditions: empty pattern or empty text or pattern longer than text
    if pattern == "" or text == "" or m > n:
        return []

    prefix_check = pattern + "$" + text
    z1 = z_array(prefix_check)
    
    suffix_p = pattern[::-1]
    suffix_t = text[::-1]
    suffix_check = suffix_p + "$" + suffix_t
    z2 = z_array(suffix_check)
    
    # exact match
    # print("z1: ",z1)
    exact_match = []

    for i in range(len(z1)):
        if (z1[i] == m):
            exact_match.append(i-m-1) # subtract pattern and '$' from z array
    
    # print(exact_match)

    # near exact match cases
    replace_char = []
    
    for i in range(n - m + 1):
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 1]

        if prefix_len + suffix_len == (m - 1):
            # print("i = ", i, "pref = ", prefix_len)
            # print("i = ", i, "suff = ", suffix_len)
            replace_char.append(i)
    
    # print(replace_char)

    insert_char = []

    for i in range(n - m + 2):
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 2]
        # print("i", i, "char",suffix_check[n - i + 2])
        # print("i", i, "pref", prefix_len, "suff", suffix_len)  # debugging purpose pls delete when done
        if m - 1 <= prefix_len + suffix_len <= m:
            # print("i = ", i, "pref = ", prefix_len)
            # print("i = ", i, "suff = ", suffix_len)
            insert_char.append(i)
    
    # print(insert_char)

    delete_char = []

    for i in range(n - m):
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i]

        if prefix_len + suffix_len == m: 
            # print("i = ", i, "pref = ", prefix_len)
            # print("i = ", i, "suff = ", suffix_len)
            delete_char.append(i)
    
    # print(delete_char)

    # print("z1: ",z1)
    # print("z2: ",z2)
    swap_char = []
    
    for i in range(n - m + 1):
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 1]

        if prefix_len + suffix_len == m - 2:
            # print("i = ", i, "pref = ", prefix_len)
            # print("i = ", i, "suff = ", suffix_len)
            if prefix_len < suffix_len:
                # print("left case", prefix_check[i + m + 1 + prefix_len], prefix_check[i + m + 2 + prefix_len])
                # print("pattern: ", pattern[prefix_len], pattern[prefix_len + 1])
                if prefix_check[i + m + 1 + prefix_len] == pattern[prefix_len + 1] and prefix_check[i + m + 2 + prefix_len] == pattern[prefix_len]:
                    swap_char.append(i)
            elif prefix_len > suffix_len:
                # print("right case", suffix_check[n - i + 2 + suffix_len], suffix_check[n - i + 1 + suffix_len])
                # print("pattern: ", pattern[m-1-suffix_len-1], pattern[m-1-suffix_len])
                if suffix_check[n - i + 2 + suffix_len] == pattern[m-1-suffix_len] and suffix_check[n - i + 1 + suffix_len] == pattern[m-1-suffix_len-1]:
                    swap_char.append(i)
            elif prefix_len == suffix_len:
                # print("middle case", prefix_check[i + m + 1 + prefix_len], suffix_check[n - i + 1 + suffix_len])
                # print("pattern: ", pattern[prefix_len], pattern[m-1-suffix_len])
                if prefix_check[i + m + 1 + prefix_len] == pattern[m-1-suffix_len] and suffix_check[n - i + 1 + suffix_len] == pattern[prefix_len]:
                    swap_char.append(i)
            else:
                # print("false positive")
                continue
    
    # print(swap_char)

    # collating results
    # print("replace_char:", replace_char)
    # print("swap_char:", swap_char)
    # print("insert_char:", insert_char)
    # print("delete_char:", delete_char)
    # print("exact match:", exact_match)
    # print("z array:", z1)
    list_of_near_exacts = [replace_char,swap_char,insert_char,delete_char]
    res = [None] * n

    for index in exact_match:
        res[index] = 0
    
    for lst in list_of_near_exacts:
        for index in lst:
            if res[index] != 0:
                res[index] = 1

    for i in range(len(res)):
        if res[i] != None:
            print(i+1, res[i])

    return res


print(z_algo("", ""))
#     # abcd # bacd acbd abdc dbca - forward
#     # dcba # acbd cdba dbca dcab - reverse


