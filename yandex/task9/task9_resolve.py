"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, 
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""


def make_interval(start, end, is_not_end):
    result_intervals = ""
    if not end:
        result_intervals += f"{start}"
    else:
        result_intervals += f"{start}-{end}"
    if is_not_end:
        result_intervals += ","
    return result_intervals


def compress(input_array):
    if not input_array:
        return ""
    sorted_array = sorted(input_array)
    result_intervals = ""

    while sorted_array:
        start = sorted_array.pop(0)
        end = None
        index = 1
        while sorted_array:
            expected_end = sorted_array[0]
            if (expected_end - index) == start:
                index += 1
                end = expected_end
                sorted_array.pop(0)
                continue
            break

        result_intervals += make_interval(start, end, len(sorted_array))

    return result_intervals
