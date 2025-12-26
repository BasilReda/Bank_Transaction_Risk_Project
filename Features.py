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
        return self.data