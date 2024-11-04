import json

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

        config_values = {
            'default_fighter_1': config['default_fighter_1'],
            'default_fighter_2': config['default_fighter_2'],
            'number_of_battles': config['number_of_battles'],
            'display_battle_log': config['display_battle_log']
        }
        return config_values

    except FileNotFoundError:
        print("Error: config.json file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
    except KeyError as e:
        print(f"Error: Missing key in config: {e}")

