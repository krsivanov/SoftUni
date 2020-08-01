needed_experience = float(input())
count_of_battles = int(input())
battle_count = 0
current_experience = 0
is_collected = False

experience_per_battle = float(input())

while is_collected==False and battle_count<count_of_battles:
    battle_count += 1
    if battle_count% 3==0:
        experience_per_battle = 1.15*experience_per_battle
        current_experience += experience_per_battle
    elif battle_count%5==0:
        experience_per_battle = 0.9*experience_per_battle
        current_experience += experience_per_battle
    else:
        current_experience += experience_per_battle

    if current_experience>=needed_experience:
        is_collected = True
        break
    else:
        if battle_count==count_of_battles:
            break
        else:
            experience_per_battle=float(input())

if is_collected:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience-current_experience:.2f} more needed.")