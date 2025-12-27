import pandas as pd
class Cleaning:
    def __init__(self,data):
        self.data = data
        self.initial_shape = data.shape
    
    def Check_nulls(self):
        null_counts = self.data.isnull().sum()
        if null_counts.sum() == 0:
            print("✅ No null values found!")
            return 0
        else:
            columns_with_nulls = null_counts[null_counts > 0].index.tolist()
            print(f"⚠️ Found null values in columns: {columns_with_nulls}")
            return 1
    
    def Remove_Nulls(self):
        print("🧹 Cleaning data...")
        self.data = self.data.dropna()
        print(f"✅ Null values removed.\nNew shape: {self.data.shape} (was {self.initial_shape})")

    def Check_duplicates(self):
        duplicate_count = self.data.duplicated().sum()
        print(f"🔍 Number of duplicate rows: {duplicate_count}")
        return duplicate_count
    
    def Remove_duplicates(self):
        initial_shape = self.data.shape
        self.data = self.data.drop_duplicates()
        print(f"✅ Duplicates removed.\nNew shape: {self.data.shape} (was {initial_shape})")

    def Clean(self):
        nulls = self.Check_nulls()
        if nulls == 1:
            self.Remove_Nulls()
        duplicates = self.Check_duplicates()
        if duplicates > 0:
            self.Remove_duplicates()
        print("🎉 Data cleaning complete!")
        return self.data
#example    
# a = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
# cleaner = Cleaning(data = a)
# data = cleaner.Clean()