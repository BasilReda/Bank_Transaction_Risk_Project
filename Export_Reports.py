import pandas as pd
import os
import time
from Risk_Anomaly import Risk_Anomaly
from Features import Features
from Clean_data import Cleaning
class Export_Reports:
    def __init__(self,data):
        self.data = data
        self.flagged_data = None
        if not os.path.exists("output"):
            os.makedirs("output")
    
    def Export_flagged_transactions(self):
        self.flagged_data = self.data[self.data["z_score"] >= 1]
        if self.flagged_data.empty:
            print("⚠️ No suspicious transactions were flagged. File will be empty.\n")
        else:
            file_path = "output/flagged_transactions.csv"
            self.flagged_data.to_csv(file_path , index = False)
            print(f"✅ Saved {len(self.flagged_data)} rows to {file_path}\n")
    
    def Customer_risk_summary(self):
        print("💾 Saving 'customer_risk_summary.csv'...")
        if self.flagged_data is not None:
            summary = self.flagged_data.groupby("nameOrig").agg(
                max_z_score = ("z_score" , "max"),
                total_moved = ("amount" , "sum")
            ).reset_index()
            summary = summary.sort_values(by = ["max_z_score" , "total_moved"], ascending = [False , False])
            file_path = "output/customer_risk_summary.csv"
            summary.to_csv(file_path , index=False)
            print(f"✅ Saved summary for {len(summary)} risky customers.\n")
            return summary
    
    def Report_txt(self):
        print("📝 Generating 'report.txt'...")
        top_risky = self.Customer_risk_summary()
        top_risky = top_risky.head(10)
        with open("output/report.txt" , "w" , encoding ="utf-8") as f:
            f.write("FRAUD DETECTION SUMMARY TOP 10\n")
            f.write("🏆 TOP 10 RISKY CUSTOMERS\n")
            f.write(f"{'User ID'} | {'Z_Score'} | {'Total Stolen'}\n")
            for index , row in top_risky.iterrows():
                f.write(f"{row["nameOrig"]} | {row["max_z_score"]} | {row["total_moved"]}\n")
        print("✅ Report saved.\n")
        return top_risky
    
    def Exporting(self):
        os.system("cls")
        self.Export_flagged_transactions()
        time.sleep(1)
        risky_customers = self.Report_txt()
        time.sleep(1)
        os.system("cls")
        return risky_customers
#example
if __name__ == "__main__":
    data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv",nrows = 1000000)
    cleaner = Cleaning(data)
    cleaned_data = cleaner.Clean()
    feature_engineer = Features(cleaned_data)
    featured_data = feature_engineer.Featuring()
    risk_analyzer = Risk_Anomaly(featured_data)
    analyzed_data = risk_analyzer.Run()
    exporter = Export_Reports(analyzed_data)
    exporter.Exporting()
