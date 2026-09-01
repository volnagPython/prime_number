from functionPrimeNum1_g import nump


def ver_num(x):


    resp = ''
    if not x.isdigit():

        resp = "Ви ввели неправильний символ. Спробуйте ще раз!"
        return resp

    x = int(x)

    if x in nump(x):
        resp = f"Ведене число {x} - просте"
        return resp
    resp = f"Ведене число {x} - не просте"
    return resp

#Aug.31,2026

