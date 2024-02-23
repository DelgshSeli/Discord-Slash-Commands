import json

# Load user groups from the JSON file
def load_user_groups():
    try:
        with open("user_groups.json", "r") as file:
            user_groups = json.load(file)
    except FileNotFoundError:
        user_groups = {"admins": [], "vips": []}

    return user_groups




