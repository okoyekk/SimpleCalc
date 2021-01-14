import tkinter as tk
from tkinter import ttk
from bin import calculator


class Controller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.calculator = calculator.Calculator()
        # self.button_labels is a dictionary mapping each button name to its position:tuple
        self.button_labels = {"%": (1, 1), "CE": (2, 1), "C": (3, 1), "del": (4, 1),
                              "1/x": (1, 2), "SQR": (2, 2), "SQRT": (3, 2), "/": (4, 2),
                              "7": (1, 3), "8": (2, 3), "9": (3, 3), "*": (4, 3),
                              "4": (1, 4), "5": (2, 4), "6": (3, 4), "-": (4, 4),
                              "1": (1, 5), "2": (2, 5), "3": (3, 5), "+": (4, 5),
                              "neg": (1, 6), "0": (2, 6), ".": (3, 6), "=": (4, 6)}
        # TODO make a dictionary mapping each button to its function name
        self.create_window()
        self.window.mainloop()

    def create_window(self):
        root = ttk.Frame(self.window).grid(column=1, row=1)
        number_frame = ttk.Frame(root, relief=tk.RIDGE).grid(row=1, column=1)
        self.create_buttons(number_frame)

    def create_buttons(self, parent):
        for label, position in self.button_labels.items():
            button_1 = ttk.Button(parent, text=label)
            button_1.grid(row=position[1], column=position[0])

    def create_frame(self, parent, position: tuple):
        pass
