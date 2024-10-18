import random

class Character:
    def __init__(self, name, hp, attack, dodge):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.dodge = dodge
    
    def take_damage(self, damage):
        self.hp -= damage
    
    def hit(self, target):
        damage = self.attack
        miss = random.randint(1, 10 - self.dodge)
        if miss == random.randint(1, 10 - self.dodge):
          target.take_damage(0)
          print(f"{target.name} dodged the attack!")
        else:
          target.take_damage(damage)
          print(f"{self.name} attacks {target.name} for {damage} damage!")

        
class Player(Character):
    def __init__(self, name, hp, attack, dodge):
        super().__init__(name, hp, attack, dodge)
        
class Enemy(Character):
    def __init__(self, name, hp, attack, dodge):
        super().__init__(name, hp, attack, dodge)

    fighter = Player("Fighter", 5, 3, 2)
    mage = Player("Mage" ,1, 5, 7)
    thief = Player("Thief" ,4, 3, 8)
    i = 1
    
    print("Welcome to Fighter Arena")
    x = input("Enter Your Name: ")
    print("Choose Your Character (fighter = 1 | mage = 2 | thief = 3)")
    choice = input()
    
    if choice == '1':
      player = fighter
    
    if choice == '2':
      player = mage
    
    if choice == '3':
      player = thief

    while True:
      enemy = random.randint(1,3)
      if enemy == 1:
        enemy = fighter
        print("\nYou are fighting a fighter!")
        break
      if enemy == 2:
        enemy = mage
        print("\nYou are fighting a mage!")
        break
      if enemy == 3:
        enemy = thief
        print("\nYou are fighting a thief!")
        break
        
    userCount = 0
    targetCount = 0

    for i in range(100):
      print("\nRound", i)
      battles = True
      first = random.randint(1, 2)

      if player == fighter:
        player.hp = 5

      if player == mage:
        player.hp = 1

      if player == thief:
        player.hp = 4

      if enemy == fighter:
        enemy.hp = 5

      if enemy == mage:
        enemy.hp = 1

      if enemy == thief:
        enemy.hp = 4
      
      while battles is True:
          if first == 1:
            player.hit(enemy)
            if enemy.hp <= 0:
              print("You win!")
              userCount+=1
              break
              
            enemy.hit(player)
            if player.hp <= 0:
              print("You lose!")
              targetCount+=1
              break
              
          if first == 2:
            enemy.hit(player)
            if player.hp <= 0:
              print("You lose!")
              targetCount+=1
              break
              
            player.hit(enemy)
            if enemy.hp <= 0:
              print("You win!")
              userCount+=1
              break

    print(f"\nYou won", userCount, "times!")
    print(f"AI won", targetCount, "times!")