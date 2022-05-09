def dernierrech(T, e):
    for i in range(len(T)-1, -1, -1):
        if T[i] == e:
            return i
    return None

def premrech(T, e):
    for i in range(len(T)):
        if T[i] == e:
            return i
    return None