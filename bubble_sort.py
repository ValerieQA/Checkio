def bubble_sort(li):
    # li = [5, 2, 7, 4, 0, 9, 8, 6]
    n = 1
    while n < len(li):
        print str(len(li)) + " len"
        for i in range(len(li) - n):
            print str(i) + " - it is i"
            print str(li) + "- list"
            if li[i] > li[i + 1]:
                # print li[i]
                # print li[i + 1]
                li[i], li[i + 1] = li[i + 1], li[i]
                # print li[i]
                # print li[i + 1]
        n += 1
        print n
    return li
print bubble_sort([5,2,7,4,0,9,8,6])



