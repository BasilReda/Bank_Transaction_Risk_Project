import pandas as pd
import os
import time
class Dataloader:
    def __init__(self,path):
        self.path=path
        self.data = None
        self.expected_columns=11

    def Load_and_Validate(self):
        try:
            print("⏳ Loading data...")
            time.sleep(1)
            loaded_data = pd.read_csv(self.path , nrows = 2000)
            if loaded_data.shape[1] != self.expected_columns:
                print("⚠️ Oops! The data shape is not what we expected 😕")
                time.sleep(1)
                os.system("cls")
                return None
            self.data = loaded_data
            print("📥 Data loaded successfully. Ready for processing 🤖")
            time.sleep(1)
            os.system("cls")
            return self.data
        
        except FileNotFoundError:
            os.system("cls")
            print("😅 Oops! We couldn’t find that file 🕵️‍♂️")
            time.sleep(1)
            os.system("cls")
            return None
        
        except Exception as e:
            os.system("cls")
            print(f"Unexcpected Error: {e}")
            time.sleep(1)
            os.system("cls")
            return None
        
#example
# path = "data/PS_20174392719_1491204439457_log.csv"
# a = Dataloader(path = path)
# a.Load_and_Validate()