def f(matrix):
    return "OK" if b >= 3 else "NG"


matrix = [(d, e) for [d, e] in [input().split() for _ in range(5)]]
a = list(d == e for d, e in matrix)
b = a.count(True)
result = f(matrix)
print(result)
