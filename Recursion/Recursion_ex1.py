


def factorial_calc(num : int ) -> int :
    if num == 1 or num == 0  :
        return 1

    return num * factorial_calc(num - 1)




if __name__=='__main__':
    num = input("Insert the number that you want to calcuate its factorial : ")
    res = factorial_calc(int(num))
    print(res)