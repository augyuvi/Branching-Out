"""Filter users CLI tool (step 2: name filter only)."""

import json


def load_users():
    """Load user data from users.json."""
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name):
    """Return users matching name (case-insensitive)."""
    users = load_users()
    return [u for u in users if u["name"].lower() == name.lower()]


def main():
    """Ask user for filter option and print results (name only in this step)."""
    option = input("Filter by (name): ").strip().lower()

    if option != "name":
        print("Filtering by that option is not yet supported.")
        return

    name_to_search = input("Enter a name to filter users: ").strip()
    results = filter_users_by_name(name_to_search)

    if results:
        for user in results:
            print(user)
    else:
        print("No users found.")


if __name__ == "__main__":
    main()
