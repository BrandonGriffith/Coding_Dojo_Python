def maskify(cc):
    ccc = str(cc)
    mask = ""
    x = 0
    for i in ccc:
        z = len(ccc) - 4
        if x < z:
            mask = mask + '#'
        else:
            mask = mask + ccc[x]
        x = x + 1
    return mask


def maskify2(cc):
    return "#"*(len(str(cc))-4) + str(cc)[-4:]


print(maskify(12345678910))
print(maskify2(12345678910))
