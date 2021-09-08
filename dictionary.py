from typing import List, Any

class Dictionary():
    """Custom Dictionary implementation
    """
    def __init__(self, size: int=10000) -> None:
        """Store elements inside a list so as to avoid hash collision.

        Args:
            size (int, optional): Number of objects to be stored inside the list.
            Defaults to 10000.
        """

        self.size = size
        self.storage = [[] for _ in range(size)]  # List of lists
        self.length = 0

    def append(self, value: str) -> None:
        """Calculate key using hash, then store the word. 
        If collision arises, append to the list.

        Args:
            value (str): The object to be strored.
        """
        key = hash(value) % self.size
        # If element is already there, skip
        if value not in self.storage[key]:
            self.storage[key].append(value)
    
    def __getitem__(self, value: str) -> str:
        """Search an item in the dictionary.

        Args:
            value (str): The item searched for.

        Returns:
            str: The item searched for. Otherwise returns "Not found".
        """
        key = hash(value) % self.size
        if value in self.storage[key]:
            return value
        else:
            return "Not Found"