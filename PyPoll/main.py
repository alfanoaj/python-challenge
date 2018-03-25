 # import necessary modules
import os
import csv
from collections import Counter

 #set the filename
filename = "election_data_1"

 #create an empty list for the tallycount of the election
tallycount = []

 #define csvpath as the file we want to open
csvpath = os.path.join(filename + '.csv')
 
 #Open our csv file and append the tallycount list adding a vote for the candidates as we iterate over each line
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        tallycount.append(row[2])

 #use the Counter module to count the tallycount list and then turns it into a dictionary - candidatedict
candidatedict = dict(Counter(tallycount))  

 #declares a winnercount variable for later use
winnercount = 0      

 #defines the total_votes cast for the election
total_votes = len(tallycount)

 #prints the results to the terminal
print('Election Results')
print('----------------------------')
print(f'Total Votes: ' + str(total_votes))
print('----------------------------')

 #Iterates through each candidate in the candidate dict
for name in candidatedict:
     #Finds which candidate had the most votes and sets winner to the name of the winning candiate
    if candidatedict[name] > winnercount:
        winnercount = candidatedict[name]
        winner = name
     #prints the candidate name with the percent of the vote they received and the count of the vote they received   
    print(f'' + str(name) + ': ' + str(round(candidatedict[name]/len(tallycount)*100)) + '% (' + str(candidatedict[name]) + ')')

print('-------------------------------')
 
 #prints the name of the winning candidate
print("Winner: " + str(winner))

 #declares the location of the output path, in this case, the same folder the CSV is located in
output_path = os.path.join(filename + '.txt')

 #writes and saves a text file with the same information from above
with open(output_path,'a') as text_file:
    print(f'Election Results\n'
    '----------------------------\n'
    'Total Votes: ' + str(total_votes) + '\n'
    '----------------------------', file = text_file)
    for name in candidatedict:
        if candidatedict[name] > winnercount:
            winnercount = candidatedict[name]
            winner = name
        print(f'' + str(name) + ': ' + str(round(candidatedict[name]/len(tallycount)*100)) + '% (' + str(candidatedict[name]) + ')', file = text_file)

    print(f'-------------------------------\n'
    f'Winner: ' + str(winner), file = text_file)
