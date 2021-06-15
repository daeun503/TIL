arr = [2, 3, 4, 54, 5, 1, 0, 334,2 , 5553]

def merge(L, R):
    result = []
    Lp, Rp = 0, 0
    while Lp < len(L) and Rp < len(R):
        if L[Lp] < R[Rp]:
            result.append(L[Lp])
            Lp += 1
        else:
            result.append(R[Rp])
            Rp += 1
    while Lp < len(L):
        result.append(L[Lp])
        Lp += 1
    while Rp < len(R):
        result.append(R[Rp])
        Rp += 1
    return result




def divide(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    L = divide(arr[:mid])
    R = divide(arr[mid:])
    return merge(L, R)


print(divide(arr))