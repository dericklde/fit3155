# Name: Douh Ee Leu
# Student ID: 31841716

# Z-array algorithm implemented using code from https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/tutorial/

# Algorithm to construct Z array 
def z_array(text):
    n = len(text)
    Z = [0] * n # each element contains longest substring starting at i that matches prefix
    L, R = 0, 0 

    for i in range(1, n):
        if i > R: # not within Z box so do a new match from beginning
            L,R = i,i
            while R < n and text[R] == text[R - L]: # difference between R and L will give us prefix of text!
                R += 1
            Z[i] = R - L 
            R -= 1  # R goes one past last matching index so have to move it back by 1
        else: # i <= R
            k = i - L
            m = R - i + 1 # use to check whether the current element will go outside of Z box
            if Z[k] < m: 
                Z[i] = Z[k]
            else: # Z[k] >= m - goes over Z box case
                L = i
                while R < n and text[R] == text[R - L]: # continue matching pass R
                    R += 1
                Z[i] = R - L 
                R -= 1  # R goes one past last matching index so have to move it back by 1
    
    return Z

# Z algorithm altered for near-exact pattern matching under DL-distance <= 1
def z_algo(text, pattern):
    n = len(text)
    m = len(pattern)

    # early exit conditions: empty pattern or empty text or pattern longer than text
    if pattern == "" or text == "" or m > n:
        return []

    # forward Z array construction
    prefix_check = pattern + "$" + text
    z1 = z_array(prefix_check)
    
    # reversed Z array construction
    suffix_p = pattern[::-1]    # reverse pattern
    suffix_t = text[::-1]       # reverse text
    suffix_check = suffix_p + "$" + suffix_t
    z2 = z_array(suffix_check)
    
    # exact match case
    exact_match = []

    # go through Z array to find match (length m)
    for i in range(len(z1)):
        if (z1[i] == m):
            exact_match.append(i-m-1) # subtract m+1 to account for pattern and '$'
    
    # near exact match cases
    # replace char case
    replace_char = []
    
    for i in range(n - m + 1):  # m sized "box" over the text
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 1]  # index of the last element of "box" in the forward match

        if prefix_len + suffix_len == (m - 1):  # there will be m - 1 matched characters
            replace_char.append(i)
    

    # insert char case
    insert_char = []

    for i in range(n - m + 2):  # m-1 sized "box" over the text
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 2] # index of the last element of "box" in the forward match

        # must also include m matched chars besides m-1 since Z array algorithm will match for entire pattern
        if m - 1 <= prefix_len + suffix_len <= m:
            insert_char.append(i)
    

    # delete char case
    delete_char = []

    for i in range(n - m):  # m+1 sized "box" over the text
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i]  # index of the last element of "box" in the forward match

        if prefix_len + suffix_len == m: # # there will be m + 1 matched characters to delete one char
            delete_char.append(i)
    
    # swap char case
    swap_char = []
    
    for i in range(n - m + 1):  # m sized "box" over the text
        prefix_len = z1[i + m + 1]
        suffix_len = z2[n - i + 1]

        if prefix_len + suffix_len == m - 2:    # there are two mismatched chars (to be swapped)
            # to be swapped char in first half of the substring
            if prefix_len < suffix_len:
                # check successive chars in first half with their opposite positions in the pattern 
                if prefix_check[i + m + 1 + prefix_len] == pattern[prefix_len + 1] and prefix_check[i + m + 2 + prefix_len] == pattern[prefix_len]:
                    swap_char.append(i)
            # to be swapped char in later half of the substring
            elif prefix_len > suffix_len:
                # check successive chars in later half with their opposite positions in the pattern 
                if suffix_check[n - i + 2 + suffix_len] == pattern[m-1-suffix_len] and suffix_check[n - i + 1 + suffix_len] == pattern[m-1-suffix_len-1]:
                    swap_char.append(i)
            # to be swapped char right down in the middle of the substring
            elif prefix_len == suffix_len:
                # check one char in first half and one char in later half (successive) their opposite positions in the pattern 
                if prefix_check[i + m + 1 + prefix_len] == pattern[m-1-suffix_len] and suffix_check[n - i + 1 + suffix_len] == pattern[prefix_len]:
                    swap_char.append(i)
            else:
                # false positive detected
                continue

    # collating results
    list_of_near_exacts = [replace_char,swap_char,insert_char,delete_char]
    res = [None] * n

    # make exact match case 0
    for index in exact_match:
        res[index] = 0
    
    # make all near match cases 1
    for lst in list_of_near_exacts:
        for index in lst:
            if res[index] != 0: # to make sure we don't replace exact match case
                res[index] = 1

    return res

import sys

# this function reads a file and returns its content as a single string
def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    res = f.read().strip()  # remove spaces and line breaks 
    f.close()
    return res

# this function writes the match results to the output file a1q1
def write_output(res):
    output_file = 'output_a1q1.txt'
    f = open(output_file, 'w')
    for i in range(len(res)):
        if res[i] != None:
            f.write(str((i + 1)) + ' ' + str(res[i]) + '\n')  # convert to 1-indexed
    f.close()

if __name__ == '__main__':
    # retrieve file paths from command line arguments
    _, filename1, filename2 = sys.argv

    text = read_file(filename1)
    pattern = read_file(filename2)

    res = z_algo(text, pattern)
    write_output(res)




