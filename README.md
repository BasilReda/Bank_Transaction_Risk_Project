# 🔍 Fraud Detection System

A comprehensive Python-based transaction fraud detection and anomaly analysis platform that identifies suspicious financial activities and flags high-risk customers using statistical analysis and feature engineering.

---

## 📋 Overview

This system processes transaction data through a multi-stage pipeline to:
- Clean and validate raw transaction data
- Engineer meaningful features from transaction patterns
- Detect anomalies using statistical methods (Z-score analysis)
- Flag suspicious transactions and identify risky customers
- Generate detailed reports on fraud findings

**Perfect for:** Financial institutions, payment processors, and fraud prevention teams.

---

## 🏗️ Project Architecture

The system follows a modular, step-by-step pipeline approach:

```
Data Loading → Data Cleaning → Feature Engineering → Risk Analysis → Flagging → Report Export
```

### Module Breakdown

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| **Load_data.py** | Loads and validates CSV files | `Load_and_Validate()` - ensures data integrity |
| **Clean_data.py** | Data preprocessing and cleaning | Removes nulls/duplicates, converts timestamps |
| **Features.py** | Feature engineering | Creates behavioral patterns (hourly/daily frequency, rolling stats) |
| **Risk_Anomaly.py** | Anomaly detection | Calculates Z-scores, assigns risk bands (Low/Medium/High/Critical) |
| **Flag_Sus.py** | Suspicious activity extraction | Identifies confirmed fraud cases |
| **Export_Reports.py** | Report generation | Creates CSV summaries and text reports |
| **CLI.py** | User interface | Interactive menu-driven workflow |

---

## ✨ Features

### Data Cleaning
- ✅ Null value detection and removal
- ✅ Duplicate row detection and removal
- ✅ Timestamp conversion (step hours → datetime)

### Feature Engineering
- 📊 **Frequency Features**: Transaction count per user per hour/day
- 💰 **Amount Statistics**: Total, average, and maximum transaction amounts
- 📈 **Rolling Statistics**: 4-period rolling average of transactions
- 🔢 **User Profiles**: Aggregated customer transaction metrics

### Risk Detection
- 📉 **Z-Score Analysis**: Statistical deviation from user's normal behavior
- 🏷️ **Risk Bands**:
  - **Low**: Z-score < 1
  - **Medium**: Z-score 1-3
  - **High**: Z-score 3-5
  - **Critical**: Z-score ≥ 5

### Reporting
- 📄 **Flagged Transactions CSV**: All suspicious transactions
- 👥 **Customer Risk Summary CSV**: Top risky customers with fraud counts and amounts
- 📝 **Summary Report TXT**: Top 10 risky customers in readable format

---

## 📊 Data Requirements

### Input CSV Format
Expected columns (11 total):
- `nameOrig` - Source account ID
- `nameDest` - Destination account ID
- `amount` - Transaction amount
- `step` - Hour of transaction
- `isFraud` - Fraud indicator (0 or 1)
- Plus 6 additional transaction attributes

### Sample Data
Located in `data/PS_20174392719_1491204439457_log.csv`

---

## 🚀 Quick Start

### Installation
```bash
# Clone or navigate to project directory
cd e:\vs codes\python_project

# Install required packages
pip install pandas numpy tqdm
```

### Running the Application

**Option 1: Interactive CLI (Recommended)**
```bash
python main.py
```

This launches an interactive menu where you can:
1. Load your CSV data
2. Clean the data
3. Engineer features
4. Run anomaly detection
5. Flag suspicious activities
6. Export reports
7. View summary statistics

**Option 2: Programmatic Usage**
```python
from Load_data import Dataloader
from Clean_data import Cleaning
from Features import Features
from Risk_Anomaly import Risk_Anomaly
from Export_Reports import Export_Reports

# Load data
loader = Dataloader("data/your_file.csv")
data = loader.Load_and_Validate()

# Clean
cleaner = Cleaning(data)
data = cleaner.Clean()

# Engineer features
engineer = Features(data)
data = engineer.Featuring()

# Detect anomalies
risk = Risk_Anomaly(data)
data = risk.Run()

# Export reports
exporter = Export_Reports(data)
exporter.Exporting()
```

---

## 📁 Project Structure

```
python_project/
├── main.py                          # Entry point
├── CLI.py                           # Interactive user interface
├── Load_data.py                     # Data loading & validation
├── Clean_data.py                    # Data cleaning pipeline
├── Features.py                      # Feature engineering
├── Risk_Anomaly.py                  # Risk scoring & anomaly detection
├── Flag_Sus.py                      # Suspicious activity extraction
├── Export_Reports.py                # Report generation
├── README.md                        # This file
├── data/                            # Input data folder
│   └── PS_20174392719_1491204439457_log.csv
├── output/                          # Generated reports folder
│   ├── customer_risk_summary.csv    # Risk rankings by customer
│   ├── flagged_transactions.csv     # All suspicious transactions
│   └── report.txt                   # Executive summary
└── __pycache__/                     # Python cache
```

---

## 📈 Workflow Example

### Step 1: Load Data
```
Input: CSV file (2000 rows sample)
↓
Validates: 11 columns required
↓
Output: Structured pandas DataFrame
```

### Step 2: Clean Data
```
Input: Raw transaction data
↓
Process: Remove nulls → Remove duplicates → Convert timestamps
↓
Output: Clean, ready-to-analyze data
```

### Step 3: Feature Engineering
```
Input: Clean transaction data
↓
Creates:
  - frequency_hour: Transactions per hour by user
  - frequency_day: Transactions per day by user
  - user_count, user_avg, user_max, user_sum: Customer stats
  - rolling_avg_4: 4-period rolling average
↓
Output: Enhanced dataset with behavioral features
```

### Step 4: Risk Analysis
```
Input: Featured data
↓
Calculates:
  - user_std: Standard deviation per customer
  - z_score: (amount - user_avg) / user_std
  - Risk_Band: Low/Medium/High/Critical based on Z-score
↓
Output: Anomaly scores and risk classifications
```

### Step 5-6: Flagging & Export
```
Input: Scored data
↓
Generates:
  - flagged_transactions.csv: All fraud cases
  - customer_risk_summary.csv: Risk rankings
  - report.txt: Top 10 risks in human-readable format
↓
Output: Ready for investigation and action
```

---

## 📊 Output Files

### customer_risk_summary.csv
| Column | Description |
|--------|-------------|
| `nameOrig` | Customer ID |
| `total_flags` | Number of fraudulent transactions |
| `total_moved` | Total amount stolen |

**Sorted by:** Flags (descending) → Amount (descending)

### flagged_transactions.csv
All transactions flagged as fraud with complete details.

### report.txt
Human-readable summary of top 10 risky customers for quick review.

---

## 🔧 Configuration & Customization

### Adjust Risk Thresholds
Edit [Risk_Anomaly.py](Risk_Anomaly.py#L27) `Assign_risk()` method:
```python
conditions = [
    (self.data["z_score"] < 1),           # Adjust thresholds here
    (self.data["z_score"] >= 1) & (self.data["z_score"] < 3),
    (self.data["z_score"] >= 3) & (self.data["z_score"] < 5),
    (self.data["z_score"] >= 5)
]
```

### Change Sample Size
Edit [Load_data.py](Load_data.py#L13):
```python
loaded_data = pd.read_csv(self.path, nrows=5000)  # Increase from 2000
```

### Modify Rolling Window
Edit [Features.py](Features.py#L40):
```python
x.rolling(window=8, min_periods=1).mean()  # Change window size
```

---

## 📋 Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical operations
- **tqdm**: Progress bars for long operations

Install all dependencies:
```bash
pip install pandas numpy tqdm
```

---

## 🎯 Use Cases

1. **Real-time Fraud Monitoring**: Identify unusual transaction patterns
2. **Customer Risk Scoring**: Rank customers by fraud probability
3. **Investigation Prioritization**: Focus resources on highest-risk cases
4. **Compliance Reporting**: Generate audit trails and summaries
5. **Pattern Analysis**: Understand fraud behaviors and trends

---

## ⚠️ Important Notes

- The system analyzes a **2000-row sample** by default (configurable)
- Z-score method works best with **multiple transactions per customer**
- Risk thresholds may need tuning based on your **domain context**
- All output files are **automatically created** in the `output/` folder

---

## 🤝 Contributing

Feel free to extend this system by:
- Adding more feature types (velocity checks, location anomalies)
- Implementing machine learning models
- Integrating with real-time streaming data
- Adding database persistence

---

## 📞 Support

For issues or questions:
1. Check that your CSV has all required columns
2. Verify the file path is correct
3. Ensure sufficient disk space for outputs
4. Review the console messages for specific error details

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Status**: Production Ready ✅
