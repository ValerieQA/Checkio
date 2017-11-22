def sum10(a, b):
    if sum([a, b]) % 10 == 0:
        return True
    return False
print sum10(5, 9)



a = 8

i = 5 if a > 7 else 0

if a > 7:
   i = 5
else:
   i = 0