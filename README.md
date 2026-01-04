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
Data Loading → Data Cleaning → Feature Engineering → Risk Analysis → Report Export
```

**Note:** Z-score based flagging is now integrated directly into Risk Analysis. Transactions with Z-score ≥ 1 are automatically flagged as suspicious.

### Module Breakdown

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| **Load_data.py** | Loads and validates CSV files | `Load_and_Validate()` - loads up to 6M rows and ensures data integrity |
| **Clean_data.py** | Data preprocessing and cleaning | Removes nulls/duplicates, converts timestamps |
| **Features.py** | Feature engineering | Creates behavioral patterns (hourly/daily frequency, rolling stats) |
| **Risk_Anomaly.py** | Anomaly detection & flagging | Calculates Z-scores, assigns risk bands, identifies suspicious transactions |
| **Export_Reports.py** | Report generation | Creates CSV summaries and text reports of flagged transactions |
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
- 🚩 **Automatic Flagging**: All transactions with Z-score ≥ 1 are flagged as suspicious

### Reporting
- 📄 **Flagged Transactions CSV**: All transactions with Z-score ≥ 1
- 👥 **Customer Risk Summary CSV**: Top risky customers ranked by maximum Z-score and total amount
- 📝 **Summary Report TXT**: Top 10 risky customers with Z-score analysis

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

# Install required packages from requirements.txt
pip install -r requirements.txt
```

**Required Packages** (automatically installed):
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `tqdm` - Progress bars for data processing

See [requirements.txt](requirements.txt) for full dependency list.

### Running the Application

**Option 1: Interactive CLI (Recommended)**
```bash
python main.py
```

This launches an interactive menu where you can:
1. Load your CSV data
2. Clean the data
3. Engineer features
4. Run risk analysis (includes Z-score computation & flagging)
5. Export flagged transactions and reports
6. View summary statistics

**Option 2: Programmatic Usage**
```python
from Bank_Transaction import Dataloader, Cleaning, Features, Risk_Anomaly, Export_Reports

# Load data
loader = Dataloader("data/your_file.csv")
data = loader.Load_and_Validate()

# Clean
cleaner = Cleaning(data)
data = cleaner.Clean()

# Engineer features
engineer = Features(data)
data = engineer.Featuring()

# Detect anomalies and flag suspicious transactions
risk = Risk_Anomaly(data)
data = risk.Run()

# Export reports of flagged transactions
exporter = Export_Reports(data)
exporter.Exporting()
```

---

## 📁 Project Structure

```
python_project/
├── main.py                          # Entry point - starts the CLI
├── README.md                        # This file
├── requirements.txt                 # Python package dependencies
├── Bank_Transaction/                # Main package directory
│   ├── __init__.py                  # Package initialization - exports all classes
│   ├── CLI.py                       # Interactive user interface & workflow orchestration
│   ├── Load_data.py                 # Data loading & validation (up to 6M rows)
│   ├── Clean_data.py                # Data cleaning pipeline
│   ├── Features.py                  # Feature engineering & behavioral pattern analysis
│   ├── Risk_Anomaly.py              # Risk scoring, Z-score calculation, automatic flagging
│   ├── Flag_Sus.py                  # Suspicious activity extraction
│   ├── Export_Reports.py            # Report generation from flagged transactions
│   ├── helper_function.py           # Utility functions (wait_user_input, etc.)
│   └── __pycache__/                 # Python cache directory
├── data/                            # Input data folder
│   └── PS_20174392719_1491204439457_log.csv (6M+ rows)
├── output/                          # Generated reports folder
│   ├── customer_risk_summary.csv    # Risk rankings by customer
│   ├── flagged_transactions.csv     # All transactions with Z-score ≥ 1
│   └── report.txt                   # Top 10 risky customers summary
└── __pycache__/                     # Python cache
```

### Package Architecture (`Bank_Transaction/`)

The project is organized as a **Python package** with centralized imports:

**`__init__.py` - Package Initialization**
```python
from Bank_Transaction.Load_data import Dataloader
from Bank_Transaction.Clean_data import Cleaning
from Bank_Transaction.Features import Features
from Bank_Transaction.Risk_Anomaly import Risk_Anomaly
from Bank_Transaction.Flag_Sus import Flag_Sus
from Bank_Transaction.Export_Reports import Export_Reports

__all__ = ['Dataloader', 'Cleaning', 'Features', 'Risk_Anomaly', 'Flag_Sus', 'Export_Reports']
```

**Benefits:**
- ✅ **Cleaner Imports**: `from Bank_Transaction import Dataloader` instead of `from Bank_Transaction.Load_data import Dataloader`
- ✅ **Clear Public API**: `__all__` explicitly defines what users should access
- ✅ **Easy Wildcard Import**: `from Bank_Transaction import *` gets all core classes
- ✅ **Centralized Dependencies**: All internal imports managed in one place
- ✅ **Professional Package Structure**: Follows Python packaging best practices

---

## 📈 Workflow Example

### Step 1: Load Data
```
Input: CSV file (up to 6M rows)
↓
Validates: 11 columns required
↓
Output: Structured pandas DataFrame ready for processing
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

### Step 4: Risk Analysis & Flagging
```
Input: Featured data
↓
Calculates:
  - user_std: Standard deviation per customer
  - z_score: (amount - user_avg) / user_std
  - Risk_Band: Low/Medium/High/Critical based on Z-score
  - Flags transactions with Z-score ≥ 1 as suspicious
↓
Output: Scored data with risk bands and flagged transactions
```

### Step 5: Report Export
```
Input: Flagged transaction data
↓
Generates:
  - flagged_transactions.csv: All transactions with Z-score ≥ 1
  - customer_risk_summary.csv: Risk rankings by Z-score and amount
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
| `max_z_score` | Maximum Z-score among flagged transactions |
| `total_moved` | Total amount in flagged transactions |

**Sorted by:** Max Z-score (descending) → Amount (descending)

### flagged_transactions.csv
All transactions with Z-score ≥ 1, including full transaction details and Z-score values.

### report.txt
Human-readable summary of top 10 risky customers ranked by maximum Z-score for quick review.

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

### Change Data Sample Size
Edit [Load_data.py](Load_data.py#L13):
```python
loaded_data = pd.read_csv(self.path, nrows=5000000)  # Adjust from default 3000000
```

### Adjust Z-Score Flagging Threshold
Edit [Export_Reports.py](Export_Reports.py#L11):
```python
self.flagged_data = self.data[self.data["z_score"] >= 1.5]  # Change from 1 to 1.5
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

- The system can process **up to 6M rows** of transaction data
- Flagging is now **Z-score based** (Z-score ≥ 1) instead of isFraud indicator
- Z-score method works best with **multiple transactions per customer**
- Risk thresholds can be customized based on your **domain context**
- All output files are **automatically created** in the `output/` folder
- The older **isFraud column** in data is no longer used for flagging

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
