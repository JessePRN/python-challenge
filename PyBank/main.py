import os
import csv

# init variables, paths
path = os.path.join('Resources', 'budget_data.csv')
outputPath = os.path.join('analysis', 'budget_analysis.txt')
totalMonths = 0
profits = []

# Read in the CSV file
with open(path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    # this first iteration is to read in the file as a json list, we parse through it in the next for loop
    # at some point I wanted a snapshot in memory rather than run all arithmetic on one iteration
    # probably not necessary!
    for row in csvreader:
        totalMonths = totalMonths + 1
        monthly = {
            "date" : row[0],
            "profit" : row[1],
            "change" : 0,
            "subtotal" : 0
        }
        profits.append(monthly)
#end open file

#vars to get stats needed for output
profitMax = 0
profitMin = 0
maxDate = ''
minDate = ''
changesMax = 0.0
changesMin = 0.0
changes = 0.0
changesSum = 0.0
lastMonth = 0.0
totalProfit = 0

for row in profits:
    # iterating through the list we created earlier, we target the stats required for proper output

    # mechanism to skip first month while aggregating profit changes month to month
    if(lastMonth != 0.0):
        changes = float(lastMonth) - float(row["profit"])
    row["changes"] = changes
    if(lastMonth  != 0.0):
        changesSum = changesSum + changes
    #update    
    lastMonth = row["profit"]
    # keep track of totalProfit, record max/min info
    totalProfit += int(row["profit"])
    if(changesMax < changes):
        changesMax = changes
        maxDate = row["date"]
    if(changesMin > changes):
        changesMin = changes  
        minDate = row["date"]

# GOOD BELOW

print("Financial Analysis\n" + "--------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(totalProfit))
#-1 to months to compensate for first year (drove me crazy for 30 minutes!)
print("Average Change: $" + str(round(-1*(changesSum/(totalMonths - 1)),2)))
print("Greatest Increase in Profits: " + minDate + " " + str(-1*changesMin))
print("Greatest Decrease in Profits: " + maxDate + " " + str(-1*changesMax)) 

with open("analysis/budget_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n" + "--------------")
    textfile.write("\nTotal Months: " + str(totalMonths))
    textfile.write("\nTotal: $" + str(totalProfit))
    textfile.write("\nAverage Change: $" + str(round(-1*(changesSum/(totalMonths - 1)),2)))
    textfile.write("\nGreatest Increase in Profits: "  + minDate + " " + str(-1*changesMin))
    textfile.write("\nGreatest Decrease in Profits: " + maxDate + " " + str(-1*changesMax)) 