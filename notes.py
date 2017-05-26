def checkio(array):
    new_array = []
    for i in range(len(array)):
        if i % 2 == 0:
            new_array.append([i])
            i+=1
        print new_array
    return new_array
    for i in new_array:
        if type(i) == int:
            i+=1
            print "gfgf"
    f = (new_array)*array[-1]
    print f
    return f


print checkio([1, 3, 5])
print checkio([0, 1, 2, 3, 4, 5])