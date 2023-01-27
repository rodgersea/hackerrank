

def circulararrayrotation(a, k, queries):
    # Write your code here
    rot = len(a) % k
    newarr = a[(len(a)-k):len(a)] + a[:len(a)-k]
    print(f'newarr: {newarr}')


m = [3, 4, 5]
n = 2
o = [1, 2]
circulararrayrotation(m, n, o)