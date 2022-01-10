list = ["ab","cd","ef",[1,2,3,4],True]
print(list)

with open("E:/training/testdata/test4.txt",'w',encoding = 'utf-8') as file:
    file.write(str(list))
file.close()