import pandas as pd
import os
import time
class Cleaning:
    def __init__(self,data):
        self.data = data
        self.initial_shape = data.shape
    
    def Check_nulls(self):
        print("🔍 Checking for null values...")
        time.sleep(1)
        null_counts = self.data.isnull().sum()
        if null_counts.sum() == 0:
            print("✅ No null values found!")
            time.sleep(1)
            return 0
        else:
            columns_with_nulls = null_counts[null_counts > 0].index.tolist()
            print(f"⚠️ Found null values in columns: {columns_with_nulls}")
            time.sleep(1)
            return 1
    
    def Remove_Nulls(self):
        print("🧹 Cleaning data...")
        self.data = self.data.dropna()
        print(f"✅ Null values removed.\nNew shape: {self.data.shape} (was {self.initial_shape})")

    def Check_duplicates(self):
        print("🔍 Checking for duplicate rows...")
        duplicate_count = self.data.duplicated().sum()
        print(f"🔍 Number of duplicate rows: {duplicate_count}")
        return duplicate_count
    
    def Remove_duplicates(self):
        initial_shape = self.data.shape
        self.data = self.data.drop_duplicates()
        print(f"✅ Duplicates removed.\nNew shape: {self.data.shape} (was {initial_shape})")
    
    def Convert_timestamp(self,column_name):
        print(f"⏱️ Converting '{column_name}' to datetime...")
        date_cols = self.data.select_dtypes(include = ["datetime"]).columns
        if column_name not in date_cols:
            base_time = pd.to_datetime("2017-01-01")
            self.data[column_name] = pd.to_timedelta(self.data["step"], unit="h")
            self.data[column_name] = base_time + self.data[column_name]
            self.data[column_name] = pd.to_datetime(self.data[column_name])
            print(f"✅ '{column_name}' conversion complete.")
        else:
            print(f"ℹ️ '{column_name}' is already in datetime format.")

    def Clean(self):
        nulls = self.Check_nulls()
        if nulls == 1:
            self.Remove_Nulls()
        duplicates = self.Check_duplicates()
        if duplicates > 0:
            self.Remove_duplicates()
        self.Convert_timestamp("step")
        print("🎉 Data cleaning complete!")
        time.sleep(2)
        os.system("cls")
        return self.data
#example    
# a = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
# cleaner = Cleaning(data = a)
# data = cleaner.Clean()