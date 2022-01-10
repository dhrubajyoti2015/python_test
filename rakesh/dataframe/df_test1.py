import pandas as pd

x = ['Python', 'Pandas']
print(x)
# Calling DataFrame constructor on list
df = pd.DataFrame(x)
print(df)

data = {"name":['deep','rakesh','sathya'],"age":[30,29,28]}
print(data)
print(type(data))

df1 = pd.DataFrame(data)
print(df1)

info = {'ID' :[101, 102, 103],'Department' :['B.Sc','B.Tech','M.Tech',]}
df = pd.DataFrame(info)
print (df)