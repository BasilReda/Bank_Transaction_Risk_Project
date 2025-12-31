import pandas as pd
import os
class Export_Reports:
    def __init__(self,data):
        self.data = data
        if not os.path.exists("output"):
            os.makedirs("output")
    
    def Export_flagged_transactions(self):
        flagged_data = self.data[self.data["isFraud"]==1]
        if flagged_data.empty:
            print("⚠️ No suspicious transactions were flagged. File will be empty.")
        else:
            file_path = "output/flagged_transactions.csv"
            flagged_data.to_csv(file_path , index = False)
            print(f"✅ Saved {len(flagged_data)} rows to {file_path}")
    
    def Customer_risk_summary(self):
        print("💾 Saving 'customer_risk_summary.csv'...")
        suspicious_subset = self.data[self.data["isFraud"] > 0]
        summary = suspicious_subset.groupby("nameOrig").agg(
            total_flags = ("isFraud" , "sum"),
            total_moved = ("amount" , "sum")
        ).reset_index()
        summary = summary.sort_values(by = ["total_flags" , "total_moved"], ascending = [False , False])
        file_path = "output/customer_risk_summary.csv"
        summary.to_csv(file_path , index=False)
        print(f"✅ Saved summary for {len(summary)} risky customers.")
        return summary
    
    def Report_txt(self):
        print("📝 Generating 'report.txt'...")
        top_risky = self.Customer_risk_summary()
        top_risky = top_risky.head(10)
        with open("output/report.txt" , "w" , encoding ="utf-8") as f:
            f.write("FRAUD DETECTION SUMMARY TOP 10\n")
            f.write("🏆 TOP 10 RISKY CUSTOMERS\n")
            f.write(f"{'User ID'} | {'Flags'} | {'Total Stolen'}\n")
            for index , row in top_risky.iterrows():
                f.write(f"{row["nameOrig"]} | {row["total_flags"]} | {row["total_moved"]}\n")
        print("✅ Report saved.")
    
    def Exporting(self):
        self.Export_flagged_transactions()
        self.Report_txt()
        return self.data
#example
if __name__ == "__main__":
    data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
    test = Export_Reports(data)
    test.Exporting()
