class Calculator:
    def __init__(self, window_object):
        self.controller = window_object
        self.functions = {"square_root": "** (1/2)", "square": "** (2)", "percent": "/ (100)",
                          "reciprocal": "** (-1)", "point": ".", "neg": "* -1"}
        self.total = 0

    def insert_number(self, number):
        number_pressed = int(number)
        self.controller.update_input(number_pressed)

    def insert_operation(self, operation):
        if len(self.controller.input_text) != 0:
            self.controller.update_input(operation)

    def find_square_root(self):
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["square_root"])

    def find_square(self):
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["square"])

    def find_percentage(self):
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["percent"])

    def find_reciprocal(self):
        if len(self.controller.input_text) != 0:
            self.controller.update_input(self.functions["reciprocal"])

    def point(self):
        if len(self.controller.input_text) == 0:
            self.controller.update_input("0" + self.functions["point"])
        else:
            self.controller.update_input(self.functions["point"])

    def flip_sign(self):
        if len(self.controller.input_text) == 0:
            self.controller.update_input("-")
        else:
            self.controller.update_input(self.functions["neg"])

    def clear(self):
        self.controller.input_text = ""
        self.controller.input.set(self.controller.input_text)
        self.total = 0

    def clear_entry(self):
        self.controller.input_text = str(self.total)
        self.controller.input.set(self.controller.input_text)

    def delete(self):
        new_input = self.controller.input_text[0:-1]
        self.controller.set_input(new_input)

    def calculate(self):
        # self.controller.throw_error(message="Cant divide by 0")
        try:
            self.total = eval(self.controller.input_text.strip())
            self.controller.set_input(self.total)
        except ZeroDivisionError:
            self.controller.throw_error("Can't Divide By 0! please revise input")
        except SyntaxError:
            self.controller.throw_error("Bad syntax! Please revise input")
