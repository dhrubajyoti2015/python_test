import pandas as pd

# making data frame from csv file
df = pd.read_csv("E:/testdata/rakesh/nba.csv")
#print(df)
#print(df[:10])
#print(df[1:10])
#df2 = df[:5]
#print(df2['Name'],"::",df2['College'],"::",df2['Team'])
#print(df2['Name'])

#print(df.aggregate(['sum', 'min']))
df2 = df.aggregate({"Number":['sum', 'min'],
              "Age":['max', 'min'],
              "Weight":['min', 'sum'],
              "Salary":['sum']})

print(df2)