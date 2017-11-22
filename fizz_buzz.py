def checkio(number):
    number = int(number)
    if 0 < number <= 1000:
        if number % 3 == 0 and number % 5 == 0:
            print "Fizz Buzz"
        elif number % 3 == 0:
            print "Fizz"
        elif number %5 == 0:
            print "Buzz"
        else:
            return str(number)
            print str(number)

print checkio(101)