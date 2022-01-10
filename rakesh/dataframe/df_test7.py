import pandas as pd

# making data frame from csv file
df = pd.read_csv("E:/testdata/rakesh/nba.csv")

a = df.groupby('Team')
#print(a.first())
#print(a.get_group('Boston Celtics'))

b = df.groupby('College')
#print(b.get_group('Texas'))

c = df.groupby(['Team', 'Position'])
print(c.head(3))
