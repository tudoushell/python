def test(uprint_thing,print_thing):
    while uprint_thing:
        thing=uprint_thing.pop()
        print_thing.append(thing)
def showthing(thing):
    thing.reverse()
    for i in thing:
        print(i+"\n")
uprinted_designs=['iphone case','robot pendant','dodecahedron']
printed_design=[]
test(uprinted_designs,printed_design)
showthing(printed_design)
for i in uprinted_designs:
    print(i+"\n")


