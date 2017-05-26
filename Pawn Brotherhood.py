def safe_pawns(pawns):
    pawns_indexes = set()
    for p in pawns:
        # print p
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        # print p[1]
        # print ord(p[0])
        # print str(row) + " print row(p[1]) - 1"
        # print str(col) + " print ord(p[0]) - 97"
        pawns_indexes.add((row, col))
        # print pawns_indexes

        count = 0
        for row, col in pawns_indexes:
            is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
            if is_safe:
                count += 1
    # print pawns_indexes
    return count
    print count


print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})

