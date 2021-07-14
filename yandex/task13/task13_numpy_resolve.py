import numpy as np


def converToFloat(line):
    # example: "0.000003 0.000012 0.000081 0.000099 0.000076 0.000045 0.000092 0.000068 0.000047 "
    # example: "0.000002 0.000045 -0.000063 -0.000009 -0.000050 0.000048 0.000070 -0.000037 0.000056 -0.000008 "
    arr = line.strip().split(" ")
    result = []
    for float_str in arr:
        result.append(float(float_str))
    return result

output_data = []
def calculate():
    with open("4.txt", "r") as f:
        count_test_cases = int(f.readline().strip())
        result_keys = []
        for i in range(count_test_cases):
            counters_m_k_n = f.readline().strip().split(" ")
            count_masses_of_metabolites = int(counters_m_k_n[0])
            count_masses_of_adducts = int(counters_m_k_n[1])
            count_masses_of_signals = int(counters_m_k_n[2])
            m = converToFloat(f.readline().strip())
            a = converToFloat(f.readline().strip())
            s = converToFloat(f.readline().strip())

            metabolites = np.repeat([m], len(a), 0)
            adducts = np.array(a)
            signals = np.array(s)

            r = (metabolites.T + adducts)
            r[r < 0] = 2000

            index = 0
            for signal in s:
                result_delta = signal - r
                abs_delta = np.absolute(result_delta)
                min_element = np.where(abs_delta == abs_delta.min())
                x, y = 0, 0
                if len(min_element[0]) == 2:
                    x, y = min_element[0][0], min_element[0][1]
                elif len(min_element[0]) == 1:
                    x, y = min_element[0], min_element[1]

                a_y = (y[0] if isinstance(y, np.ndarray) else y) + 1
                m_x = (x[0] if isinstance(x, np.ndarray) else x) + 1
                output_data.append((str(m_x), str(a_y)))

                if not index%100:
                    if index%5000:
                        print(index, end=" ")
                    else:
                        print(index,)

                index+=1

    s = open(f"output-4-optimize.numpy.txt", "w")
    for m_index, a_idnex in output_data:
        s.write(" ".join([m_index, a_idnex]) + "\n")
    s.close()


def main():
    calculate()


if __name__ == "__main__":
    main()
