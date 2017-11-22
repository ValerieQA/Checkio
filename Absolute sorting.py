def checkio(data):
    return sorted(data, key = abs)

print checkio((-20, -5, 10, 15))
