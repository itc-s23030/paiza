def f(N, S):
    return "\n".join([S] * (N))


N, S = int(input()), input()
result = f(N, S)
print(result)
