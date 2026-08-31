def nump(x):
    '''Finding the prime numbers in the given range
    of numbers'''


    if x == 2:
        res = [2]

    elif x == 3:
        res = [2, 3]

    else:
        numb = list(range(2, x + 1))

        ln = len(numb)
        # print(f"The list of all integer numbers: {numb}")

        res = []
        nres = []

        dv1 = numb[::-1]
        dv2 = numb[ln - 2::-1]

        for i in range(len(dv1)):
            for j in range(i, len(dv2)):

                count = dv1[i] % dv2[j]

                if count == 0:
                    nres.append(dv1[i])
                    break

        for item in dv1[:]:
            if item in nres:
                dv1.remove(item)
                res = dv1.copy()

        res = res[::-1]
        print(f"Prime numbers -- {res}")
    return res