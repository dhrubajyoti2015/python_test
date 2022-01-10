try:
    with open('E:/testdata/rakesh/test2.txt','a',encoding="utf-8") as f:
        f.write("hello deep\n")
        f.write("welcome to python\n")
except Exception as ex:
    print("exception --",ex)

finally:
    f.close()