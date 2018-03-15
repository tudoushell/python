filename = 'F:\hello.txt'
with open(filename,"w") as file:
    flag=True
    while flag:
        name=input("please input your name ")
        print("hello "+name) 
        file.write(name+"\n")
        flag=input("can you continue write yes/no?")
        if flag=="yes":
            flag=True
        else:
            flag=False
            print("Thank you !")
            
