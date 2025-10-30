# import libraries
import quantstats as qs
import pandas as pd
import os
import argparse
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')


# Load configuration from config file
config_path = 'config/config.csv'
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file not found: {config_path}")

config_df = pd.read_csv(config_path)
config_dict = dict(zip(config_df['parameter'], config_df['value']))

# parse command-line arguments (will override config values if provided)
parser = argparse.ArgumentParser(description='Generate portfolio performance report with QuantStats')
parser.add_argument('--ticker', type=str, default=config_dict.get('ticker'), help='Stock ticker symbol for benchmark')
parser.add_argument('--company', type=str, default=config_dict.get('company'), help='Company name')
args = parser.parse_args()

# Use command-line args (they default to config values if not provided)
TICKER = args.ticker
COMPANY = args.company

# Define column names from config
DATE_COL = config_dict.get('date_col', 'Date')
RETURNS_COL = config_dict.get('returns_col', 'return')
DATA_FILE = config_dict.get('data_file', 'data/returns.csv')
OUTPUT_FILE = config_dict.get('output_file', 'results/report.html')
LOGO_PATH = config_dict.get('logo_path', 'logo/logo.svg')

# load custom data
df = pd.read_csv(DATA_FILE)

# convert date column to datetime and sort by date
df[DATE_COL] = pd.to_datetime(df[DATE_COL])
df.sort_values(by = DATE_COL, inplace = True)
df.set_index(DATE_COL, inplace = True)

STOCK_TICKER = TICKER
BENCHMARK_TICKER = TICKER
COMPANY_NAME = COMPANY
STRATEGY_TITLE = f'{COMPANY_NAME[0]}SM'



# create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Read logo file and embed it in the report
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, 'r', encoding='utf-8') as f:
        logo_content = f.read()
    # Embed the SVG directly
    logo_html = f'<div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">{logo_content}</div>'
else:
    logo_html = '<div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; color: #888; font-size: 12px;">SVG LOGO</div>'

qs.reports.html(df[RETURNS_COL], STOCK_TICKER, output=OUTPUT_FILE, title=f"{COMPANY_NAME} Company", strategy_title=STRATEGY_TITLE, benchmark_title=STOCK_TICKER, company_name=COMPANY_NAME, logo=logo_html)