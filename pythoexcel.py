#import pandas lib as pd
#from pickle import NONE
import pandas as pd
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('CG Report 2022.xlsx', sheet_name = 'Sheet1')
sum_stcg = 0.0
index_stcg = dataframe1.columns.get_loc('STCG')
print(dataframe1)
#finding the sum of stcg
for row in range(0, len(dataframe1)):
    if((dataframe1.iat[row, index_stcg])):
        sum_stcg = float(sum_stcg) + float(dataframe1.iat[row, index_stcg])

print("Sum of STCG = ", sum_stcg)
#finding the sum of LTCG
sum_ltcg = 0.0
index_ltcg = dataframe1.columns.get_loc('LTCG')
for row in range(0, len(dataframe1)):
    if((dataframe1.iat[row, index_ltcg])):
         sum_ltcg = float(sum_ltcg) + float(dataframe1.iat[row, index_ltcg])
        
print("Sum of LTCG = ", sum_ltcg)
#finding sum of STCG group by mont
dataframe2 = pd.read_excel('CG Report 2022.xlsx', sheet_name = 'Sheet1')
indexofmonth = dataframe2.columns.get_loc('Date')
dataframe2.groupby('Date')
print(dataframe2)
 #dataframe1.groupby()
