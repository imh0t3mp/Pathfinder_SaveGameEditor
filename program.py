# Title:            Pathfinder Kingmaker - Savegame Editor
# Description:      Savegame Editor to edit character attributes.
# Author:           Tobias Menzel
# Date:             14.10.2018
# Version:          0.1
# Language:         Python 3.7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import modules.
import tkinter as tk
from Application.MainWindow import MainWindow


# # # # # # # # # # # #
#  MAIN APPLICATION   #
# # # # # # # # # # # #

# Define main application function.


def main():
    """Start main application window"""
    # Define root as Tk-Application object.
    root = tk.Tk()

    # Define app as Application object.
    app = MainWindow(master=root)


# Define entry point.
if __name__ == '__main__':
    main()
