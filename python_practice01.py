"""
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

def fight():
    enemy_name = input("请输入角色名称：")
    enemy_hp = int(input("请输入角色血量："))
    enemy_power = int(input("请输入角色力量："))
    my_power = 200
    hp = 1000
    my_name = "test"
    while True:
        hp = hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print("我的血量：{},敌人的血量：{}".format(hp,enemy_hp))
        if enemy_hp<=0:
            print("{}输了".format(enemy_name))
            break
        elif hp<=0:
            print("{}输了".format(my_name))
            break

# def role_messages():
#     enemy_name = input("请输入角色名称：")
#     enemy_hp = int(input("请输入角色血量："))
#     enemy_power = int(input("请输入角色力量："))
#     return enemy_name,enemy_hp,enemy_power

if __name__ == "__main__":
    # role_messages()
    fight()
