"""
Find the longest substring without repeating characters

Solution Approach
-----------------
Use a hashmap (character as the key, index as value) and two pointers, iterate over the string.
if the current character is in the hashmap, shift the left pointer i, compute the length
and add the character to the hashmap, finally return the length
"""

def longest_substring(string: str) -> int:
    """
    return the length of maxsubstring without repeating character
    Parameters
    ----------
    string: input string

    Returns
    -------
    max_len: max length of substring without repeating character
    """
    if not string:
        return 0
    max_len = 0
    i = 0 # first pointer pointer
    ch_map = {}
    for j in range(len(string)): # j is the second pointer
        if string[j] in ch_map:
            # if the character was already there 
            # shift the i pointer to max index of the occured character
            i = max(i, ch_map[string[j]])
        
        # update the max len by comparing the current substring
        max_len = max(max_len, j - i + 1)
    return max_len
