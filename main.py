import json
from fighter import Fighter

def choose_fighters():
    # fighter1 = input("Input Fighter 1: ")
    # fighter2 = input("Input Fighter 2: ")
    fighter1 = "fire_monster"
    fighter2 = "ice_monster"
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


def resolve_damage(move, target):
    damage = move.get('damage')
    target.hp -= damage

def battle(fighter_list):
    for i in range(20):

        # Check if any of the fighters were defeated
        if any(fighter.hp <= 0 for fighter in fighter_list):
            if fighter_list[0].hp <= 0 and fighter_list[1].hp <= 0:
                print(f"Both fighters lost")
            elif fighter_list[0].hp <= 0:
                print(f"{fighter_list[1].name} wins!")
            elif fighter_list[1].hp <= 0:
                print(f"{fighter_list[0].name} wins!")
            else:
                print(f"Something went wrong...")
            break

        print(f"==============")
        print(f"Move: {i+1}")
        print(f"==============")
        for index, fighter in enumerate(fighter_list):
            print(f"Name: {fighter.name}")
            print(f"Current Move: {fighter.current_move} ({fighter.moves[str(fighter.current_move)]['name']}, dmg: {fighter.moves[str(fighter.current_move)]['damage']})")
            print(f"HP: {fighter.hp}")
            print(f"Next Move: {fighter.next_moves}")
            print(f"-----------")

            target = fighter_list[1] if index == 0 else fighter_list[0]
            move = fighter.moves.get(str(fighter.current_move))
            resolve_damage(move, target)

            # Randomly choose a new move and update the moveset
            fighter.current_move = fighter.randomly_select_next_move()
            fighter.update_next_moves()

def main():
    fighters = choose_fighters()
    # list_fighter_moves(fighters[0])
    # list_fighter_moves(fighters[1])

    fighter1 = create_fighter(fighters[0])
    fighter2 = create_fighter(fighters[1])
    fighter_list = [fighter1, fighter2]

    # List fighters if you want.
    # list_fighter_stats(fighter_list)

    battle(fighter_list)



if __name__ == "__main__":
    main()
