def count_up(n):
    for i in range(n):
        yield i


g = count_up(5)
print(next(g))
print(next(g))



