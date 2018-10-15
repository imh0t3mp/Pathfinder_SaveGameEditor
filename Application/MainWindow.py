# Title:            MainWindow Class
# Description:      Class for the application main window
# Author:           Tobias Menzel
# Date:             14.10.2018
# Version:          0.1
# Language:         Python 3.7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import modules for the MainWindow class.
import tkinter as tk
from tkinter.filedialog import askopenfilename


# Define class for the main window.


class MainWindow(tk.Frame):
    """Class for the application main window"""
    # Initialize.
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # # # # # # # #
        #   MENU      #
        # # # # # # # #

        # Initialize menu & config.
        self.menu = tk.Menu(master)
        self.master.config(menu=self.menu)

        # Add Menus.
        self.filemenu = tk.Menu(self.menu)
        self.helpmenu = tk.Menu(self.menu)

        # Add options for the menus.
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)

        # Add actions for the filemenu.
        self.filemenu.add_command(label='Open', command=self.on_open_file)
        self.filemenu.add_command(label='Save')
        self.filemenu.add_command(label='Quit', command=master.destroy)

        # Add actions for the helpmenu.
        self.helpmenu.add_command(label='Readme')
        self.helpmenu.add_command(label='About')

        # # # # # # # #
        #   MENU END  #
        # # # # # # # #

        # # # # # # # # # # #
        # CONTROL ELEMENTS  #
        # # # # # # # # # # #

        # Add button action load file.
        self.btn_load_file = tk.Button(self, command=self.on_open_file)
        self.btn_load_file['text'] = 'Load file'
        self.btn_load_file.pack(side='top')

        # Add button action quit application.
        self.btn_quit = tk.Button(self, fg='red', command=master.destroy)
        self.btn_quit['text'] = 'Quit Program'
        self.btn_quit.pack(side='bottom')

        # Add button action save file.
        self.btn_save_file = tk.Button(self)
        self.btn_save_file['text'] = 'Save file'
        self.btn_save_file.pack(side='top')

    # Define static methods.
    @staticmethod
    def on_open_file():
        """Opens a file dialog"""
        file = askopenfilename()
        print("Your choosen file: {file}".format(file=file))  # Test Test Test

