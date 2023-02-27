a = 0
b = 1
N = int(input())
for i in range(N):
    print(a, end="")
    if i < N-1:
        print('\n', end="")
    Nth = a + b
    a = b
    b = Nth