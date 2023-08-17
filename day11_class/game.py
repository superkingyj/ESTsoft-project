import random

class Player():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Game: 

    def __init__(self):
        self.player = Player("지삐", 100, 10)
        self.enemy = Player("별이", 50, 5)

        while self.player.attack > 0 and self.enemy.health > 0:
            print(f"{self.player.name}의 차례입니다")
            self.player_turn()
            print(f"{self.enemy.name}의 차례입니다.")
            self.enemy_turn()

        if self.player.health > 0: print("승리하였습니다")
        else: print("패배하였습니다ㅠㅠ")


    def player_turn(self):
        action = int(input("어떤 행동을 하겠습니까? (1: 건초어택/2: 사료스킬) "))
        
        if action == 1:
            attack_damage = random.randint(1, self.player.attack)
            self.attack(self.player.name, attack_damage)
            self.enemy.health -= attack_damage
            self.current_health(self.enemy.name, self.enemy.health)
        elif action == 2:
            skill_damage = random.randint(1, self.player.attack+5)
            self.attack(self.player.name, skill_damage)
            self.enemy.health -= skill_damage
            self.current_health(self.enemy.name, self.enemy.health)
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            self.player_turn()

    def enemy_turn(self):        
        enemy_attack_damage = random.randint(1, self.enemy.attack)
        self.attack(self.enemy.name, enemy_attack_damage)
        self.player.health -= enemy_attack_damage
        self.current_health(self.player.name, self.player.health)

    def attack(self, character_name, attack_damage):
        print(f"{character_name}의 공격! 적에게 {attack_damage}의 피해를 입혔습니다!")
        print()

    def current_health(self, charater_name, remain_health):
        print(f"{charater_name}의 체력이 {remain_health}만큼 남았습니다.")
    
game = Game()