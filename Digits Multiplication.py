def checkio (number):
    sum = 1
    for i in str(number):
        print "i is "+ i
        n = int(i)
        print "n is " + str(n)
        if not n:
            print "n is in if " + str(n)
            continue

        sum*=n
        print sum
    return sum



print checkio(123405)


