
try:
    f = open('E:/testdata/rakesh/test1.csv','r')
    for line in f:
        list = line.split(",")
        #print(line.split(",")[0])
        print(list[0],",",list[4],",",list[7])
finally:
    f.close()
