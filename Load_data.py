import pandas as pd
import os
import time
import helper_function as hf
class Dataloader:
    def __init__(self,path):
        self.path = path
        self.data = None
        self.expected_columns_names  = ["step", "type", "amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig", "nameDest", "oldbalanceDest", "newbalanceDest", "isFraud", "isFlaggedFraud"]

    def Load_and_Validate(self):
        try:
            print("⏳ Loading data...")
            time.sleep(1)
            loaded_data = pd.read_csv(self.path , nrows = 2000)
            if  list(loaded_data.columns) != self.expected_columns_names:
                print("⚠️ Oops! The data shape is not what we expected 😕")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                return None
            self.data = loaded_data
            print("📥 Data loaded successfully. Ready for processing 🤖")
            hf.wait_user_input()
            os.system('cls' if os.name == 'nt' else 'clear')
            return self.data
        
        except FileNotFoundError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("😅 Oops! We couldn’t find that file 🕵️‍♂️")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return None
        
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Unexcpected Error: {e}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return None
        
#example
if __name__ == "__main__":
    path = "data/PS_20174392719_1491204439457_log.csv"
    a = Dataloader(path = path)
    a.Load_and_Validate()