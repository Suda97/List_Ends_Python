def take(lis):
    b = len(lis)  # length of the list
    x = [lis[0], lis[b - 1]]
    return x


a = [5, 10, 15, 20, 25]
print(take(a))
