from random import randrange

# dieRoll(3) -> [5, 3, 1] :: returns list sorted
def die_roll(how_many_die = 0):
    """

    :type how_many_die: How many die/dice you want to be contained in the list
    """
    i = 0
    result_list = []
    while i < how_many_die:
        result_list.append(randrange(1, 7))
        i += 1

    result_list.sort()
    result_list.reverse()
    return(result_list)

attacking_countries = input("How many of your countries can attack the defenders country?")
attack_troops = input("How many troops do you have available to attack with?")
defence_troops = input("How many troops does the defender have available?")
init_attack_troops = attack_troops

while defence_troops > 0 and attack_troops >= attacking_countries:
    if attack_troops >= 3 and defence_troops >= 2:
        # Roll the dice
        attackers_roll = die_roll(3)  # Attack with maximum amount of troop(s)
        defenders_roll = die_roll(2)  # Defence with maximum amount of troop(s)
        # First Highest Die Comparison
        if max(attackers_roll) > max(defenders_roll):
            defence_troops -= 1
        elif max(attackers_roll) == max(defenders_roll):
            attack_troops -= 1
            defence_troops -= 1
        else:  # If max(attackers_roll) < max(defenders_roll)
            attack_troops -= 1
        # Second Highest Die Comparison
        if attackers_roll[1] > attackers_roll[1]:
            defence_troops -= 1
        elif attackers_roll[1] == attackers_roll[1]:
            attack_troops -= 1
            defence_troops -= 1
        else:  # if attackers_roll[1] < defenders_roll[1]
            attack_troops -= 1

    elif attack_troops >= 3 and defence_troops <= 2:
        # Roll the dice
        attackers_roll = die_roll(3)  # Attack with maximum amount of troop(s)
        defenders_roll = die_roll(defence_troops)  # Defence with maximum(1) amount of troop(s)
        # First Highest Die Comparison
        if max(attackers_roll) > max(defenders_roll):
            defence_troops -= 1
        elif max(attackers_roll) == max(defenders_roll):
            attack_troops -= 1
            defence_troops -= 1
        else:  # if max(attackers_roll) < max(defenders_roll)
            attack_troops -= 1
        # Second Highest Die Comparison
        if defence_troops == 2:
            if attackers_roll[1] > attackers_roll[1]:
                defence_troops -= 1
            elif attackers_roll[1] == attackers_roll[1]:
                attack_troops -= 1
                defence_troops -= 1
            else:  # if attackers_roll[1] < defenders_roll[1]
                attack_troops -= 1

    elif attack_troops < 3 and defence_troops == 1:
        # Roll the dice
        attackers_roll = die_roll(attack_troops)  # Attack with maximum amount of troop(s)
        defenders_roll = die_roll(defence_troops)  # Defence with maximum(1) amount of troop(s)
        # First Highest Die Comparison
        if max(attackers_roll) > max(defenders_roll):
            defence_troops -= 1
        elif max(attackers_roll) == max(defenders_roll):
            attack_troops -= 1
            defence_troops -= 1
        else:  # if max(attackers_roll) < max(defenders_roll)
            attack_troops -= 1

    elif attack_troops <= 3 and attack_troops >= 2  and defence_troops >= 2:
        # Roll the dice
        attackers_roll = die_roll(attack_troops) # Attack with maximum amount of troop(s)
        defenders_roll = die_roll(2) # Defence with maximum(1) amount of troop(s)
        # First Highest Die Comparison
        if max(attackers_roll) > max(defenders_roll):
            defence_troops -= 1
        elif max(attackers_roll) == max(defenders_roll):
            attack_troops -= 1
            defence_troops -= 1
        else:  # if max(attackers_roll) < max(defenders_roll)
            attack_troops -= 1
        # Second Highest Die Comparison
        if attackers_roll[1] > attackers_roll[1]:
            defence_troops -= 1
        elif attackers_roll[1] == attackers_roll[1]:
            attack_troops -= 1
            defence_troops -= 1
        else:  # if attackers_roll[1] < defenders_roll[1]
            attack_troops -= 1

    else:  #Never to be used...
        continue

    print("{0} Attacking Troops Remain... {1} Defending Troops Remain.").format(attack_troops, defence_troops)

if defence_troops == 0:
    print("You have taken over the enemies territory! {0} troops have been lost, {1} remain.").format(init_attack_troops - attack_troops, attack_troops)
