"""
Epigenomic Marks 2
While having a constant nucleotide sequence, DNA molecules in a cell can be chemically modified in several different ways. For example, the DNA bases can be methylated, or histone proteins, around which DNA is wrapped, can be supplied with chemical tags such as acetylation. It is thought that such modifications (or epigenomic marks) define cell specialization or a cell state when a specific combination of marks regulates how genes are expressed.

In this problem, you are given genomic tracks describing the presence or absence of several epigenomic marks. Your task is to split the genomic positions into the smallest number of states so that each state corresponds to a particular combination of marks.

Input format
The first line of the input contains tt — the number of tests.

Each test consists of multiple lines. The first line contains two integers nn and ll — the number of sequences and their length. The remaining nn lines in the test include sequences of 00 and 11, describing the epigenomic marks. All sequences have the same length ll.

Output format
Your output file should contain 2t2t lines with two lines per test. The first line of the answer on a test should contain the minimal number of used states ss to distinguish all combinations of marks. The second line should contain ll numbers separated by spaces — the states per each position, encoded as numbers from 1 to ss.

"""


def convertTolistDNA(lines, len):
    result = []
    for i in range(len):
        r = ""
        for line in lines:
            r += line[i]
        result.append(r)
    return result


def subDNAresult(dna_array):
    r = {}
    count = 1
    result = []
    for dna in dna_array:
        if dna not in r.keys():
            r[dna] = count
            count += 1
        result.append(str(r[dna]))

    return (str(count-1), " ".join(result))


s = open("output.txt", "w")
with open("2.txt", "r") as f:
    count_lines = int(f.readline().strip())

    for i in range(count_lines):
        str_line = f.readline().strip().split(" ")

        next_lines = int(str_line[0])
        count_dna = int(str_line[1])
        lines = []
        for line in range(next_lines):
            lines.append(f.readline().strip())
        arr_dna = convertTolistDNA(lines, count_dna)
        result = subDNAresult(arr_dna)
        s.write(result[0] + "\n")
        s.write(result[1] + "\n")

s.close()
