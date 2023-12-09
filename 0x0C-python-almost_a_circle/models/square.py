#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                match i:
                    case 0:
                        if args[i] is None:
                            self.__init__(self.size,
                                          self.x, self,y)
                        else:
                            self.id = args[i]
                    case 1:
                        self.size = args[i]
                    case 2:
                        self.x = args[i]
                    case 3:
                        self.y = args[i]

        elif kwargs and len(kwargs) != 0:
            for key,value in kwargs.items():
                if key == "id" and value == None:
                    self.__init__(self.size, self.x, self.y)
                elif key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                         self.y, self.width)
