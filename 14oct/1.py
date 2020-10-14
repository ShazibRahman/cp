def kangaroo(x1, v1, x2, v2):
    if (x1>x2 and v1>v2) or(x2>x1 and v2>v1)  :
        return 'NO'
    if v1>v2:
        while x1<x2:
            x1+=v1
            x2+=v2
        if x1==x2:
            return "YES"
    if v2> v1:
        while x2<x1:
            x1+=v1
            x2+=v2
        if x1==x2:
            return 'YES'
    return 'NO'
