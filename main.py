from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from placecollection import PlaceCollection
from place import Place


class TravelTrackerApp(App):
    """Main app for Travel Tracker."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.place_collection.load_places("places.json")
        self.title = "Travel Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.create_place_buttons()
        self.update_status_bar()
        return self.root

    def create_place_buttons(self):
        """Create buttons for each place."""
        self.root.ids.place_buttons.clear_widgets()
        for place in self.place_collection.places:
            button = Button(
                text=str(place),
                background_color=(0, 1, 0, 1) if place.visited else (1, 0, 0, 1),
                on_release=lambda btn: self.toggle_visited(btn.text)
            )
            self.root.ids.place_buttons.add_widget(button)

    def toggle_visited(self, place_text):
        """Toggle the visited status of a place."""
        for place in self.place_collection.places:
            if str(place) == place_text:
                if place.visited:
                    place.mark_unvisited()
                    self.root.ids.status_bar.text = f"You need to visit {place.name}."
                else:
                    place.mark_visited()
                    self.root.ids.status_bar.text = f"You visited {place.name}. Great travelling!"
                self.create_place_buttons()
                self.update_status_bar()
                return

    def add_place(self):
        """Add a new place to the collection."""
        name = self.root.ids.input_name.text.strip()
        country = self.root.ids.input_country.text.strip()
        priority_text = self.root.ids.input_priority.text.strip()

        if not name or not country or not priority_text:
            self.root.ids.status_bar.text = "All fields must be completed."
            return

        if not priority_text.isdigit() or int(priority_text) < 1:
            self.root.ids.status_bar.text = "Please enter a valid positive number for priority."
            return

        priority = int(priority_text)
        new_place = Place(name, country, priority, False)
        self.place_collection.add_place(new_place)
        self.create_place_buttons()
        self.update_status_bar()
        self.clear_inputs()
        self.root.ids.status_bar.text = f"{name} in {country} added to the list."

    def clear_inputs(self):
        """Clear the input fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def update_status_bar(self):
        """Update the status bar with the number of unvisited places."""
        unvisited_count = self.place_collection.get_unvisited_count()
        self.root.ids.status_bar.text = f"Places to visit: {unvisited_count}"

    def on_stop(self):
        """Save places to JSON file when the app closes."""
        self.place_collection.save_places("places.json")
