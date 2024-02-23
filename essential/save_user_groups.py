import json

# Save user groups to the JSON file
def save_user_groups(user_groups):
    with open("user_groups.json", "w") as file:
        json.dump(user_groups, file, indent=2)
