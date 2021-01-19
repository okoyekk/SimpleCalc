class Calculator:
    def __init__(self, window_object):
        """
        Description: Initializes the Calculator class with the controller window object, a dictionary holding
                     function mappings for some operations and sets the running total of calculations (self.total) to 0
        parameters: self, window_object
        returns: None
        """
        self.controller = window_object
        self.functions = {"square_root": "** (1/2)", "square": "** (2)", "percent": "/ (100)",
                          "reciprocal": "** (-1)", "point": ".", "neg": "* -1"}
        self.total = 0

    def insert_number(self, number):
        """
        Description: Inserts a number to the input label in the controller window
        parameters: self, number
        returns: None
        """
        number_pressed = int(number)
        self.controller.update_input(number_pressed)

    def insert_operation(self, operation):
        """
        Description: Inserts an operation to the input label in the controller window
        parameters: self, operation
        returns: None
        """
        if len(self.controller.input_text) != 0:
            self.controller.update_input(operation)

    def find_square_root(self):
        """
        Description: Inserts the square root operation to the input label in the controller window
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["square_root"])

    def find_square(self):
        """
        Description: Inserts the square operation to the input label in the controller window
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["square"])

    def find_percentage(self):
        """
        Description: Inserts the percentage operation to the input label in the controller window
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["percent"])

    def find_reciprocal(self):
        """
        Description: Inserts the reciprocal operation to the input label in the controller window
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["reciprocal"])

    def point(self):
        """
        Description: Inserts the point(".") to the input label in the controller window, its action depends on the
                     label length (to avoid errors)
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) == 0:
            self.controller.update_input("0" + self.functions["point"])
        else:
            self.controller.update_input(self.functions["point"])

    def flip_sign(self):
        """
        Description: Multiplies a number by (-1) or inserts the (-) operator, based on the length of the label
        parameters: self
        returns: None
        """
        if len(self.controller.input_text) == 0:
            self.controller.update_input("-")
        else:
            self.controller.update_input(self.functions["neg"])

    def clear(self):
        """
        Description: Clears the Label and sets the total to 0
        parameters: self
        returns: None
        """
        self.controller.input_text = ""
        self.controller.input.set(self.controller.input_text)
        self.total = 0

    def clear_entry(self):
        """
        Description: Replaces the current label text with the last result OR sets it to the default value (0)
        parameters: self
        returns: None
        """
        self.controller.input_text = str(self.total)
        self.controller.input.set(self.controller.input_text)

    def delete(self):
        """
        Description: Deletes the last entered character in the label, by setting the input label to the previous
                     sliced input label
        parameters: self
        returns: None
        """
        new_input = self.controller.input_text[0:-1]
        self.controller.set_input(new_input)

    def calculate(self):
        """
        Description: Calculates the result of the users input on the input label, using the python builtin eval()
                     function and updates the label to that. Efficiently handles errors and displays them to the user
                     for correction
        parameters: self
        returns: None
        """
        # self.controller.throw_error(message="Cant divide by 0")
        try:
            self.total = eval(self.controller.input_text.strip())
            self.controller.set_input(self.total)
        except ZeroDivisionError:
            self.controller.throw_error("Can't Divide By 0! please revise input")
        except SyntaxError:
            self.controller.throw_error("Bad syntax! Please revise input")
