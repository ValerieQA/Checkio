from nose.tools import assert_equals


def remainder(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return "dividing by zero is impossible"
    c = int(a / b)
    rem = a - b * c
    assert_equals(rem, (a % b))
    return rem


print remainder(1, 0)
print remainder(0, 5)
print remainder(-1, 5)
print remainder(1, 5)
print remainder(14, 5)
