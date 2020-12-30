import csv
import os


# set path for file
# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join(
    r"C:\Users\justd\Documents\HW_Boot_camp\python-challenge_1\PyBank", "budget_data.csv")
# -------------------------------------------------------

# Open and read csv
# with open(budget_csv) as csv_file:
with open(budget_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    date = []
    total_months = []
    Profit_Loss = []
    Delta_Profit_Loss = []

    max_monthly_profit_date = ""
    min_monthly_profit_date = ""

    avg_profit_loss = []

    for i in csv_reader:
        date.append(i[0])
        total_months.append(i[0])

        # revenue.append(int(row[1]))
        Profit_Loss.append(int(i[1]))

# -----------------------------------------------------------------------
    for j in range(1, len(Profit_Loss)):

        # TotalRev = TotalRev + int(row[1])

        Delta_Profit_Loss.append(Profit_Loss[j] - Profit_Loss[j-1])

    # RevEnd = int(row[1])

        # AveRevChg = TotalRevChange / itemCount
        avg_profit_loss = sum(Delta_Profit_Loss) / len(Delta_Profit_Loss)

        # GIncrease = max(revenueChange)
        max_monthly_profit = max(Delta_Profit_Loss)

        # IncreaseDate = date[revenueChange.index(GIncrease)]
        max_monthly_profit_date = date[Delta_Profit_Loss.index(
            max_monthly_profit)]

        min_monthly_profit = min(Delta_Profit_Loss)

        min_monthly_profit_date = date[Delta_Profit_Loss.index(
            min_monthly_profit)]

# --write to file----------------------------------------------

# with open('financial_report' + str(str(i)+1) + '.txt', 'w') as text:

    # --------------------------------------------------------------

    print(f'            Financial Analysis')
    print(f'    ________________________________________')
    print(f'    Total Months:          ', len(total_months))
    print(f'    Total Profits:          $', sum(Profit_Loss))
    print(f'    Average_Profit_Change:  $', round(avg_profit_loss, 2))
    print(f'    Max Monthly Profit Date and Profit:',
          max_monthly_profit_date,  '($', max_monthly_profit, ')')
    print(f'    Min Monthly Profit Date and Profit:',
          min_monthly_profit_date,  '($', min_monthly_profit, ')')
