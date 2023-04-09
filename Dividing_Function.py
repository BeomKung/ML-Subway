import pandas as pd

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', index_col=0, header=0)
Revenue = pd.read_excel('Data/All_Revenue_Loss.xlsx', index_col=0, header=0)

index = [2, 6, 10, 14, 18, 22, 26, 30, 34]

MonthPeople = []
for i in range(48):
  tempList = []
  for j in index:
    SumPeople = 0
    SumPeople = Subway.iloc[i, j] // 1000
    tempList.append(SumPeople)
  MonthPeople.append(tempList)

ratio = []
for i in range(48):
  AllMonthPeople = 0
  tempList2 = []

  for j in range(9):
    AllMonthPeople = AllMonthPeople + MonthPeople[i][j]

  for k in range(9):
    temp = 0
    temp = MonthPeople[i][k] / AllMonthPeople
    tempList2.append(round(temp, 2))
  ratio.append(tempList2)

MonthRevenue = []
for i in range(48):
  tempList3 = []

  for j in range(9):
    RevenueYear = 0
    RevenueYear = Revenue.iloc[0, i] * ratio[j]
    tempList3.append(RevenueYear)
  MonthRevenue.append(tempList3)

print(MonthRevenue)