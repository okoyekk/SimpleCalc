import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from bin import calculator


class Controller:
    def __init__(self):
        """
        Description: Initializes the Controller class with instance variables and methods
        parameters: self
        returns: None
        """
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
                                 "SQRT": self.calculator.find_square_root, "/": self.calculator.insert_operation,
                                 "7": self.calculator.insert_number, "8": self.calculator.insert_number,
                                 "9": self.calculator.insert_number, "*": self.calculator.insert_operation,
                                 "4": self.calculator.insert_number, "5": self.calculator.insert_number,
                                 "6": self.calculator.insert_number, "-": self.calculator.insert_operation,
                                 "1": self.calculator.insert_number, "2": self.calculator.insert_number,
                                 "3": self.calculator.insert_number, "+": self.calculator.insert_operation,
                                 "+/-": self.calculator.flip_sign, "0": self.calculator.insert_number,
                                 ".": self.calculator.point, "=": self.calculator.calculate}
        # Initialized input variables for updating the input label
        self.input_bar = None
        self.input_text = ""
        self.input = tk.StringVar()
        self.input.set(self.input_text)
        # Created a root frame, self.root to house all widgets
        self.root = ttk.Frame(self.window, relief=tk.RIDGE)
        self.root.pack()
        self.create_window()

    def create_window(self):
        """
        Description: Sets up the program's window
        parameters: self
        returns: None
        """
        # convert logo.jpg to a tk PhotoImage
        photo = ImageTk.PhotoImage(Image.open("assets/logo.jpg"))
        # sets the windows icon to photo
        self.window.iconphoto(False, photo)
        # Turns off window resizing
        self.window.resizable(False, False)
        # Sets window title to "SimpleCalc"
        self.window.winfo_toplevel().title("SimpleCalc")
        # Creates, styles and positions the input bar
        self.input_bar = ttk.Label(self.root, textvariable=self.input, anchor="e", width=32, font="Verdana 8 bold")
        self.input_bar.grid(row=0, column=0, columnspan=4, sticky=(tk.N, tk.E, tk.W))
        # Creates all the buttons in the root frame
        self.create_buttons(self.root)

    # noinspection PyArgumentList
    def create_buttons(self, parent):
        """
        Description: Creates and positions all the buttons in the parent window based off self.button_labels dictionary
                     and binds them to functions using the self.button_functions dictionary
        parameters: self, parent(Tk frame object)
        returns: None
        """
        for label, position in self.button_labels.items():
            # Maps a different command to each button, if the button is a number or an operation, it passes the
            # number to the calculator class function as an argument, else it makes a regular function button
            if label.isnumeric():
                button_1 = tk.Button(parent, text=label, command=lambda x=label: self.button_functions[x](x),
                                     height=3, width=8)
            elif label in "+-/*":
                button_1 = tk.Button(parent, text=label, command=lambda x=label: self.button_functions[x](x),
                                     height=3, width=8)
            else:
                button_1 = tk.Button(parent, text=label, command=self.button_functions[label], height=3, width=8)
            # Positions each button using the value of each key in the self.button_labels dictionary
            button_1.grid(row=position[1], column=position[0])

    def update_input(self, key):
        """
        Description: Updates the self.input variable which changes the input label in the application window
        parameters: self, key
        returns: None
        """
        # concatenates key and the self.input_text variable
        self.input_text += str(key)
        self.input.set(self.input_text)

    def set_input(self, key):
        """
        Description: Sets the self.input variable to the key given
        parameters: self, key
        returns: None
        """
        self.input_text = str(key)
        self.input.set(self.input_text)

    @staticmethod
    def throw_error(message):
        """
        Description: Shows a tkinter error messagebox with message when passed
        parameters: message
        returns: None
        """
        messagebox.showerror(title="Error!", message=message)
