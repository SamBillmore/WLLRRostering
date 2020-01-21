import pandas as pd
import os

from import_export.import_export_classes import Data_Imports
from import_export.import_export_classes import Data_Exports

class Individual_Rosters(Data_Imports,Data_Exports):
    """
    Create individual rosters for each crew member
    """

    def __init__(self):
        """
        Initiates the class
        """
        self.data_import = None
        self.expected_columns = {'Date':object,'Timetable':object,'Turn':int,'Driver':object,'Fireman':object,'Trainee':object}
        self.fill_na = ''

    def create_individual_rosters(self,save_location):
        """
        Controlling function to:
        - import the final roster
        - create individual rosters for each crew member
        - save them to a specified location as a pdf
        """
        self.data_import.fillna(self.fill_na,inplace=True)
        rostered_individuals = self.data_import['Driver'].append(self.data_import['Fireman'].append(self.data_import['Trainee'])).unique()
        for indiv in rostered_individuals:
            if indiv != self.fill_na:
                driver_filter = self.data_import['Driver'] == indiv
                fireman_filter = self.data_import['Fireman'] == indiv
                trainee_filter = self.data_import['Trainee'] == indiv
                indiv_roster_df = self.data_import[driver_filter | fireman_filter | trainee_filter]
                indiv_save_path = os.path.join(save_location,r'Individual roster_'+indiv+'.pdf')
                self.print_df_to_pdf(indiv_roster_df,indiv_save_path)