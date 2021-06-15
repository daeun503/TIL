def solution(arr1, arr2):
    b = []
    for i in range(len(arr1)):
        a = []
        for k in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr2)):
                tmp += arr1[i][j] * arr2[j][k]
            a.append(tmp)
        b.append(a)
    return b