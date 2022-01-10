import pandas as pd

info = {'one': pd.Series([1, 2], index=['a', 'b']),
        'two': pd.Series([1, 2, 3], index=['a', 'b', 'c'])}

df = pd.DataFrame(info)
print("The DataFrame:")
print(df)

# using del function
#print("Delete the first column:")
del df['one']
#print(df)
# using pop function
#print("Delete the another column:")
#f.pop('two')
#print(df)
print('--------------')
info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df = pd.DataFrame(info)
#print(df.loc['f'])

#print (df.iloc[3])

#sclicing rows
print (df[0:6:2])