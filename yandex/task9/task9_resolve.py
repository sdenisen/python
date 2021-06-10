"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, 
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""


def compress(l):
    if not l:
        return ""
    l = sorted(l)
    result_intervals = ""

    index = 0
    while True:
        start_interval = l[index]
        end_interval = start_interval
        for j in range(index + 1, len(l) - 1):
            if end_interval + 1 == l[j]:
                end_interval = l[j]
            index = j
            break

        if end_interval == start_interval:
            result_intervals += f"{start_interval}"
            index += 1
        else:
            result_intervals += f"{start_interval}-{end_interval}"

        if index != len(l):
            result_intervals += ","
        else:
            break

    return result_intervals

