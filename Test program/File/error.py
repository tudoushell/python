# 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
# 文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
# 的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
while True:
    try:
        i=int(input("please input data \n"))
        j=int(input("please input next data \n"))
        z=i+j
    except :
        print("your type data is error")
    else:
        print('%d'"+"'%d'"="'%d'%(i,j,z))
        flag=input("over the program yes/no \n")
        if flag=="yes":
            break;