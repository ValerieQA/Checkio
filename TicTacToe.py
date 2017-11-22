# def checkio(data):
#     # Checking rows
#     i = 0
#     while i < 3:
#         line = data[i]
#         if (line == "XXX"): return "X"
#         if (line == "OOO"): return "O"
#         i += 1
#
#     # Checking collumns
#     j = 0
#     while j < 3:
#         column = data[0][j] + data[1][j] + data[2][j]
#         if (column == "XXX"): return "X"
#         if (column == "OOO"): return "O"
#         j += 1
#
#     # Checking diagonals
#     d1 = data[0][0] + data[1][1] + data[2][2]
#     d2 = data[2][0] + data[1][1] + data[0][2]
#     print("D1: " + d1 + " - D2: " + d2)
#     diagonals = [d1, d2]
#     k = 0
#     while k < 2:
#         diagonal = diagonals[k]
#         if (diagonal == "XXX"): return "X"
#         if (diagonal == "OOO"): return "O"
#         k += 1
#
#     return "D"


# def checkio(rows):
#     cols = [''.join([rows[y][x] for y in range(3)]) for x in range(3)]
#     digs = [''.join([rows[x][x] for x in range(3)]),
#             ''.join([rows[x][2 - x] for x in range(3)])]
#
#     triples = rows + cols + digs
#     for check in triples:
#         winner = x_or_o(check)
#         if winner: return winner
#     return 'D'
#
#
# def x_or_o(triple):
#     if triple.count('X') == 3:
#         return 'X'
#     elif triple.count('O') == 3:
#         return 'O'
#     else:
#         return 'D'




def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
