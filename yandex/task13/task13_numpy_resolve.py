import numpy as np
from task13.common import convert_to_float


def calculate():
    with open("3.txt", "r") as f:
        count_test_cases = int(f.readline().strip())
        output_data = []
        for i in range(count_test_cases):
            count_m_a_s = convert_to_float(f.readline().strip())
            m = convert_to_float(f.readline().strip())
            a = convert_to_float(f.readline().strip())
            s = convert_to_float(f.readline().strip())

            metabolites = np.repeat([m], len(a), 0)
            adducts = np.array(a)

            r = (metabolites.T + adducts)
            r[r < 0] = 20000

            index = 0
            for signal in s:
                result_delta = signal - r
                abs_delta = np.absolute(result_delta)
                min_element = np.where(abs_delta == abs_delta.min())
                a_y = min_element[1][0] + 1
                m_x = min_element[0][0] + 1
                output_data.append((str(m_x), str(a_y)))

                if not index % 1000:
                    print(index, end=" " if index % 10000 else None)
                index += 1

    s = open(f"output-3-optimize.numpy.txt", "w")
    for m_index, a_idnex in output_data:
        s.write(" ".join([m_index, a_idnex]) + "\n")
    s.close()


def main():
    calculate()


if __name__ == "__main__":
    main()
