#This is my paractice attempt to use my learning of python. In this project I have used a data set from Kaggle which has movie reviews.
#I have used my basic python skill to classify reviews - positive , negative or neurtal - based on few key words. This is not a foolproof system but a basic try 
#to manupulate data and use basic python data strucures like lists, dictionaries and loops.
# I have used some learning and help from online youtube videos for plotting the final graph
import pandas as pd
from matplotlib import pyplot as plt


reviews_input = pd.read_excel("C:\\Users\\path\\OneDrive\\Desktop\\Python\\reviews_test.xlsx") #importing excel sheet using Pandas
#print(type(reviews_input))

reviews_input.drop_duplicates() # remove potential duplicate reviews.
#print(len(reviews_input))

# Dictionary to validate sentiments in the reviews.

keyWords = {'positive':["good", "best", "amazing", "lovely", "wonderful", "great", "lovely"],'neutral':["ok", "not bad", "not great", "okay", "not bad","fine"],
'negative':["bad", "hate it", "stupid", "irritating","pathetic","poor","stink","poorly","boring" ]} 

#to store the result from review analysis
output = []
#print(reviews_input)



#if(any(e in test for e in tinp)):
    #print("yes")

for i,v in reviews_input.iterrows(): # looping thru data set
    for key, val in keyWords.items(): # checking each review witht the dictionary entires.
        if(any(k in v["Reviews"] for k in val)):
            if(key == 'positive'): 
                output.append('positive') #assigning the nature of review to a variable.
                break
            elif(key == 'negative'):
                output.append('negative')
                break
            elif(key == 'neutral'):
                output.append('neutral')
                break
            else:
                output.append('neutral')
                break

#print(output)
#print(len(output))


outputAggr = {'positive':output.count('positive'),'neutral':output.count('neutral'),'negative':output.count('negative')} # agrregating totals of each kind of output into a dictionary

print(outputAggr)
#plotting a bar graph
names = list(outputAggr.keys())
values = list(outputAggr.values())

plt.bar(range(len(outputAggr)), values, tick_label=names)
plt.show()
