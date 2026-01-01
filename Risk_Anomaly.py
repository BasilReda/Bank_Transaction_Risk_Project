import pandas as pd
import numpy as np
from Features import Features
import os
import time
class Risk_Anomaly:
    def __init__(self,data):
        self.data = data
    
    def Validate_columns(self , columns_required):
        if isinstance(columns_required , str):
            columns_required = [columns_required]
        
        needed_columns = [col for col in columns_required if col not in self.data.columns]
        if needed_columns:
            raise KeyError(f"❌ Missing required columns: {needed_columns}\nRun previous Step to Get these Columns")
    
    def Compute_z_scores(self):
        os.system("cls")
        print("📊 Calculating Z-Scores...")
        self.Validate_columns(["nameOrig" , "amount" , "user_avg"])
        self.data["user_std"] = self.data.groupby("nameOrig")["amount"].transform("std")
        self.data["user_std"] = self.data["user_std"].fillna(1).replace(0,1)
        self.data["z_score"] = (self.data["amount"] - self.data["user_avg"])/self.data["user_std"]
        print("✅ Z-scores computed.")
        time.sleep(1)
    
    def Assign_risk(self):
        print("🏷️ Assigning Risk Bands...")
        self.Validate_columns("z_score")
        conditions = [
            (self.data["z_score"]<1),
            (self.data["z_score"]>=1) & (self.data["z_score"]<3),
            (self.data["z_score"]>=3) & (self.data["z_score"]<5),
            (self.data["z_score"]>=5)
        ]
        labels = ["Low" , "Medium" , "High" , "Critical"]
        self.data["Risk_Band"] = np.select(conditions , labels , default="Low")
        print("✅ Risk Bands assigned.")
        print(f"summary for risk bands {self.data["Risk_Band"].value_counts()}")
        time.sleep(1)
    
    def Run(self):
        self.Compute_z_scores()
        self.Assign_risk()
        os.system("cls")
        return self.data
#example:
if __name__ == "__main__":
    data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
    test2 = Features(data)
    test2 = test2.Featuring()
    test = Risk_Anomaly(test2)
    test.Run()