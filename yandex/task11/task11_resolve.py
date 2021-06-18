"""
Example: Finding a Motif in DNA
Given two strings ss and tt, tt is a substring of ss if tt is contained as a contiguous collection of symbols in contiguous collection of symbols in ss (as a result, tt must be no longer than ss).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position ii of ss is denoted by s[i]s[i].

A substring of ss can be represented as s[j:k]s[j:k], where jj and kk represent the starting and ending positions of the substring in ss; for example, if ss = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]s[2:5] = "UGCU".

The location of a substring s[j:k]s[j:k] is its beginning position jj; note that tt will have multiple locations in ss if it occurs more than once as a substring of ss (see the Sample below).

Download the test from https://stepik.org/media/attachments/lesson/60794/test-B.zip.

You have to upload the answer to the provided test, not the source code!

Input format
The first line of the input contains the number of tests. Each test is described by two lines: the first line contains ss and the second line contains tt. Lengths of the strings do not exceed 1 kb.

Output format
For each test output on a separate line all locations of tt as a substring of ss in any order.

The indexing in this problem starts from 1!

Scoring
This is a non-scoring problem and you will get 0 points for solving it.
"""

def findPattern(pattern, string):
    result = []
    for idx, c in enumerate(string):
        is_substring = string.startswith(pattern, idx, max(idx + len(pattern), len(string)))
        if is_substring:
            result.append(str(idx + 1))
    return " ".join(result)


s = open("output.txt", "w")
with open("input 2.txt", "r") as f:
    count_lines = int(f.readline())
    for i in range(count_lines):
        str_line = str(f.readline())
        pattern = str(f.readline().strip())
        r = findPattern(pattern, str_line)
        s.write(r + "\n")

s.close()
