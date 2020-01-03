import tkinter as tk
from tkinter import filedialog

from user_interface.home_screen import HomeScreen
from user_interface.blank_availability_screen import BlankAvailabilityScreen
from user_interface.blank_roster_screen import BlankRosterScreen
from user_interface.allocate_crews_screen import AllocateCrewsScreen
from user_interface.individual_rosters_screen import IndividualRostersScreen
from user_interface.master_availability_screen import MasterAvailabilityScreen
from user_interface.error_screen import ErrorScreen

class App(tk.Tk):
    """
    Overall container for app
    Individual screens are raised within this container
    """

    def __init__(self):
        """
        Initialise the class
        """
        tk.Tk.__init__(self)

        self.title('WLLR footplate crew rostering program')
        self.geometry('850x600+250+100')
        self.frame_names_list = (HomeScreen,BlankAvailabilityScreen,BlankRosterScreen,AllocateCrewsScreen,MasterAvailabilityScreen,IndividualRostersScreen,ErrorScreen)
        self.frames = {}
        self.background_col = 'black'
        self.foreground_col = 'white'
        self.font = 'courier 11'

        # the container holds the stack of frames on top of each other. The one to be visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create each frame instance and add to self.frames dictionary
        for frame_name in self.frame_names_list:
            page_name = frame_name.__name__
            frame_object = frame_name(parent=container, controller=self, background_col = self.background_col, foreground_col = self.foreground_col, font = self.font)
            self.frames[page_name] = frame_object
            frame_object.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomeScreen.__name__)

    def show_frame(self, page_name):
        """
        Show a frame for the given page_name
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def browse_file(self, entry):
        """
        Browse the file system
        """
        file_path = filedialog.askopenfilename(title='Choose a file')
        if file_path != None:
            entry.delete(0, 'end')
            entry.insert(0, file_path)

    def browse_directory(self, entry):
        """
        Browse the file system and select a directory
        """
        dir_path = filedialog.askdirectory(title='Choose a folder location')
        if dir_path != None:
            entry.delete(0, 'end')
            entry.insert(0, dir_path)