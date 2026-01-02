import pandas as pd
import os
import helper_function as hf
class Flag_Sus:
    def __init__(self,data):
        self.data = data

    def Sus_activity(self):
        print("📋 Extracting list of confirmed fraud cases...")
        subset = self.data[self.data["isFraud"]==1]
        subset = subset[["nameOrig" , "nameDest" , "amount","isFraud"]]
        fraud_list = subset.to_dict("records")
        print(f"✅ Extracted {len(fraud_list)} fraud cases.")
    
    def Flagging(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.Sus_activity()
        hf.wait_user_input()
        os.system('cls' if os.name == 'nt' else 'clear')
        return self.data
    
#example
if __name__ == "__main__":
    data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
    test = Flag_Sus(data)
    test.Sus_activity()