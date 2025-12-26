import pandas as pd
class Dataloader:
    def __init__(self,path):
        self.path=path
        self.data = None
        self.expected_columns=11

    def Load_and_Validate(self):
        try:
            print("⏳ Loading data...")      
            loaded_data = pd.read_csv(self.path)
            if loaded_data.shape[1] != self.expected_columns:
                print("⚠️ Oops! The data shape is not what we expected 😕")
                return 0
            self.data = loaded_data
            print("📥 Data loaded successfully. Ready for processing 🤖")
            return self.data
        
        except FileNotFoundError:
            print("😅 Oops! We couldn’t find that file 🕵️‍♂️")
            return 0
        
        except Exception as e:
            print(f"Unexcpected Error: {e}")
            return 0
        

path = "data/PS_20174392719_1491204439457_log.csv"
a = Dataloader(path = path)
a.Load_and_Validate()