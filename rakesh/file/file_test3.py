
try:
    with open('E:/testdata/rakesh/test1.csv','r',encoding="utf-8") as f:
        for each in f:
            print(each)
except Exception as ex:
    print("exception --",ex)

finally:
    f.close()
