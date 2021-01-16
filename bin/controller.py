import tkinter as tk
from tkinter import ttk
from bin import calculator


class Controller:
    def __init__(self):
        self.window = tk.Tk()
        self.calculator = calculator.Calculator(self)
        # self.button_labels is a dictionary mapping each button name to its position:tuple
        # All position tuples are in the form of (column, row)
        self.button_labels = {"%": (0, 1), "CE": (1, 1), "C": (2, 1), "del": (3, 1),
                              "1/x": (0, 2), "SQR": (1, 2), "SQRT": (2, 2), "/": (3, 2),
                              "7": (0, 3), "8": (1, 3), "9": (2, 3), "*": (3, 3),
                              "4": (0, 4), "5": (1, 4), "6": (2, 4), "-": (3, 4),
                              "1": (0, 5), "2": (1, 5), "3": (2, 5), "+": (3, 5),
                              "+/-": (0, 6), "0": (1, 6), ".": (2, 6), "=": (3, 6)}
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
        self.input = tk.StringVar()
        self.input_text = ""
        self.input.set(self.input_text)

        self.root = ttk.Frame(self.window, relief=tk.RIDGE)
        self.root.pack()
        self.create_window()
        self.window.mainloop()

    def create_window(self):
        # self.window.resizable(False, False)
        self.window.winfo_toplevel().title("SimpleCalc")
        # update input_bar
        self.input_bar = ttk.Label(self.root, textvariable=self.input, anchor="e", width=32)
        self.input_bar.grid(row=0, column=0, columnspan=4, sticky=(tk.N, tk.E, tk.W))
        self.create_buttons(self.root)

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
            button_1.grid(row=position[1], column=position[0])

    def test_print(self, word):
        print("test -- ", word)
        self.input_text += str(word)
        self.input.set(self.input_text)
