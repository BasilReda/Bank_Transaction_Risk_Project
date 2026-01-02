from tqdm  import tqdm
import pandas as pd
import time
import os
import helper_function as hf
class Features:
    def __init__(self,data):
        self.data = data


    def Frequency_hour(self):
        print("📊 Calculating transaction frequency per user per hour...")
        hourly_counts = self.data.groupby(
            ["nameOrig" , "step"]).size().reset_index(name="transaction_count")
        self.data["frequency_hour"] = self.data.set_index(["nameOrig" , "step"]).index.map(
            hourly_counts.set_index(["nameOrig","step"])["transaction_count"]
        )
        print("✨ Feature ready Named: 'frequency_hour'")
    
    def Frequency_day(self):
        print("⏳ Creating daily transaction frequency feature...")
        self.data["day"] = self.data["step"].dt.date
        daily_counts = self.data.groupby(["nameOrig","day"]).size().reset_index(name="day_count")
        self.data["frequency_day"] = self.data.set_index(["nameOrig","day"]).index.map(
            daily_counts.set_index(["nameOrig","day"])["day_count"]
        )
        print("✔️ frequency_per_day feature created")

    def Statistics(self):
        steps = 3
        with tqdm(total=steps, desc="🔧 Feature Engineering Progress") as pbar:
            print("🔢 Computing transaction count per customer...")
            self.data["user_count"] = self.data.groupby("nameOrig")["amount"].transform("count")
            print("✅ Transaction count per customer completed.")
            pbar.update(1)
            time.sleep(1)

            print("💰 Computing total, average, and maximum transaction amounts...")
            self.data["user_max"] = self.data.groupby("nameOrig")["amount"].transform("max")
            self.data["user_avg"] = self.data.groupby("nameOrig")["amount"].transform("mean")
            self.data["user_sum"] = self.data.groupby("nameOrig")["amount"].transform("sum")
            print("✅ Transaction amount statistics completed.")
            pbar.update(1)
            time.sleep(1)

            print("📊 Computing rolling transaction statistics...")
            self.data = self.data.sort_values(by=["nameOrig" , "step"])
            self.data["rolling_avg_4"] = self.data.groupby("nameOrig")["amount"].transform(lambda x : x.rolling(window = 4 , min_periods = 1).mean())
            print("✅ Rolling statistics completed.")
            pbar.update(1)
            time.sleep(1)


    def Featuring(self):
        self.Frequency_hour()
        time.sleep(1)
        self.Frequency_day()
        time.sleep(1)
        self.Statistics()
        hf.wait_user_input()
        os.system('cls' if os.name == 'nt' else 'clear')
        return self.data


# example:
if __name__ == "__main__":
    data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
    test = Features(data)
    test.Featuring()