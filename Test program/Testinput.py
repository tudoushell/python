flag=True
information={}
while flag:
    name=input("please input your name ")
    age=input("please input your age ")
    information[name]=age
    flags=input("if you continue type information yes/no? ")
    if flags=="yes":
        flag=True
    else:
        flag=False
for name,age in information.items():
    print("name: "+name+"\n"+"age: "+age+"\n")
