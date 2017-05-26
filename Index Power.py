

def index_power(array, n):
   # print len(array)
   # print array[:-1]
    if n > int(len(array))-1:
        return -1
    elif 0 < len(array) <= 10 and 0 <= n:
        return array[n]**n





print index_power([1, 2, 3, 4], 7)
