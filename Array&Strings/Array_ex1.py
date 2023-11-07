

def inPlace_rev_func(text : str) -> str :
    print(text[::-1])




def rev_func(text : str) -> str:
    size = len(text) -1 
    s1 = ''
    while size >= 0 :
        s1 = s1 + text[size]
        size = size - 1 

    #for i in text:
    #    s1 = i + s1
    #print(s1)

    print(s1)



def main():
    #tests
    text = input("Please enter the text that you want to reverse : ")
    inPlace_rev_func(text)
    rev_func(text)


if __name__ == "__main__":
    main()