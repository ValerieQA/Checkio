print max(2.2, 5.6, 5.9, key=int)
print min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
lis = ['1','100','111','2', '99', '66', '68']
print max(lis, key=lambda x:str(x))
print str(5)<str({})
print min("hello") == "e"
print max(2.2, 5.6, 5.9, key=int)



import functools
def abstract(*args, **kwargs):
    compare = kwargs.get('compare', lambda x, y: x > y)
    key = kwargs.get('key', lambda x: x)
    values = iter(args[0]) if len(args) == 1 else iter(args)
    result = next(values)
    for i in values:
        if compare(key(i), key(result)):
            result = i
    return result


max = functools.partial(abstract, compare=lambda x, y: x > y)
min = functools.partial(abstract, compare=lambda x, y: x < y)
print abstract(max(3, 2) == 3, "Simple case max")