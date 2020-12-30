# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import pandas as pd
csvpath = os.path.join('Resources', 'election_data.csv')
Candidate = (row[2])

with open(csvpath, newline='', encoding='utf-8') as csvfile:
    # with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Candidate.append(row[1])

#df = pd.DataFrame(index=index, columns=columns)
df = pd.read_csv('Resources/election_data.csv')

s = pd.Candidate(df.election_data_test)

s1 = pd.Series({'nunique': len(s), 'unique values': s.index.tolist()})
s.append(s1)

# _this works to print---print(len(df))
print(df.head(10))

# Method 2: Improved Reading using CSV module
# with open(csvpath) as csvfile:
# CSV reader specifies delimiter and variable that holds contents
#csvreader = csv.reader(csvfile, delimiter=',')
# print(csvreader)
# Read the header row first (skip this step if there is now header)
#csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")
# Read each row of data after the header
#    for row in csvreader:
#       print(row)
