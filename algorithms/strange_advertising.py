
def viraladvertising(n):
    import math

    shared = 5
    liked = 2
    cum = 2
    for x in range(n-1):
        shared = liked*3
        liked = math.floor(shared/2)
        cum += liked
        print(f'day: {x}, liked: {liked}, cum: {cum}')
    return cum

viraladvertising(5)
