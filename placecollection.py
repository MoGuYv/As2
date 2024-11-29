import json
from operator import attrgetter
from place import Place


class PlaceCollection:
    """Class to manage a collection of Place objects."""

    def __init__(self):
        """Initialize a PlaceCollection with an empty list."""
        self.places = []

    def load_places(self, filename: str):
        """Load places from a JSON file into the places list."""
        with open(filename, 'r') as file:
            data = json.load(file)
            self.places = [
                Place(place['name'], place['country'], place['priority'], place['visited'])
                for place in data
            ]

    def save_places(self, filename: str):
        """Save the places list to a JSON file."""
        with open(filename, 'w') as file:
            data = [
                {
                    'name': place.name,
                    'country': place.country,
                    'priority': place.priority,
                    'visited': place.visited,
                }
                for place in self.places
            ]
            json.dump(data, file, indent=4)

    def add_place(self, place: Place):
        """Add a new Place object to the collection."""
        self.places.append(place)

    def get_unvisited_count(self) -> int:
        """Return the number of unvisited places."""
        return sum(not place.visited for place in self.places)

    def sort(self, key: str):
        """Sort places by the specified key and then by priority."""
        self.places.sort(key=attrgetter(key, 'priority'))
