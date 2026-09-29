# Campus Lost & Found Management System
lost_items = []
found_items = []

def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty. Please try again.")


def get_date(message):
    while True:
        date = input(message).strip()
        parts = date.split("-")

        if len(parts) == 3:
            if all(part.isdigit() for part in parts):
                if len(parts[0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4:
                    return date

        print("Please enter the date in DD-MM-YYYY format.")

def report_lost_item():
    print("\n========== REPORT LOST ITEM ==========")

    item = {
        "id": len(lost_items) + 1,
        "name": get_non_empty_input("Item name: "),
        "category": get_non_empty_input("Category: "),
        "colour": get_non_empty_input("Colour: "),
        "location": get_non_empty_input("Location lost: "),
        "date": get_date("Date lost (DD-MM-YYYY): "),
        "description": get_non_empty_input("Description: "),
        "status": "Lost"
    }

    lost_items.append(item)

    print("\nLost item reported successfully.")
    print("Lost Item ID:", item["id"])

def report_found_item():
    print("\n========== REPORT FOUND ITEM ==========")

    item = {
        "id": len(found_items) + 1,
        "name": get_non_empty_input("Item name: "),
        "category": get_non_empty_input("Category: "),
        "colour": get_non_empty_input("Colour: "),
        "location": get_non_empty_input("Location found: "),
        "date": get_date("Date found (DD-MM-YYYY): "),
        "description": get_non_empty_input("Description: "),
        "status": "Found"
    }

    found_items.append(item)

    print("\nFound item reported successfully.")
    print("Found Item ID:", item["id"])

def display_item(item):
    print("-" * 40)
    print("ID          :", item["id"])
    print("Item        :", item["name"])
    print("Category    :", item["category"])
    print("Colour      :", item["colour"])
    print("Location    :", item["location"])
    print("Date        :", item["date"])
    print("Description :", item["description"])
    print("Status      :", item["status"])
    print("-" * 40)


def view_all_items():
    print("\n========== ALL LOST ITEMS ==========")

    if len(lost_items) == 0:
        print("No lost items have been reported.")
    else:
        for item in lost_items:
            display_item(item)

    print("\n========== ALL FOUND ITEMS ==========")

    if len(found_items) == 0:
        print("No found items have been reported.")
    else:
        for item in found_items:
            display_item(item)

def search_items():
    print("\n========== SEARCH ITEMS ==========")

    keyword = get_non_empty_input(
        "Enter item name, category, colour or location: "
    ).lower()

    results = []

    for item in lost_items + found_items:
        if (
            keyword in item["name"].lower()
            or keyword in item["category"].lower()
            or keyword in item["colour"].lower()
            or keyword in item["location"].lower()
        ):
            results.append(item)

    if len(results) == 0:
        print("\nNo matching items found.")
    else:
        print("\nMatching items:")

        for item in results:
            display_item(item)
def calculate_match_score(lost, found):
    score = 0
    if lost["name"].lower() == found["name"].lower():
        score += 2
    if lost["category"].lower() == found["category"].lower():
        score += 2
    if lost["colour"].lower() == found["colour"].lower():
        score += 1
    if lost["location"].lower() == found["location"].lower():
        score += 2
    lost_words = lost["description"].lower().split()
    found_words = found["description"].lower().split()

    for word in lost_words:
        if word in found_words:
            score += 1
            break

    return score


def find_possible_match():
    print("\n========== FIND POSSIBLE MATCH ==========")

    if len(lost_items) == 0:
        print("No lost items available.")
        return

    if len(found_items) == 0:
        print("No found items available.")
        return

    print("\nLost Items:")

    for item in lost_items:
        print(
            item["id"],
            "-",
            item["name"],
            "|",
            item["colour"],
            "|",
            item["location"]
        )

    try:
        lost_id = int(input("\nEnter Lost Item ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    selected_lost = None

    for item in lost_items:
        if item["id"] == lost_id:
            selected_lost = item
            break

    if selected_lost is None:
        print("Lost item not found.")
        return

    matches = []

    for found in found_items:
        score = calculate_match_score(selected_lost, found)

        if score >= 4:
            matches.append((found, score))

    if len(matches) == 0:
        print("\nNo possible matches found.")
        return

    matches.sort(key=lambda x: x[1], reverse=True)

    print("\n========== POSSIBLE MATCHES ==========")

    for found, score in matches:
        print("\nMatch Score:", score, "/ 8")

        if score >= 7:
            print("Match Level: HIGH")
        elif score >= 5:
            print("Match Level: MEDIUM")
        else:
            print("Match Level: LOW")

        display_item(found)

def update_item_status():
    print("\n========== UPDATE ITEM STATUS ==========")

    print("1. Update Lost Item")
    print("2. Update Found Item")

    choice = input("Enter your choice: ")

    if choice == "1":
        items = lost_items
    elif choice == "2":
        items = found_items
    else:
        print("Invalid choice.")
        return

    if len(items) == 0:
        print("No items available.")
        return

    try:
        item_id = int(input("Enter Item ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for item in items:
        if item["id"] == item_id:

            print("\nCurrent status:", item["status"])

            print("\nAvailable statuses:")
            print("1. Lost")
            print("2. Found")
            print("3. Matched")
            print("4. Claimed")

            status_choice = input("Choose new status: ")

            if status_choice == "1":
                item["status"] = "Lost"
            elif status_choice == "2":
                item["status"] = "Found"
            elif status_choice == "3":
                item["status"] = "Matched"
            elif status_choice == "4":
                item["status"] = "Claimed"
            else:
                print("Invalid status.")
                return

            print("Status updated successfully.")
            return

    print("Item ID not found.")

def main():
    while True:

        print("\n")
        print("=" * 50)
        print("       CAMPUS LOST & FOUND SYSTEM")
        print("=" * 50)

        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. Search Items")
        print("4. Find Possible Match")
        print("5. View All Items")
        print("6. Update Item Status")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            report_lost_item()

        elif choice == "2":
            report_found_item()

        elif choice == "3":
            search_items()

        elif choice == "4":
            find_possible_match()

        elif choice == "5":
            view_all_items()

        elif choice == "6":
            update_item_status()

        elif choice == "7":
            print("\nThank you for using the Campus Lost & Found System.")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
