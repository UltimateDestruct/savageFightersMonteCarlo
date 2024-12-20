import json
from fighter import Fighter
from helpers.helper import load_config

# Load the global config values
config = load_config()

def choose_fighters():
    # Choose fighter 1
    if config['default_fighter_1']:
        fighter1 = config['default_fighter_1']
    else:
        fighter1 = input("Input Fighter 1: ")

    # Choose fighter 2
    if config['default_fighter_2']:
        fighter2 = config['default_fighter_2']
    else:
        fighter2 = input("Input Fighter 2: ")

    return [fighter1, fighter2]

def load_fighter_json_data(fighter):
    with open('./fighters/' + fighter + '.json', 'r') as file:
        data = json.load(file)
    return data


def create_fighter(fighter):
    data = load_fighter_json_data(fighter)
    character = Fighter(
        data['fighter']['name'],
        data['fighter']['hp'],
        data['fighter']['moves'],
        1
    )
    return character


def list_fighter_moves(fighter):
    data = load_fighter_json_data(fighter)

    print(f"{data['fighter']['name']}")
    for page, details in data['fighter']['moves'].items():
        print(f"Page: {page[0]}: {details['name']}, Next Moves: {details['moveOptions']}")


def list_fighter_stats(fighter_list):
    for fighter in fighter_list:
        print(f"***************")
        print(f"Name: {fighter.name}\nHP: {fighter.hp}\nMoves: {fighter.moves}\nCurrent Move: {fighter.current_move}\nNext Moves: {fighter.next_moves}")


def check_for_defeated_fighter(fighter_list):
    if fighter_list[0].hp <= 0 and fighter_list[1].hp <= 0:
        print(f"Both fighters lost")
    elif fighter_list[0].hp <= 0:
        print(f"{fighter_list[1].name} wins!")
    elif fighter_list[1].hp <= 0:
        print(f"{fighter_list[0].name} wins!")
    else:
        print(f"Something went wrong...")


def resolve_damage(source_move, target_move, target):
    source_move_type = source_move.get('type')
    target_move_type = target_move.get('type')
    damage = 0

    match (source_move_type, target_move_type):
        case('basicAttack', 'basicAttack') | ('basicAttack', 'fighterStance'):
            damage = source_move.get('damage')
        case _:
            # Other types of damage unnecessary to calculate at this time
            print(f"No damage")

    target.hp -= damage


def print_fighter_move_details(fighter):
    print(f"Name: {fighter.name}")
    print(
        f"Current Move: {fighter.current_move} ({fighter.moves[str(fighter.current_move)]['name']}, dmg: {fighter.moves[str(fighter.current_move)]['damage']})")
    print(f"HP: {fighter.hp}")
    print(f"Next Move: {fighter.next_moves}")
    print(f"-----------")


def battle(fighter_list):
    num_turns = config['max_number_of_turns']
    for i in range(num_turns):

        # Check if any of the fighters were defeated
        if any(fighter.hp <= 0 for fighter in fighter_list):
            check_for_defeated_fighter(fighter_list)
            break

        if config['display_battle_log']:
            print(f"==============")
            print(f"Move: {i+1}")
            print(f"==============")
        for index, fighter in enumerate(fighter_list):
            if config['display_battle_log']:
                print_fighter_move_details(fighter)

            if fighter == fighter_list[0]:
                source = fighter_list[0]
                target = fighter_list[1]
            else:
                source = fighter_list[1]
                target = fighter_list[0]

            source_move = source.moves.get(str(source.current_move))
            target_move = target.moves.get(str(target.current_move))
            resolve_damage(source_move, target_move, target)

            # Randomly choose a new move and update the moveset
            fighter.current_move = fighter.randomly_select_next_move()
            fighter.update_next_moves()

def main():


    fighters = choose_fighters()
    # list_fighter_moves(fighters[0])
    # list_fighter_moves(fighters[1])
    # list_fighter_stats(fighter_list)

    fighter1 = create_fighter(fighters[0])
    fighter2 = create_fighter(fighters[1])
    fighter_list = [fighter1, fighter2]

    battle(fighter_list)


if __name__ == "__main__":
    main()
