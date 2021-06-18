"""
def revertДана строка (возможно, пустая), состоящая из букв A-Z и пробелов, разделяющих слова.
Нужно написать функцию, которая развернет слова.
И сгенерирует ошибку, если на вход пришла невалидная строка.
Примеры:
"QUICK FOX JUMPS"->"KCIUQ XOF SPMUJ"
"  QUICK FOX   JUMPS "->"  KCIUQ XOF   SPMUJ "
"  "->"  "
""->"

"""
import re

def revers(word):
    r = []
    index = len(word)-1
    while index >= 0:
        r.append(word[index])
        index -= 1

    return "".join(r)


def revers_words(s):

    if not s:
        return ""

    r = re.search(r"[A-Z]| ", s)
    if not r:
        raise Exception

    a = s.split(" ")  # "abc  cde" => [['abc']['']['cde']] ==> revers() ==> join(" ")
    result = []
    for word in a:
        result.append(revers(word))
    return " ".join(result)

