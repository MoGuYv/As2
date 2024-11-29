from placecollection import PlaceCollection
from place import Place


def display_menu():
    """Display the main menu for user selection."""
    print("\nMenu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("S - Sort places")
    print("Q - Quit")


def list_places(collection: PlaceCollection):
    """List all current places, including their visited status."""
    if not collection.places:
        print("No places in the list.")
    else:
        for i, place in enumerate(collection.places, 1):
            visited_status = "v" if place.visited else " "
            print(f"{i}. {visited_status} {place}")


def add_place(collection: PlaceCollection):
    """Add a new place to the list."""
    name = input("Name: ").strip()
    while not name:
        print("Name cannot be blank.")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Country cannot be blank.")
        country = input("Country: ").strip()

    priority_input = input("Priority: ").strip()
    while not priority_input.isdigit() or int(priority_input) < 1:
        if not priority_input.isdigit():
            print("Please enter a valid number for priority.")
        elif int(priority_input) < 1:
            print("Priority must be > 0.")
        priority_input = input("Priority: ").strip()

    priority = int(priority_input)
    new_place = Place(name, country, priority, False)
    collection.add_place(new_place)
    print(f"{new_place} added to the list.")


def mark_place_visited(collection: PlaceCollection):
    """Mark the user-selected place as visited."""
    if collection.get_unvisited_count() == 0:
        print("No unvisited places.")
        return

    list_places(collection)
    user_input = input("Enter the number of a place to mark as visited: ").strip()
    valid_input = False
    while not valid_input:
        if user_input.isdigit() and 1 <= int(user_input) <= len(collection.places):
            valid_input = True
        else:
            print("Please enter a valid number.")
            user_input = input("Enter the number of a place to mark as visited: ").strip()

    choice = int(user_input)
    place = collection.places[choice - 1]
    if place.visited:
        print(f"{place.name} has already been visited.")
    else:
        place.mark_visited()
        print(f"You visited {place.name}. Great travelling!")


def sort_places(collection: PlaceCollection):
    """Sort places by a user-specified attribute."""
    valid_keys = ["name", "country", "priority"]
    key = input("Sort by (name/country/priority): ").strip().lower()
    while key not in valid_keys:
        print("Invalid sort key. Please choose name, country, or priority.")
        key = input("Sort by (name/country/priority): ").strip().lower()
    collection.sort(key)
    print(f"Places sorted by {key}.")


def main():
    """Main program to control the console menu loop."""
    collection = PlaceCollection()
    collection.load_places("places.json")
    print("Travel Tracker 2.0 - by LuJunwen")

    menu_choice = ""
    while menu_choice != "Q":
        display_menu()
        menu_choice = input(">>> ").strip().upper()

        if menu_choice == "L":
            list_places(collection)
        elif menu_choice == "A":
            add_place(collection)
        elif menu_choice == "M":
            mark_place_visited(collection)
        elif menu_choice == "S":
            sort_places(collection)
        elif menu_choice == "Q":
            collection.save_places("places.json")
            print("Places saved. Goodbye!")
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
