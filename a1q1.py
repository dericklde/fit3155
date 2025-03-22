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

    prefix_check = pattern + "$" + text
    z1 = z_array(prefix_check)
    
    suffix_p = pattern[::-1]
    suffix_t = text[::-1]
    suffix_check = suffix_p + "$" + suffix_t
    z2 = z_array(suffix_check)
    
    near_match_indices = []

    # for i in range(n - m + 1):
    
    # res = []
    # for i in range(len(new_text)):
    #     if z[i] == len(pattern):
    #         res.append(i - (len(pattern)+1)) # +1 for delimiter "$"
    
    # return res
print(z_algo("abcd", "xbcdaxcdabxdabcx"))
