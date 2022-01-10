
final_list =[]
try:
    f = open('E:/testdata/rakesh/test1.csv','r')
    for line in f:
        list = line.split(",")
        #print(line.split(",")[0])
        #print(list[0],",",list[4],",",list[7])
        final_list.append(list[0])
        
    print(final_list)
finally:
    f.close()