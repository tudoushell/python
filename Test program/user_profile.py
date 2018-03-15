def build_user(first,last,**information):
    family={}
    family["first_name"]=first
    family["last_name"]=last
    for i,j in information.items():
        family[i]=j
    return family
first_name='z'
last_name='k'
address={'home':'ten','phone':'12323'}
infor=build_user(first_name,last_name,home='ten',phone=123)
for i,j in infor.items():
    print(i)
    print(j)