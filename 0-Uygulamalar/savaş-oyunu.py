# ### Bir savaş oyunu yapalım
# ### Kahramanlar --> Ad - Vuruş Gücü - Sağlık Puanı
# ### Kahramanlar --> Ya Saldıracak / Ya da Savunacak
# ### Saldırı yapmak isteyen kahraman, [0-30] arasında kaç gücünde saldırmak istediğini seçecek. Yüksek vuruşlarda saldırı şansı düşük olacak.
# ### Saldırdığı zaman rakip saldırıya karşılık veremezse, rakibin sağlık puanı saldırı miktarınca azalacak
# ### Rakip saldırıya karşılık verebilirse, kahramanın saldırdığı miktarda sağlık puanı azalacak
# ### Rakibinin sağlık puanı 0'lanan savaşı kazanacak
import random

class Hero:
    
    def __init__(self, name):
        self.Name = name
        self.HealthPoint = 100
        
    def attack(self, hero, power, turn):
        
        if power < 10:
            hit_ratio = 0.9
        elif 10 <= power < 15:
            hit_ratio = 0.8
        elif 15 <= power < 25:
            hit_ratio = 0.5
        else:
            hit_ratio = 0.3
            
        if random.random() < hit_ratio:
            print(25*" ", self.Name, hero.Name, "'ya saldırdı!", power)
            self.hit(hero, power)
            
        else:
            print(30*" ", self.Name, "ıskaladı!", power)
            self.miss(power)
        
        self.print_info(hero, turn)
    
    def hit(self, hero, power):
        hero.HealthPoint -= power
        
    def miss(self, power):
        self.HealthPoint -= power
        
    def print_info(self, hero, turn):
        hero1 = self
        hero2 = hero
        if turn == 1:
            hero1 = self
            hero2 = hero
        elif turn == 2:
            hero1 = hero
            hero2 = self
        
        print(hero1.Name, " "*(77-len(hero1.Name) - len(hero2.Name)), hero2.Name)
        print(hero1.HealthPoint//3 * "|", " "*(77-hero1.HealthPoint//3 - hero2.HealthPoint//3), hero2.HealthPoint//3 * "|")
            

name1 = input("Lütfen 1. Kahramanın ismini giriniz: ")
name2 = input("Lütfen 2. Kahramanın ismini giriniz: ")

hero1 = Hero(name1)
hero2 = Hero(name2)

print(30*" ", "OYUN BAŞLIYOR")
turn = 1
while hero1.HealthPoint > 0 and hero2.HealthPoint > 0:
    if turn == 1:
        power = input(hero1.Name + " kaç gücünde vurmak istiyor?")
        hero1.attack(hero2, int(power), turn)
        turn = 2
        
    elif turn == 2:
        pwrs = [5, 10, 15, 20, 25, 30]
        idx = random.randint(0, len(pwrs)-1)
        hero2.attack(hero1, pwrs[idx], turn)
        turn = 1
        
if hero1.HealthPoint <= 0:
    print(30*" ", hero2.Name, "KAZANDI")
else:
    print(30*" ", hero1.Name, "KAZANDI")

