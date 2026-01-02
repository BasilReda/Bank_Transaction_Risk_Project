from Load_data import Dataloader
from Clean_data import Cleaning
from Features import Features
from Risk_Anomaly import Risk_Anomaly
from Flag_Sus import Flag_Sus
from Export_Reports import Export_Reports
import os
import time
import helper_function as hf
class CLI:
    def __init__(self):
        self.loaded_data = None
        self.data = None
        self.cleaned_data = None
        self.featured_data = None
        self.risk_data = None
        self.flagged_data = None
        self.exported_data = None
        self.path=None
        self.risky_customers = None
        
    
    def Clear_Screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def Run(self):
        while True:
            print("1 ➡️ Loading Data")
            print("2 ➡️ Cleaning Data")
            print("3 ➡️ Feature Engineering")
            print("4 ➡️ Risk Anomaly Detection")
            print("5 ➡️ Flagging Suspicious Activities")
            print("6 ➡️ Exporting Reports")
            print("7 ➡️ Display Summary in Console")
            print("0 ➡️ Exit")
            choice = input("Select an option (0-7): ")
            match choice:
                case "1":
                    if self.loaded_data is not None:
                        self.Clear_Screen()
                        print("⚠️ Data already loaded. Loading again will overwrite existing data.")
                        time.sleep(1)
                        confirm = input("Do you want to continue? (y/n): ")
                        if confirm.lower() != "y":
                            self.Clear_Screen()
                            continue

                    self.Clear_Screen()
                    input_path = input("Enter the path to the CSV file: ")
                    loader = Dataloader(input_path)
                    new_data = loader.Load_and_Validate()

                    if new_data is not None:
                        self.data = new_data
                        self.loaded_data = 1
                        self.path = input_path
                        self.Clear_Screen()
                        print(f"Current loaded data: {self.path}")
                        time.sleep(1)

                    else:
                        if self.loaded_data is not None:
                            print("❌ Loading failed. Retaining previous state.")
                        else:
                            print("❌ Loading failed. No data is currently loaded.")
                            time.sleep(1)
                        if self.path is not None:
                            print(f"Current loaded data: {self.path}")
                        time.sleep(2)
                
                case "2":
                    self.Clear_Screen()
                    if self.data is not None:
                        cleaner = Cleaning(self.data)
                        self.cleaned_data = 1
                        self.data = cleaner.Clean()
                    else:
                        print("⚠️ Please load data first.")
                        time.sleep(1)
                        self.Clear_Screen()

                case "3":
                    self.Clear_Screen()
                    if self.cleaned_data is not None:
                        feature_engineer = Features(self.data)
                        self.data = feature_engineer.Featuring()
                        self.featured_data = 1
                    else:
                        print("⚠️ Please Clean Data first.")
                        time.sleep(1)
                        self.Clear_Screen()
                        
                case "4":
                    self.Clear_Screen()
                    if self.featured_data is not None:
                        risk_anomaly = Risk_Anomaly(self.data)
                        self.data = risk_anomaly.Run()
                        self.risk_data = 1
                    else:
                        print("⚠️ Please perform Feature Engineering first.")
                        time.sleep(1)
                        self.Clear_Screen()

                case "5":
                    self.Clear_Screen()
                    if self.risk_data is not None:
                        flag_sus = Flag_Sus(self.data)
                        self.data = flag_sus.Flagging()
                        self.flagged_data = 1
                    else:
                        print("⚠️ Please perform Risk Anomaly Detection first.")
                        time.sleep(1)
                        self.Clear_Screen()

                case "6":
                    self.Clear_Screen()
                    if self.flagged_data is not None:
                        exporter = Export_Reports(self.data)
                        self.risky_customers = exporter.Exporting()
                        self.exported_data = 1
                    else:
                        print("⚠️ Please perform Flagging Suspicious Activities first.")
                        time.sleep(1)
                        self.Clear_Screen()

                case "7":
                    self.Clear_Screen()
                    if self.exported_data is not None:
                        self.Clear_Screen()
                        print(self.risky_customers)
                        hf.wait_user_input()
                        self.Clear_Screen()
                    else:
                        print("⚠️ Please perform Exporting Reports first.")
                        time.sleep(1)
                        self.Clear_Screen()

                case "0":
                    self.Clear_Screen()
                    print("👋 Exiting the program. Goodbye!")
                    time.sleep(1)
                    break

