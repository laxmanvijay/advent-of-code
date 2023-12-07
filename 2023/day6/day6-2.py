from functools import reduce

inputMap = [(35937366, 212206012011044)]

results = []

for g in inputMap:
    c = 0
    for i in range(0, g[0]+1):
        if i * (g[0] - i) > g[1]:
            c += 1
    results.append(c)

print(reduce(lambda a, b: a*b, results))