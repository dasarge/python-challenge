import csv
import os


# 1. set path for file
# 2. Open and read csv - with open(budget_csv) as csv_file:
# 3. Set Variables
# 4. for loop and calculate, total profit, and monthly profit change
# 5. Calulate the following
#       AveRevChg = TotalRevChange / itemCount
#       GIncrease = max(revenueChange)
#       IncreaseDate = date[revenueChange.index(GIncrease)]
#       GDecrease = min(revenueChange)
#       DecreaseDate = date[revenueChange.index(GDecrease)]
# 6, write to monitor

# 1.-----------------------------------------------
budget_csv = os.path.join(
    r"C:\Users\justd\Documents\HW_Boot_camp\python-challenge\PyBank\Resources", "budget_data.csv")

# 2.-------------------------------------------------------

with open(budget_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# 3.--------------------------------------------

    total_months = []
    Profit_Loss = []
    Delta_Profit_Loss = []
    max_monthly_profit = ""
    min_monthly_profit = ""
    max_monthly_profit_date = ""
    min_monthly_profit_date = ""
    avg_profit_loss = 0
    counter = 0

# 4. -----------------------------------------------------------------------

    for row in csv_reader:
        month = row[0]
        profitLoss = row[1]
        total_months.append(month)

#
        Profit_Loss.append(int(profitLoss))

#
        if(len(Profit_Loss) > 1):
            Delta_Profit_Loss.append(
                Profit_Loss[counter] - Profit_Loss[counter-1])
        counter += 1

# 5.----------------------------------------------------------------------
    avg_profit_loss = sum(Delta_Profit_Loss) / len(Delta_Profit_Loss)

    max_monthly_profit = max(Delta_Profit_Loss)

    max_monthly_profit_date = str(
        total_months[Delta_Profit_Loss.index(max(Delta_Profit_Loss))+1])

    min_monthly_profit = min(Delta_Profit_Loss)

    min_monthly_profit_date = str(
        total_months[Delta_Profit_Loss.index(min(Delta_Profit_Loss))+1])

# 6. ------------------------------------------------

    print(f'            Financial Analysis')
    print(f'    ________________________________________')
    print(f'    Total Months:          ', len(total_months))
    print(f'    Total Profits:          $', sum(Profit_Loss))
    print(f'    Average_Profit_Change:  $', round(avg_profit_loss, 2))

    print(f'    Max Monthly Profit Date and Profit:',
          max_monthly_profit_date,  '($', max_monthly_profit, ')')
    print(f'    Min Monthly Profit Date and Profit:',
          min_monthly_profit_date,  '($', min_monthly_profit, ')')

# 7.------------------------------------------------------------

    output_file = os.path.join("Analysis", "Financial_Analysyis.txt")
    with open(output_file, "w", newline="") as datafile:
        datafile.write(f'            Financial Analysis')
        datafile.write(f'    ________________________________________')
        datafile.write(f'    Total Months:          ', (len(total_months)))
        datafile.write(f'    Total Profits:          $', sum(Profit_Loss))
        datafile.write(f'    Average_Profit_Change:  $',
                       round(avg_profit_loss, 2))

        datafile.write(f'    Max Monthly Profit Date and Profit:',
                       max_monthly_profit_date,  '($', max_monthly_profit, ')')
        datafile.write(f'    Min Monthly Profit Date and Profit:',
                       min_monthly_profit_date,  '($', min_monthly_profit, ')')
