number_of_heroes = int(input())
hero = {}


for i in range(number_of_heroes):
  args = input().split()
  hero[args[0]]= [int(args[1]),int(args[2])]
  
while True:
  tokens = input().split(" - ")
  action=tokens[0]

  if action=='End':
    break
  
  elif action =="CastSpell":
    hero_name=tokens[1]
    mp_needed=int(tokens[2])
    spell_name=tokens[3]
    if mp_needed <= hero[hero_name][1]:
      hero[hero_name][1]-=mp_needed
      print(f"{hero_name} has successfully cast {spell_name} and now has {hero[hero_name][1]} MP!")
    else:
      print(f"{hero_name} does not have enough MP to cast {spell_name}!")

  elif action =='TakeDamage':
    hero_name=tokens[1]
    damage_taken=int(tokens[2])
    attacker = tokens[3]
    if hero[hero_name][0] > damage_taken:
      hero[hero_name][0] -= damage_taken
      print(f"{hero_name} was hit for {damage_taken} HP by {attacker} and now has {hero[hero_name][0]} HP left!")
    else:
      print(f"{hero_name} has been killed by {attacker}!")
      hero.pop(hero_name)


  elif action=="Recharge":
    hero_name = tokens[1]
    recharged_mp = int(tokens[2])
    if hero[hero_name][1]+recharged_mp <=200:

      hero[hero_name][1]+= recharged_mp
    else:
      recharged_mp = 200 - hero[hero_name][1]
      hero[hero_name][1]=200

    print(f"{hero_name} recharged for {recharged_mp} MP!")


  elif action =='Heal':
    hero_name = tokens[1]
    healed_hp = int(tokens[2])
    if hero[hero_name][0]+healed_hp <=100:

      hero[hero_name][0]+= healed_hp
    else:
      healed_hp = 100 - hero[hero_name][0]
      hero[hero_name][0]=100

    print(f"{hero_name} healed for {healed_hp} HP!")


sorted_hero = dict(sorted(hero.items(), key= lambda h: (-h[1][0],h[0])))

for (key,value) in sorted_hero.items():
  print(f'{key}')
  print(f'  HP: {value[0]}')
  print(f'  MP: {value[1]}')
