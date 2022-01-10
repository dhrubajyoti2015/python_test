import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two': pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}

df = pd.DataFrame(info)
#print(d1)

#print d1['one'])

print("Add new column by passing series")
df['three'] = pd.Series([20, 40, 60], index=['a', 'b', 'c'])
print(df)

print("Add new column using existing DataFrame columns")
df['four'] = df['one'] + df['three']

print(df)