
import os
if os.path.exists("E:/training/testdata/data2.txt"):
  os.remove("E:/training/testdata/data2.txt")
  print("file removed successfully")
else:
  print("The file does not exist")