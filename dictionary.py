from spell_checker import spell_checker

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
        Time Complexity: Avg: O(1); Worst: O(n)
        Space Complexity: O(n)

        Args:
            value (str): The object to be strored.
        """
        value = value.lower()
        key = hash(value) % self.size
        # If element is already there, skip
        if value not in self.storage[key]:
            self.storage[key].append(value)
            self.length += 1
    
    def __getitem__(self, value: str) -> str:
        """Search an item in the dictionary.
        Time Complexity: Avg: O(1); Worst: O(n)
        Space Complexity: O(1)
        Args:
            value (str): The item searched for.

        Returns:
            str: The item searched for. Otherwise returns "Not found".
        """
        value = value.lower()
        key = hash(value) % self.size
        if value in self.storage[key]:
            return value
        else:
            return f"'{value}' not found. Did you mean: '{spell_checker(value)}'?"

    def __delitem__(self, value: str) -> None:
        """Delete a value from the dictionary.
        Time Complexity: Avg: O(1); Worst: O(n)
        Space Complexity: O(1)
        Args:
            value (str): The value to be deleted.
        """
        value = value.lower()
        key = hash(value) % self.size
        if value in self.storage[key]:
            self.storage[key].remove(value)
            self.length -= 1
        else:
            print(f'{value} not found.')

    def __len__(self) -> int:
        """Return the number of elements stored.

        Returns:
            int: Number of elements stored.
        """
        return self.length