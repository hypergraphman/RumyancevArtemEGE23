def f(s, c, m):
    if s > 80:
        return c % 2 != m % 2
    if s >= 77:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(s + 1, c + 1, m),
             f(s * 2, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 77):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)
            break