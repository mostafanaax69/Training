


def areBracketsBalanced(expr : str) -> bool :
    stack = []

    for char in expr :
        #case 1 : opening bracket 
        if char in ["(" , "[" , "{"]:
            stack.append(char)

        # case 2 the char should be closing brackets which means that the stack shouldnt be empty !
        else : 
            if len(stack) == 0 :
                return False
            

            temp = stack.pop()
            if char == ')' and temp != '(' : return False
            if char == '}' and temp != '{' : return False
            if char == ']' and temp != '[' : return False

    
    return (len(stack) == 0) ## if len is 0 then true else false












if __name__ == "__main__":

    #testexpr = "{()}[]"

    expr = input("Type the string that you want to check : ")
 
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")