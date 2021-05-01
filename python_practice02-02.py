"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
import time
class Tonglao():
    def __init__(self,power,hp):
        self.power = power
        self.hp = hp
    def see_people(self,name):
        self.name =name
        if self.name == "WYZ":
            print("师弟！！！！")
        elif self.name == "李秋水":
            print("呸，贱人")
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")
    def fight_zms(self,enemy_power,enemy_hp):
        self.final_hp = self.hp/2 - enemy_power
        self.final_enemy_hp = enemy_hp - self.power
        if self.final_hp > self.final_enemy_hp:
            print("天山童姥胜利")
        else:
            print("天山童姥失败")

class XuZhu(Tonglao):

    def read(self):
        print("罪过罪过")

tl = Tonglao(20,100)
tl.fight_zms(5,200)
xz = XuZhu(50,100)
