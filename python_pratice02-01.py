"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。

"""


class pets():
#定义宠物价格、每天的花费、宠物的寿命天数
    def __init__(self,price,spend_life,lifes):
        self.price = price
        self.spend_life = spend_life
        self.lifes = lifes
        self.costs = self.price + self.spend_life * self.lifes
#宠物所花费钱
    def cat(self,):
        print("宠物猫需要花费{}".format(self.costs))
#宠物狗训练费用
    def dog(self,training_expenses):
        self.training_expenses = training_expenses
        self.costs = self.price + self.spend_life * self.lifes+self.training_expenses
        print("宠物狗需要花费{}".format(self.costs))

cost = pets(10,20,100)
cost.cat()
cost.dog(30)

