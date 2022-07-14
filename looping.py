continueLoop = 'YES' #control variable
inpList = [] #input list

while (continueLoop == 'YES'):
    a = input("Enter any thing: ")
    inpList.append(a)    
    shouldContinue = input ("Do you Wish to Continue - enter Yes or No ")
    continueLoop = shouldContinue.upper()

print("you entered the following inputs: ")
for i in inpList:
    print(i)