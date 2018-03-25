 #imports the os module
import os

 #sets the filename to the file we need to open
filename = "budget_data_1"

 #declares the path of the csv file we need to open
csvpath = os.path.join(filename + ".csv")

 #declares variables and sets them to 0 for later use
month_count = 0
total_revenue = 0
revenue_this_month = 0
revenue_last_month = 0
revenue_difference = 0
total_revenue_difference = 0
average_revenue_change = 0
greatest_revenue_increase = 0
greatest_revenue_decrease = 0

 #creates blank lists to be used later
monthtotal = []
monthlist = []

 #imports the csv module
import csv
 
 #opens our filepath and iterates through each line
with open(csvpath, newline = "")as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
         #adds each month's total to the monthtotal list
        monthtotal.append(row[1])
         #adds the separate months to our monthlist
        monthlist.append(row[0])

     #iterates through monthtotal list
    for row in monthtotal:

         #increments the month_count by 1 each time the list is iterated
        month_count += 1
         
         #calculates total revenue for the file
        total_revenue += int(row)

         #finds revenue for the month in the current row we are in
        revenue_this_month = int(row)

         #Calculates the difference in revenue between the current row and the previous row
        revenue_difference = revenue_this_month - revenue_last_month

         #Checks to see if the prior month had 0 revenue and does nothing, otherwise updates revenue difference accordingly
        if revenue_difference == revenue_this_month - 0:
            revenue_difference = 0
        else:
            revenue_difference = revenue_this_month - revenue_last_month

         #sets revenue last month to be used in the next iteration through the monthtotal list   
        revenue_last_month = int(row)

         #Adds revenue difference to our running total revenue difference
        total_revenue_difference += revenue_difference

         #Checks to see if we are not at the first month as there is no revenue change with just 1 month, then calculates the average revenue change
        if month_count-1 != 0:
            average_revenue_change = round(total_revenue_difference / int(month_count-1),2)
        
         #Checks to see if we have a new greatest revenue increase
        if greatest_revenue_increase < revenue_difference:
             #if we ahve a new greatest revenue increase, sets the greatest revenue decrease accordingly
            greatest_revenue_increase = revenue_difference
             #if we have a new greatest revenue decrease, sets the month_increase to the corresponding intenger for the index in the monthlist
            month_increase = int(month_count)-1

         #Checks to see if we have a new greatest revenue decrease
        if greatest_revenue_decrease > revenue_difference:
             #if we have a new greatest revenue decrease, sets the greatest revenue decrease accordingly
            greatest_revenue_decrease = revenue_difference
             #if we have a new greatest revenue decrease, sets the month_decrease to the corresponding integer for the index in the monthlist
            month_decrease = (month_count)-1

 #uses month_increase and month_decrease to pull the appropriate month out of the monthlist for greatest month increase/decrease
greatest_month_increase = monthlist[month_increase]
greatest_month_decrease = monthlist[month_decrease]

 #print our results to the terminal
print(f'Financial Analysis for ' + filename + '\n'
'------------------------------------------\n'
'Total Months: '+ str(month_count) + '\n'
'Total Revenue: $' + str(total_revenue) + '\n'
'Average Revenue Change: $' + str(average_revenue_change) +'\n'
'Greatest Increase in Revenue: ' + greatest_month_increase + ' ($' + str(greatest_revenue_increase) + ')\n'
'Greatest Decrease in Revenue: ' + greatest_month_decrease  + ' ($' + str(greatest_revenue_decrease) + ')')

 #print our results to a text file
output_path = os.path.join(filename + ".txt")
with open(output_path,'a') as text_file:
    print(f'Financial Analysis for ' + filename + '\n'  
    '------------------------------------------\n'
    'Total Months: '+ str(month_count) + '\n'
    'Total Revenue: $' + str(total_revenue) + '\n'
    'Average Revenue Change: $' + str(average_revenue_change) +'\n'
    'Greatest Increase in Revenue: ' + greatest_month_increase + ' ($' + str(greatest_revenue_increase) + ')\n'
    'Greatest Decrease in Revenue: ' + greatest_month_decrease  + ' ($' + str(greatest_revenue_decrease) + ')', file = text_file)