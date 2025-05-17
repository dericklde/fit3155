# Name: Douh Ee Leu
# Student ID: 31841716

# def naive_implicit_suffix_tree(str):
#     n = len(str)
#     # Construct I_1
#     for i in range(n):
#         # begin phase i+1
#         for j in range(i+1):
#             pass
#             # begin extension j
#             # Follow the path str[j...i] from the root in the current state of the implicit suffix tree.
#             # Apply the appropriate suffix extension rule.
#         # str[j...i+1] is now in the tree
#     # end of phase i+1 (I_{i+1} computed)

def dl_search():
    return [(2,1,3,1)]

import sys

# this function reads a file and returns a list of text file names and a list of pattern file names
def read_file(file_path: str) -> str:
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
  
    txt_list, pat_list = read_file(filename)

    # txt_suffix_tree = naive_implicit_suffix_tree(txt_list)

    dl_list = dl_search()

    write_output(dl_list)