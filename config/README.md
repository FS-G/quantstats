# Configuration File

## config.csv

This CSV file contains all default configuration parameters for the QuantStats report generation.

### Usage

1. Edit `config.csv` to set default values
2. Run the script normally: `python run.py`
3. Or override defaults via command line: `python run.py --ticker AAPL --company MyCompany`

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| ticker | Stock ticker symbol for benchmark | SPY |
| company | Company name for the report | Autan |
| date_col | Column name for date in returns CSV | Date |
| returns_col | Column name for returns in CSV | return |
| data_file | Path to returns data file | data/returns.csv |
| output_file | Output path for generated HTML report | results/report.html |
| logo_path | Path to logo SVG file | logo/logo.svg |

### Command Line Override

Any parameter can be overridden via command line arguments:
- `--ticker`: Override the ticker symbol
- `--company`: Override the company name

Example:
```bash
python run.py --ticker AAPL --company MyCompany
```
