def convert_to_float(line):
    # example: "0.000003 0.000012 0.000081 0.000099 0.000076 0.000045 0.000092 0.000068 0.000047 "
    # example: "0.000002 0.000045 -0.000063 -0.000009 -0.000050 0.000048 0.000070 -0.000037 0.000056 -0.000008 "
    arr = line.strip().split(" ")
    result = []
    for float_str in arr:
        result.append(float(float_str))
    return result
