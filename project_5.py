def minCoins(coinList, total):
    table = [0 for i in range (0, total + 1)] #makes optimal table
    table[0] = 0 # base case
    for i in range (1, total + 1): # finds all variations  
        table[i] = total #
        for j in range(0, len(coinList)): # looks at each coin 
            if (coinList[j] <= i): #if coin is smaller then amount take coin value away from amount
                table[i] = min(table[i], table[i - coinList[j]] + 1) # get min of the two
                
    return table[total] # return the minimum coin 

#online question
def intelligentGirl(userInput):
    table = [0] * len(userInput) # makes new array to count even
    counter = 0 
    for i in range (len(userInput)): # finds even number at i in the string
        if int(userInput[i]) % 2 == 0: # converts string to int and sees if even
            counter = table[i - 1] + 1
        table [i] = counter # adds result to array
    for j in table: # prints out array with spaces
        print(j, end = " ")
    
            
