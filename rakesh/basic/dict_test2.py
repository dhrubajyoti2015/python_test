
employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}

for each in employee:
    print(each)

for each in employee:
    print(employee[each])

print(employee.items())

print(employee.get("salary"))

#print(employee.get("phone"))
#print(employee['phone'])

#employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"}
for key,value in employee.items():
    print('key--',key,'value---',value)

print(len(employee))

