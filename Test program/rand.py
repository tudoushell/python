from random import randint
# 请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
# 个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰
# 子，再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。
class Die():
    def __init__(self,sides):
        self.sides=sides
    def roll_die(self):
        x=randint(1,self.sides)
        print(x,end=" ")
ten_test=Die(6)
for i in range(0,10):
    ten_test.roll_die()
twenty_test=Die(20)
for i in range(0,20):
    twenty_test.roll_die()