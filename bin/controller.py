import tkinter as tk
from tkinter import ttk
from bin import calculator


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.calculator = calculator.Calculator()
        # self.button_labels is a dictionary mapping each button name to its position:tuple
        # All position tuples are in the form of (column, row)
        self.button_labels = {"%": (1, 1), "CE": (2, 1), "C": (3, 1), "del": (4, 1),
                              "1/x": (1, 2), "SQR": (2, 2), "SQRT": (3, 2), "/": (4, 2),
                              "7": (1, 3), "8": (2, 3), "9": (3, 3), "*": (4, 3),
                              "4": (1, 4), "5": (2, 4), "6": (3, 4), "-": (4, 4),
                              "1": (1, 5), "2": (2, 5), "3": (3, 5), "+": (4, 5),
                              "+/-": (1, 6), "0": (2, 6), ".": (3, 6), "=": (4, 6)}
        # self.button_functions is a dictionary mapping each button name to a function of the Calculator class
        self.button_functions = {"%": self.calculator.find_percentage, "CE": self.calculator.clear_entry,
                                 "C": self.calculator.clear, "del": self.calculator.delete,
                                 "1/x": self.calculator.find_reciprocal, "SQR": self.calculator.find_square,
                                 "SQRT": self.calculator.find_square_root, "/": self.calculator.divide,
                                 "7": self.calculator.insert_number, "8": self.calculator.insert_number,
                                 "9": self.calculator.insert_number, "*": self.calculator.multiply,
                                 "4": self.calculator.insert_number, "5": self.calculator.insert_number,
                                 "6": self.calculator.insert_number, "-": self.calculator.subtract,
                                 "1": self.calculator.insert_number, "2": self.calculator.insert_number,
                                 "3": self.calculator.insert_number, "+": self.calculator.add,
                                 "+/-": self.calculator.flip_sign, "0": self.calculator.insert_number,
                                 ".": self.calculator.point, "=": self.calculator.calculate}
        self.input_bar = None

        self.create_window()
        self.root.mainloop()

    def create_window(self):
        self.root.winfo_toplevel().title("SimpleCalc")
        input_frame = self.create_frame((1, 1))
        number_frame = self.create_frame((1, 2))
        # Create input_bar
        input_bar = ttk.Entry(input_frame)
        input_bar.grid(row=0, column=0)
        self.create_buttons(number_frame)

    # noinspection PyArgumentList
    def create_buttons(self, parent):
        for label, position in self.button_labels.items():
            # Maps a different command to each button, if the button is a number, it passes the number to the
            # calculator class function as an argument, else it makes a regular function button
            if label.isnumeric():
                button_1 = tk.Button(parent, text=label, command=lambda x=label: self.button_functions[x](x),
                                     height=3, width=8)
            else:
                button_1 = tk.Button(parent, text=label, command=self.button_functions[label], height=3, width=8)
            button_1.grid(row=position[1], column=position[0], padx=(1, 1), pady=(1, 1))

    def create_frame(self, position: tuple):
        new_frame = ttk.Frame(self.root, relief=tk.RIDGE).grid(row=position[1], column=position[0])
        return new_frame
