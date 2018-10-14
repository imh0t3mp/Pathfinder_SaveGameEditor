# Title:            MainWindow Class
# Description:      Class for the application main window
# Author:           Tobias Menzel
# Date:             14.10.2018
# Version:          0.1
# Language:         Python 3.7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import modules for the MainWindow class.
import tkinter as tk


# Define class for the main window.


class MainWindow(tk.Frame):
    """Class for the application main window"""
    # Initialize.
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    # Create widgets for the main window.
    def create_widgets(self):
        pass
