li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li, reverse=True)
print 'Sorted Variable:', s_li
li.sort()
print li

def bubble_sort(list):
    n = 1
    while n < len(list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        n += 1
    return list
print bubble_sort([5, 2, 7, 4, 0, 9, 8, 6, 1, -1])
