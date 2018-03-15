def magician(name):
    for names in name:
        print(names)
        print("\n")
def make_great(name,change_name):
    while name:
        names=name.pop()
        change_name.append(names+" the great")
def show_name(name,chang_name):
    for names in chang_name:
        print(names)
    for n in name:
        print(n)
            
magician_name=["zk","wj"]
change_name=[]
magician(magician_name)
make_great(magician_name[:],change_name)
show_name(magician_name,change_name)