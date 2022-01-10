final_list = []
str = ''
try:
    f = open('E:/testdata/rakesh/test1.csv', 'r')
    count = 0
    for line in f:
        print(count)
        list = line.split(",")
        # print(line.split(",")[0])
        # print(list[0],",",list[4],",",list[7])
        str = list[0]+","+list[4]+","+list[7]
        print(str)
        count = count + 1
        final_list.append(str)
    #print(final_list)
    print(str)
    #for each in final_list:
        #print(each)
    rakesh = open('E:/testdata/rakesh/test3.txt','w')
    for element in final_list:
        rakesh.write(element+"\n")

finally:
    f.close()
    rakesh.close()
