# QuantStats Portfolio Analytics

This project uses QuantStats to generate comprehensive portfolio performance reports from custom returns data.

## Prerequisites

- Python 3.10 or higher
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd quantstats-project
```

### 2. Create a Virtual Environment

Create a virtual environment in the project directory:

**On Windows:**
```bash
python -m venv ./venv
```

**On macOS/Linux:**
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**On Windows:**
```bash
./venv/Scripts/activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

When activated, you should see `(venv)` at the beginning of your terminal prompt.

### 4. Install Requirements

Install all required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Prepare Your Data

#### Update Your Returns Data

Place your returns data in the `data/` directory. The data should be in CSV format with the following structure:

- **Date column**: Column named `Date` containing dates in YYYY-MM-DD format
- **Return column**: Column named `return` containing daily returns (as decimals, e.g., 0.0125 for 1.25%)

Example structure:
```csv
Date,return
2025-09-01,0.0000
2025-09-02,0.0125
2025-09-03,-0.0050
```

#### Update the Data Path (if needed)

If your data file is in a different location or has a different name, update the path in `run.py`:

```python
# Line 12 in run.py
df = pd.read_csv('data/returns.csv')  # Update this path if needed
```

## Running the Report

Once everything is set up, run the analysis. The script accepts optional command-line arguments for customization:

### Basic Usage (with defaults)

```bash
python run.py
```

This will use the default values:
- **Company Name**: ABC
- **Stock Ticker**: SPY

### Advanced Usage (with custom arguments)

You can pass custom arguments using `--ticker` and `--company` flags:

```bash
python run.py --ticker AAPL --company Apple
```

```bash
python run.py --ticker MSFT --company "Microsoft Corporation"
```

**Arguments:**
- `--ticker`: Stock ticker symbol for benchmark comparison (default: SPY)
- `--company`: Company name to display in the report (default: ABC)

**Examples:**
```bash
# Generate report for Tesla with TSLA benchmark
python run.py --ticker TSLA --company Tesla

# Generate report for Amazon with QQQ benchmark
python run.py --ticker QQQ --company Amazon
```

The script will:
- Load your returns data
- Compare it with the specified benchmark
- Generate a comprehensive HTML report

## Output

The generated report will be saved in the `results/` directory as `results/report.html`.

You can open this file in any web browser to view:
- Performance metrics (Sharpe ratio, Sortino ratio, etc.)
- Cumulative returns
- Drawdown analysis
- Monthly and annual returns
- Risk statistics
- Benchmark comparison

## Configuration

You can customize the report in two ways:

### 1. Command-Line Arguments (Recommended)

Pass arguments when running the script:
```bash
python run.py --ticker AAPL --company "Your Company Name"
```

See the [Running the Report](#running-the-report) section for details.

### 2. Modify Variables in run.py

Alternatively, you can modify variables in `run.py`:
- `COMPANY_NAME`: Your company name
- `STOCK_TICKER`: Ticker symbol for the benchmark (default: 'SPY')
- `STRATEGY_TITLE`: Custom title for your strategy (auto-generated from COMPANY_NAME)
- `DATE_COL`: Name of the date column in your data
- `RETURNS_COL`: Name of the returns column in your data

## Troubleshooting

### Import Errors
If you encounter import errors, make sure:
- Your virtual environment is activated
- All requirements are installed: `pip install -r requirements.txt`

### Data Format Issues
Ensure your CSV file has:
- Proper date format (YYYY-MM-DD)
- Returns as decimals (not percentages)
- Column headers exactly as `Date` and `return`

### Directory Not Found Errors
The script will automatically create the `results/` directory if it doesn't exist.

## Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

## License

This project uses QuantStats. See the QuantStats license in the quantstats directory.

