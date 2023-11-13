


def isEven(n):
 
    # n&1 is 1, then odd, else even
    return (not(n & 1))
 
 

if __name__ == "__main__":
 
    n = input("Insert the number you want to check : ")
    if isEven(int(n)):
        print("Even")
    else:
        print("Odd")
 