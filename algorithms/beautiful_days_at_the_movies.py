
def beautifuldays(i, j, k):
    def isbeautiful(num):
        numstring = str(num)
        numreversed = ''
        for a in numstring[::-1]:
            numreversed += a
        numreversed = int(numreversed.lstrip('0'))
        print(numreversed)
        return numreversed
    print(f'i: {i}, j: {j}, k: {k}')
    numdays = 0
    for x in range(i, j+1):
        print(x)
        if abs(x-isbeautiful(x)) % k == 0:
            numdays += 1
    return numdays


beautifuldays(20, 23, 6)
