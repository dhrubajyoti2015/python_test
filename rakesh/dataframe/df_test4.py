import pandas as pd
# Create first Dataframe using dictionary
info1 = pd.DataFrame({"x":[25,15,12,19],"y":[47, 24, 17, 29]})
print(info1)
# Create second Dataframe using dictionary
info2 = pd.DataFrame({"x":[25, 15, 12],"y":[47, 24, 17],"z":[38, 12, 45]})
print(info2)
# append info2 at end in info1
info = info2.append(info1,ignore_index=True)
print(info)

