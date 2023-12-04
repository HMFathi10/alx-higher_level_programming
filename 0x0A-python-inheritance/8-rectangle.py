#!/usr/bin/python3
"""module subclass rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __inti__(self, width, height):
        """Rectangle that inherits from BaseGeometry"""
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.width = width
        self.height = height
