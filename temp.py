rdl = list(map(int,input().split()))
n, m = rdl
for i in range(n):
        rdl = input()
        cur = []
        for k in range(m):
            if int(rdl[k]) == 1:
                cur.append(-1)
            else:
                cur.append(int(rdl[k]))
        lab.append(cur)