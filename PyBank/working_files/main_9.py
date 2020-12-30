import csv
import os
#import math

# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join('budget_data_2.csv')

# Open and read csv
total_profits = 0
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # next(csv_reader)
    budget_csv_len = len(budget_csv)
    total_profits = sum((i[1])for i in range("budget_csv_len"))
    #total_profits = sum((i[0])for i in range(0, "csv_reader"))

print(f'            Financial Analysis')
print(f'    ________________________________________')

print(f'    Total Profits:          ${total_profits} ')
#print(f'    Average_Profit_Change:  {average_profit} ')
