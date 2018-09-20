from character import Enemy
dave = Enemy("Dave","A smelly zombie")

dave.describe()

dave.talk()

dave.set_conversation("Uuuuuuurgh!")

dave.talk()

dave.set_weakness("Onions")

print("Dave is allergic to " + dave.weakness)

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
