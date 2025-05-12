def traverse():
    pass
def makeExtension():
    pass
def resolveSuffixLinks():
    pass
def moveToNextExtension():
    pass

# Base Ukkonen's code structure taken from pseudocode in Week 4 lecture notes by Taylor Kearney
def ukkonen(str):
    # Append the terminal character
    str = str + '$'
    n = len(str)

    # Base case
    #construct I_1

    # Initialise variables , active node , remainder , last_j , globalEnd
    AN = root
    rem = None
    lastJ = 1
    globalEnd = 1

    for i in range(1, n):
        # Begin phase i+1 and perform rapid leaf extension
        globalEnd = globalEnd + 1
        # Explicit extensions start from lastJ+1
        for j in range(lastJ+1,i+2):
            # Skip-count down to the extension point
            traverse()
            # Apply the appropriate extension
            makeExtension()
            # Resolve any pending suffix links from the previous extension
            resolveSuffixLinks()
            # Move to next extension i.e. traversing suffix links , or showstopper
            moveToNextExtension()
        # str[j...i+1] is now in the tree
        # End of phase i+1 (I_{i+1} computed)
    
    # Return the tree 
    return root