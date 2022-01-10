
try:
    with open('E:/testdata/rakesh/test2.txt','w',encoding="utf-8") as f:
        f.write("hello rakesh\n")
        f.write("welcome to python\n")
except Exception as ex:
    print("exception --",ex)

finally:
    f.close()