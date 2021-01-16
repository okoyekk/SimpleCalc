import math

class Calculator:
    def __init__(self, window_object):
        self.name = "test"
        self.number_pressed = None
        self.controller = window_object

    def insert_number(self, number):
        self.number_pressed = int(number)
        self.controller.test_print(self.number_pressed)

    def add(self):
        print("add")

    def subtract(self):
        print("subtract")

    def divide(self):
        print("divide")

    def multiply(self):
        print("multiply")

    def find_square_root(self):
        print("find_square_root")

    def find_square(self):
        print("find_square")

    def find_percentage(self):
        print("find_percentage")

    def find_reciprocal(self):
        print("find_reciprocal")

    def clear(self):
        print("clear")

    def clear_entry(self):
        print("clear_entry")

    def delete(self):
        print("delete")

    def calculate(self):
        print("calculate")

    def point(self):
        print("point")

    def flip_sign(self):
        print("flip sign")
