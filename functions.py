def numClassify(inpt):
    try:    #even number 
        n = int(inpt) # the int function converts input to number if valid 
        if(n%2 == 0): #if remainder is 0 when divided by 2
            print("hello",n,"is a even number")
        #odd number 
        elif(n%2 != 0):
            print("hello",n,"is a odd number") #if remainder is not 0 when divided by 2
    except TypeError:
        print("Please Enter Numbers Only")
    except Exception as e:
        print("An exception has been received please check! --->",e)

inp = input("Enter any Number: ")
#numClassify(inp) # when we run this as - input function converts numbers to strings
numClassify(inp) 

    