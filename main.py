from bin import controller


def main():
    print("SimpleCalc --- A program that handles basic calculator functions")
    simple_calc = controller.Controller()
    # Starts main loop
    simple_calc.window.mainloop()
    print("Thanks for using SimpleCalc!")


if __name__ == '__main__':
    main()
