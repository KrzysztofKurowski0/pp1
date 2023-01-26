cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

def f(d):
    isin = []
    for i in range (len(d)):
        if d[i][1] == "in":
            isin.append(d[i][0])
        else:
            isin.remove(d[i][0])

    return sorted(isin)

