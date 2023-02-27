B = int(input())
H = int(input())
for i in range(H):
    for j in range(B):
        print("*", end="")
    if i < H - 1:
        print()
        print("", end="")