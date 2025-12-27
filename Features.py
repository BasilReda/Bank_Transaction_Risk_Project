import pandas as pd
class Features:
    def __init__(self,data):
        self.data = data

    def Convert_timestamp(self,column_name):
        print(f"⏱️ Converting '{column_name}' to datetime...")
        base_time = pd.to_datetime("2017-01-01")
        self.data[column_name] = pd.to_timedelta(self.data["step"], unit="h")
        self.data[column_name] = base_time + self.data[column_name]
        self.data[column_name] = pd.to_datetime(self.data[column_name])
        print(f"✅ '{column_name}' conversion complete.")

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

    def featuring(self):
        self.Convert_timestamp("step")
        self.Frequency_hour()
        self.Frequency_day()
        return self.data


#example:
# data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
# test = Features(data)
# test.featuring()