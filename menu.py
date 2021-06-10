# File:        menu.py
# Authors:     Bhavyai Gupta, Brandon Attai
# Description: Source Code to display the menu for the Project

import ansi_colors as color
from custom_errors import ValueOutOfRange
import os


def splash_message():
    """
    Function to display the welcome message to the program, and opens up the VT mode
    by bug (https://bugs.python.org/issue30075) for windows default console for ANSI
    sequence to work. This function intends to be run only once at program startup.

        Parameters:
            none

        Returns:
            None
    """
    os.system("")

    print(color.magenta)
    print("---------------------------------------------------")
    print(" Welcome to UN Population and Education Statistics")
    print("---------------------------------------------------")
    print(color.reset, end="")


def clear_console():
    """Function to clear the console

        Parameters:
            none

        Returns:
            None
    """
    print("\033\143")


def program_menu():
    """
    Function to control the flow the whole program by displaying the menu
    and navigation throughtout according to the user input

        Parameters:
            none

        Returns:
            None
    """
    print("\n" + color.yellow + "Program menu" + color.reset + "\n")
    print("[1] Print stats for relation between Life Expectancy and Urbanization")
    print("[2] Print stats for relation between Tertiary Education in all countries")
    print("[3] Print stats for relation between Fertility and Literacy")
    print("[4] Print stats for relation between Urbanization and Fertility")
    print("[0] Exit")

    while(True):
        try:
            choice = int(input("\nPlease enter the menu option number (1-4 or 0): "))

            if choice == 0:
                return

            elif choice == 1:
                # call function for stats for Life Expectancy and Urbanization
                pass

            elif choice == 2:
                # # call function for stats for Tertiary Education
                pass

            elif choice == 3:
                # call function for stats for Fertility and Literacy
                pass

            elif choice == 4:
                # call function for Urbanization and Fertility
                pass

            else: # choice < 0 or choice > 4:
                raise ValueOutOfRange("This option is not supported. Please choose a valid menu option")

        except ValueError as e:
            print("\n" + color.red + "Please enter a valid menu option" + color.reset)

        except ValueOutOfRange as e:
            print("\n" + color.red + str(e) + color.reset)



if __name__ == '__main__':
    clear_console()
    splash_message()
    program_menu()