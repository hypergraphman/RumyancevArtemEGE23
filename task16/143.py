from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10_000:
        return n
    if n % 3 == 0:
        return n + f(n // 3)
    return 2 * n + f(n + 3)


for i in range(10000, 1, -1):
    try:
        f(i)
    except:
        pass
print(f(999) - f(46))
