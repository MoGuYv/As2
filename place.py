class Place:
    """Class to represent a place with name, country, priority, and visited status."""

    def __init__(self, name: str, country: str, priority: int, visited: bool = False):
        """Initialize a Place object with name, country, priority, and visited status."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self) -> str:
        """Return a string representation of the Place."""
        status = "visited" if self.visited else "not visited"
        return f"{self.name} in {self.country}, priority {self.priority}, {status}"

    def mark_visited(self):
        """Mark the place as visited."""
        self.visited = True

    def mark_unvisited(self):
        """Mark the place as not visited."""
        self.visited = False

    def is_important(self) -> bool:
        """Return True if the place is considered important (priority <= 2)."""
        return self.priority <= 2
