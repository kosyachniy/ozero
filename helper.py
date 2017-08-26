def inch(x):
    return x[0]

list = [(1,0), (2,0), (3,0)]
L = map(inch, list)
print(L)
for i in map(lambda x: x[0], list):
    print(i)
