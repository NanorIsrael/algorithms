#!/usr/bin/python3
"""Defines a Square class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}"
                .format(type(self).__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        attr = ['id', 'size', 'x', 'y']
        if args:
            i = 0 
            for idx, value in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[idx], value)
                    i += 1
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
    
    def to_dictionary(self):
        return (
            {
                'id': self.id, 'size': self.size, 
                'x': self.x, 'y': self.y
            })