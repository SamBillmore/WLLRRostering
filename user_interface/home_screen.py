from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage

from user_interface.blank_availability_screen import BlankAvailabilityScreen
from user_interface.blank_roster_screen import BlankRosterScreen
from user_interface.allocate_crews_screen import AllocateCrewsScreen
from user_interface.individual_rosters_screen import IndividualRostersScreen
from user_interface.resource_path import ResourcePath

class HomeScreen(Frame,ResourcePath):
    """
    The home screen for the program
    """

    def __init__(self, parent, controller, background_col, foreground_col, font):
        """
        Layout for the home screen
        """
        Frame.__init__(self, parent, bg=background_col)
        self.controller = controller
        self.parent = parent
        self.picture_path = './/user_interface//home_screen_pic.png'

        self.logo = PhotoImage(file=self.resource_path(self.picture_path))

        self.picture = Label (self, image=self.logo)
        self.picture.image = self.logo
        self.intro_label = Label (self, text='Welcome to the WLLR footplate department rostering program!', bg=background_col, fg=foreground_col, font=font)
        self.step_1_label = Label (self, text='Step 1: Set up input files', bg=background_col, fg=foreground_col, font=font)
        self.step_1a_label = Label (self, text='\t(1) timetable dates and colours', bg=background_col, fg=foreground_col, font=font)
        self.step_1b_label = Label (self, text='\t(2) crew requirements for each colour timetable', bg=background_col, fg=foreground_col, font=font)
        self.step_2_label = Label (self, text='Step 2: Create blank availability forms', bg=background_col, fg=foreground_col, font=font)
        self.step_3_label = Label (self, text='Step 3: Create a blank roster', bg=background_col, fg=foreground_col, font=font)
        self.step_4_label = Label (self, text='Step 4: Open blank roster file and enter any specific crew allocations', bg=background_col, fg=foreground_col, font=font)
        self.step_5_label = Label (self, text='Step 5: Allocate crews to remaining turns', bg=background_col, fg=foreground_col, font=font)
        self.step_6_label = Label (self, text='Step 6: Review allocations and amend as necessary', bg=background_col, fg=foreground_col, font=font)
        self.step_7_label = Label (self, text='Step 7: Generate individual rosters', bg=background_col, fg=foreground_col, font=font)

        self.step_2_button = Button (self, text='Blank availability', width=18, command=lambda: controller.show_frame(BlankAvailabilityScreen.__name__))
        self.step_3_button = Button (self, text='Blank roster', width=18, command=lambda: controller.show_frame(BlankRosterScreen.__name__))
        self.step_5_button = Button (self, text='Allocate crews', width=18, command=lambda: controller.show_frame(AllocateCrewsScreen.__name__))
        self.step_7_button = Button (self, text='Individual rosters', width=18, command=lambda: controller.show_frame(IndividualRostersScreen.__name__))
        
        self.picture.grid(row=0, column=0, padx = 5, pady = 5, columnspan=2)
        self.intro_label.grid(row=1, column=0, padx = 25, pady = 15, columnspan=2)
        self.step_1_label.grid(row=2, column=0, sticky='W', padx = 25, pady = 0)
        self.step_1a_label.grid(row=3, column=0, sticky='W', padx = 25, pady = 0)
        self.step_1b_label.grid(row=4, column=0, sticky='W', padx = 25, pady = 0)
        self.step_2_label.grid(row=5, column=0, sticky='W', padx = 25, pady = 15)
        self.step_3_label.grid(row=6, column=0, sticky='W', padx = 25, pady = 10)
        self.step_4_label.grid(row=7, column=0, sticky='W', padx = 25, pady = 10)
        self.step_5_label.grid(row=8, column=0, sticky='W', padx = 25, pady = 10)
        self.step_6_label.grid(row=9, column=0, sticky='W', padx = 25, pady = 10)
        self.step_7_label.grid(row=10, column=0, sticky='W', padx = 25, pady = 10)

        self.step_2_button.grid(row=5,column=1,sticky='W')
        self.step_3_button.grid(row=6,column=1,sticky='W')
        self.step_5_button.grid(row=8,column=1,sticky='W')
        self.step_7_button.grid(row=10,column=1,sticky='W')