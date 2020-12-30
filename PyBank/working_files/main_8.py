import csv
import os

# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join('budget_data.csv')

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    average_profit = sum(int(csv_reader(1)) / len(int(csv_reader(1)))
    total_months=0
    total_profit=0.00
    monthly_profit_change=0.00
    mpc=monthly_profit_change
    profit_present_month=0.00
    profit_prior_month=1.00
    pprm=profit_prior_month
    pptm=profit_present_month
    item_count=0

    for x in csv_reader:
        total_months += 1
        total_profit += int(x[1])
        pptm=float(x[1])
        # mpc = (pptm - pprm) / pprm
        # profit_prior_month = profit_present_month

print(f'            Financial Analysis')
print(f'    ________________________________________')
print(f'    Total Months:           {total_months}')
print(f'    Total Profits:          ${total_profit} ')
print(f'    Average_Profit_Change:  ${pprm}')
print(f'    Average_Profit_Change:  ${pptm}')

# print(f'    Average_Profit_Change: {csv_reader[0]}, {csv_reader[1]}  {monthly_profit_change_percent} ')
