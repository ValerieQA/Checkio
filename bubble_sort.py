def bubble_sort(li):
    # li = [5, 2, 7, 4, 0, 9, 8, 6]
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li
print bubble_sort([5,2,7,4,0,9,8,6])

