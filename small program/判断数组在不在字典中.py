#该字典中的文字在不在当前的字典中
#定义一个字典
name={
 'jen':'python',
 'sarah':'c',
 'plil':'ruby'
 }
#定义一个数组
welcome_name=['jen','sarah','plil','mike']
#循环字典文件
for i in range(0,len(welcome_name)):
	#判断该数组在不在字典文件中，在的话打印，不在的话也打印
	if welcome_name[i] in name.keys():
		print("welcome to "+welcome_name[i])
	else:
		print("please visit this meeting "+welcome_name[i])
