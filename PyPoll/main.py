import os
import csv

# declare paths, vars. in this case using votes list to hold all votes as dict objects
path = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('analysis', 'election_analysis.txt')
votes = []

# Read in the CSV file
with open(path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # create vote object and add it to our list
    for row in csvreader:
        vote = dict()
        vote["id"] = row[0]
        vote["county"] = row[1]
        vote["candidate"] = row[2]
        votes.append(vote)

# time for number crunching. iterating through our list of votes to calculate proportions for each candidate. 
# results will be stored as new dictionary which we can reference when printing/writing
results = { "total" : 0 }
winner = { "count" : 0, "name" : ''}
for vote in votes:
    #increment total
    results["total"] = results["total"] + 1
    #if candidate doesn't exist in list (as a key), add the candidate with 1 vote. otherwise increment candidate votes by 1
    if(vote["candidate"] in results.keys()):
        results[vote["candidate"]] = results[vote["candidate"]] + 1
    else:
        results[vote["candidate"]] = 1

# print to console        
print("Election Results\n--------------")
print("Total Votes: " + str(results["total"]) + "\n--------------")
for key in results.keys():
    if key != "total":
        if winner["count"] < results[key]:
            winner["name"] = key
            winner["count"] = results[key]
        print(key + ": " + str(round(results[key]/results["total"]*100,3)) + "% (" + str(results[key]) + ")")
print("--------------")
print("Winner: " + winner["name"] + "\n--------------")

# write to file
with open("analysis/election_results.txt", "w") as textfile:
    textfile.write("Election Results\n" + "--------------")
    textfile.write("\nTotal Votes: " + str(results["total"]) + "\n--------------")
    for key in results.keys():
        if key != "total":
            textfile.write("\n" + key + ": " + str(round(results[key]/results["total"]*100,3)) + "% (" + str(results[key]) + ")")
    textfile.write("\n--------------")
    textfile.write("\nWinner: " + winner["name"] + "\n--------------")