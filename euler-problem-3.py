__author__ = 'sdenisenko'

target_number = 600851475143


def isNatural(item, naturals):
    for nat_number in naturals:
        if not item % nat_number:
            break
    else:
        return True
    return False

def getNaturals(n):
    naturals = []
    for i in range(2, n):
        if isNatural(i, naturals):
            naturals.append(i)
    naturals.insert(0, 1)
    return naturals

def getNaturals(start, stop, naturals):
    for i in range(start, stop):
        if isNatural(i, naturals):
            naturals.append(i)
    return naturals


def checkTargetNumber(target_number):
    naturals = []
    result = []
    last = 0
    i = 2
    iteration = 1000
    naturals = getNaturals(2, iteration, naturals)
    while (True):
        if i >= iteration:
            next_step = iteration + 1000
            naturals = getNaturals(iteration, next_step, naturals)
            iteration = next_step
        result = [i for i in naturals if not target_number % i]
        if last !=result[-1:][0]:
            print result[-1:]
            last = result[-1:][0]

        if i >= target_number:
            break
        i += 1000
    return naturals


#print getNaturals(102)
print checkTargetNumber(target_number)