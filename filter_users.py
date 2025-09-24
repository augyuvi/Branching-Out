"""Filter users CLI tool (step 4: name + age + email)."""

import json


def load_users():
    """Load user data from users.json."""
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name):
    """Return users matching name (case-insensitive)."""
    users = load_users()
    return [u for u in users if u["name"].lower() == name.lower()]


def filter_users_by_age(age):
    """Return users matching age (exact integer)."""
    users = load_users()
    return [u for u in users if u["age"] == age]


def filter_users_by_email(email):
    """Return users matching email (case-insensitive)."""
    users = load_users()
    return [u for u in users if u["email"].lower() == email.lower()]


def main():
    """
    Ask user for filter option and print results.
    Supports: name / age / email.
    """
    option = input("Filter by (name/age/email): ").strip().lower()

    if option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        results = filter_users_by_name(name_to_search)

    elif option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
        except ValueError:
            print("Please enter a valid number for age.")
            return
        results = filter_users_by_age(age_to_search)

    elif option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        results = filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
        return

    if results:
        for user in results:
            print(user)
    else:
        print("No users found.")


if __name__ == "__main__":
    main()
