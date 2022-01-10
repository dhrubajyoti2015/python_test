import pandas as pd

# Creating the dataframe
df = pd.read_csv("E:/training/testdata/nba.csv")
# Print the dataframe
df1 = df.groupby('Team')

#print(df1.first())
print(df1.get_group('Boston Celtics'))

df2 = df.groupby(['Team', 'Position'])
#print(df2.first())
print(df2.head(5))
