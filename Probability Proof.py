import secrets
i = 0
ii = 0
iii = 0
iv = 0
v = 0
vi = 0

for z in range(100000):
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 7)

    if result == 1:
        i = i + 1
    elif result == 2:
        ii = ii + 1
    elif result == 3:
        iii = iii + 1
    elif result == 4:
        iv = iv + 1
    elif result == 5:
        v = v + 1
    elif result == 6:
        vi = vi + 1


print("1 =",i,"\n2 =", ii, "\n3 =", iii, "\n4 =", iv, "\n5 =", v, "\n6 =", vi)
