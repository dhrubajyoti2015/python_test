list =[]

try:
    with open("E:/training/testdata/data2.txt","r",encoding = 'utf-8') as file:
        data = file.readlines()
        for line in data:
            #word = line.split(",")
            #print(word)
            list.append(line.rstrip('\n'))
except Exception:
    print("file not found")
else:
    for each in list:
        print(each)
finally:
    file.close()

#for each in list:
    #print(each)