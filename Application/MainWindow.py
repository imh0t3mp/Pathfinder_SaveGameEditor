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

        # Add button action load file.
        self.btn_load_savefile = tk.Button(self)
        self.btn_load_savefile['text'] = 'Load save'
        self.btn_load_savefile.pack(side='top')

        # Add button action quit application.
        self.btn_quit = tk.Button(self, fg='red', command=master.destroy)
        self.btn_quit['text'] = 'Quit Program'
        self.btn_quit.pack(side='bottom')
