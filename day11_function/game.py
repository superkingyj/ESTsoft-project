import random

player_name = "지삐"
player_health = 100
player_attack = 10

enemy_name = "별이"
enemy_health = 50
enemy_attack = 5

def player_turn():
    global enemy_health
    action = int(input("어떤 행동을 하겠습니까? (1: 건초어택/2: 사료스킬) "))
    
    if action == 1:
        attack_damage = random.randint(1, player_attack)
        attack(player_name, attack_damage)
        enemy_health -= attack_damage
        current_health(enemy_name, enemy_health)
    elif action == 2:
        skill_damage = random.randint(1, player_attack+5)
        attack(player_name, skill_damage)
        enemy_health -= skill_damage
        current_health(enemy_name, enemy_health)
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        player_turn()

def enemy_turn():
    global player_health
    
    enemy_attack_damage = random.randint(1, enemy_attack)
    attack(enemy_name, enemy_attack_damage)
    player_health -= enemy_attack_damage

def attack(character_name, attack_damage):
    print(f"{character_name}의 공격! 적에게 {attack_damage}의 피해를 입혔습니다!")
    print()

def current_health(charater_name, remain_health):
    print(f"{charater_name}의 체력이 {remain_health}만큼 남았습니다.")


while player_attack > 0 and enemy_health > 0:
    print(f"{player_name}의 차례입니다")
    player_turn()

    print(f"{enemy_name}의 차례입니다.")
    enemy_turn()

if player_health > 0: print("승리하였습니다")
else: print("패배하였습니다ㅠㅠ")

