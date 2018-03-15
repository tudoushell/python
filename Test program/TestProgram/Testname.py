from Test import formatname as Testname
print("please input q to quit this program")
while True:
    first_name=input("please input first name ")
    if first_name=='q':
        break
    last_name=input("please input last name ")
    if last_name=='q':
        break
    print(Testname(first_name,last_name))