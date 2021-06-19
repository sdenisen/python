def converToFloat(line):
    # example: "0.000003 0.000012 0.000081 0.000099 0.000076 0.000045 0.000092 0.000068 0.000047 "
    # example: "0.000002 0.000045 -0.000063 -0.000009 -0.000050 0.000048 0.000070 -0.000037 0.000056 -0.000008 "
    arr = line.strip().split(" ")
    result = []
    for float_str in arr:
        result.append(float(float_str))
    return result


def getIndexesOfDiffs(metabolites, adducts):
    r = {}
    for m_dx, metabl in enumerate(metabolites):
        for a_dx, adduct in enumerate(adducts):
            sum_m_a = round(metabl + adduct, 6)
            if sum_m_a < 0:
                continue
            r[(m_dx+1, a_dx+1)] = sum_m_a
    return r


def getMinimumDeltaOfSignal(keylist, signal):
    min_delta = None
    result = 0
    for key in keylist:
        abs_signals = abs(signal - key)
        if min_delta is None or abs_signals < min_delta:
            min_delta = abs_signals
            result = key
        else:
            break
    return result


def calculate():
    with open("3.txt", "r") as f:
        count_test_cases = int(f.readline().strip())
        result_keys = []
        for i in range(count_test_cases):
            counters_m_k_n = f.readline().strip().split(" ")

            count_masses_of_metabolites = int(counters_m_k_n[0])
            count_masses_of_adducts = int(counters_m_k_n[1])
            count_masses_of_signals = int(counters_m_k_n[2])

            metabolites = converToFloat(f.readline().strip())
            adducts = converToFloat(f.readline().strip())
            signals = converToFloat(f.readline().strip())

            indexes_diffs = getIndexesOfDiffs(metabolites, adducts)
            res = {val: key for key, val in indexes_diffs.items()}  # here we remove duplicates;

            if count_masses_of_metabolites != len(metabolites) or count_masses_of_adducts != len(
                    adducts) or count_masses_of_signals != len(signals):
                raise Exception(" some error")

            print("start calculate")
            key_list = sorted(res.keys())
            for signal in signals:
                result_keys.append( getMinimumDeltaOfSignal(key_list, signal) )

            s = open(f"output-3-optimize.6.{i}.txt", "w")
            for key in result_keys:
                r = res[key]
                m_index = str(r[0])
                a_idnex = str(r[1])
                s.write(" ".join([m_index, a_idnex]) + "\n")
            s.close()


def main():
    calculate()


if __name__ == "__main__":
    main()
