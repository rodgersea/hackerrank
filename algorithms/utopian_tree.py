

def utopiantree(n):
    print(f'n: {n}')
    if n == 0:
        start = 1
    else:
        counter = 1
        start = 1
        for x in range(n):
            print(f'x: {x}, start: {start}, counter: {counter}')
            if counter == 1:
                start = start*2
                counter = 0
            else:
                start += 1
                counter = 1

    return start


utopiantree(1)
