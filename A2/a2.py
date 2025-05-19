# Name: Douh Ee Leu
# Student ID: 31841716

# Code structure taken from Week 4 lecture notes by Taylor Kearney, implemented by Douh Ee Leu
def naive_implicit_suffix_tree(text):
    n = len(text)
    suffix_tree = {}

    # Construct I_1           
    suffix_tree[(0, 0)] = {"leaf" : 0}  # each text file contains at least one character (no need to check n > 0)

    for i in range(1, n):               # 1 as I1 already constructed
        # begin phase i+1
        for j in range(i+1):             
            substring_exist = False     # flag to check if substring of suffix already exist for extension decision

            for (start_index, end_index) in suffix_tree:                        # (start index of text, end index of text) tuple contains pointers to the original text string
                if text[start_index : end_index + 1] == text[j : i + 1]:        # check if there is an existing path for the substring in the suffix tree
                    substring_exist = True
                    break

            if substring_exist == False:                                        # rule 2 extension 
                suffix_tree[(j, i)] = {"leaf": j}

    return suffix_tree

# Logic not implemented, returns a sample result for correct output format 
def dl_search(suffix_trees, pattern_list):
    # sample result - returns a list of tuples, each tuple is a DL>= 1 successful search
    return [(2,1,3,1)]

import sys

# this function reads a file and returns a list of text file names and a list of pattern file names
def read_config_file(file_path: str) -> str:
    f = open(file_path, 'r')
    
    # convert first line in N and M values (for loop)
    n_m_list = f.readline().strip().split()  # remove spaces and line breaks and split into ["N","M"]
    n = int(n_m_list[0])
    m = int(n_m_list[1])

    # resulting lists
    txt_list = []
    pat_list = []

    # using tuple to represent (text/pattern number, text/pattern file name)
    for _ in range(n):
        txt_file = f.readline().strip().split()
        txt_list.append((int(txt_file[0]), txt_file[1])) # convert into tuple and append to text list

    for _ in range(m):
        pat_file = f.readline().strip().split()
        pat_list.append((int(pat_file[0]), pat_file[1])) # convert into tuple and append to pattern list
    
    f.close()

    return txt_list, pat_list

# this function reads a file and returns its content as a single string
def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    res = f.read().strip()  # remove spaces and line breaks 
    f.close()

    return res

# this function writes the match results to the output file a2 (it assumes the format of res is a list of tuples (pat_num, txt_num, 0-indexed pos, dl-dist))
def write_output(res):
    output_file = 'output_a2.txt'
    f = open(output_file, 'w')

    # output to <pattern number> <text number> <position of occurrence> <DL-distance> format
    for tuples in res:
        f.write(str(tuples[0]) + ' ' + str(tuples[1]) + ' ' + str(tuples[2] + 1) + ' ' + str(tuples[3]) + '\n')  # convert pos occurence to 1-indexed

    f.close()

if __name__ == '__main__':
    # retrieve file paths from command line arguments
    _, filename= sys.argv
  
    txt_list, pat_list = read_config_file(filename)                 # separate run-configuration file into lists of text and pattern files respectively

    n_suffix_tree = {}                                              # all n of suffix trees constructed from n text files
    for (txt_num, txt_file_name) in txt_list:
        txt = read_file(txt_file_name)                              # read text string from file.txt
        suffix_tree = naive_implicit_suffix_tree(txt)               # suffix tree constructed from txt file
        n_suffix_tree[txt_num] = suffix_tree                        # add to suffix tree collection using dictionary

    dl_list = dl_search(n_suffix_tree, pat_list)                    # search every text suffix tree for each pattern

    write_output(dl_list)                                           # write to output file in output format