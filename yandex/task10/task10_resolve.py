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


def revers(word):
    r = []
    index = len(word)
    while index > 0:
        r.append(word[index])
    return "".join(r)


def revers_words(s):
    a = s.split(" ")  # "abc  cde" => [['abc']['']['cde']] ==> revers() ==> join(" ")
    result = []
    for word in a[:-1]:
        result.append(revers(word))

    return result

    return " ".join(result)


def revers2_word(s):
    i = 0
    result = ""
    word = ""
    for i in len(s):
        if i == " ":
            result += revers(word)
            result += " "
            word = ""
            continue

        word += s[i]
    else:
        result += revers(word)



