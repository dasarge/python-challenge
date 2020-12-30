import csv
import os


# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join(
    r"C:\Users\justd\Documents\HW_Boot_camp\python-challenge_1\PyBank", "budget_data.csv")


# Open and read csv
with open(budget_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    total_months = 0
    total_profit = 0.00
    y = 0.00

    for i in csv_reader:
        apc = 0.00
        profit_change = 0.00
        average_profit = 0.00

        total_months += 1
        total_profit += float(i[1])

        x = i[1]
        profit_change = float(x)-float(y)
        # apc = float(profit_change) / float(total_months
        apc = ((profit_change) / float(total_months))
        y = x

print(f'            Financial Analysis')
print(f'    ________________________________________')
print(f'    Total Months:           {total_months}')
print(f'    Total Profits:          ${total_profit} ')
print(f'    Average_Profit_Change:  {float(apc)} ')
print(f'    Average_Profit_Change:  {profit_change} ')
print(f'    Average_Profit_Change:  ${x}')
print(f'    Average_Profit_Change:  ${y}')
# print(f'    Average_Profit_Change:  {monthly_profit_change_1} ')
# print(f'    Average_Profit_Change:  {monthly_profit_change_2} ')
# print(f'    Average_Profit_Change: {csv_reader[0]}, {csv_reader[1]}  {monthly_profit_change_percent} ')
