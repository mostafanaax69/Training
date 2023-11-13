
def permuations(word, l , r , res) :

    if( l == r ):
        res.append(list(word)) # new word append to our result list
    for i in range(l , r ):
        word[l] , word[i] = word[i] , word[l] # swap 
        permuations(word ,l+1 , r , res) # recursive
        word[l], word[i] = word[i], word[l]  # backtrack , changing to old word before swapping





if __name__=='__main__':

    #string = "ABC"
    num = input("Insert the string that you want to print all of its permuations : ")
    n = len(num) 
    a = list(num) # casting to list because 'str' object does not support item assignment
    res = []
    # Function call 
    permuations(a, 0, n , res ) 
    for b in res :
        print(''.join(b))


    













