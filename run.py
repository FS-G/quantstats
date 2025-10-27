# import libraries
import quantstats as qs
import pandas as pd
import os
import argparse
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')


# define column names
DATE_COL = 'Date'
RETURNS_COL = 'return'

# parse command-line arguments
parser = argparse.ArgumentParser(description='Generate portfolio performance report with QuantStats')
parser.add_argument('--ticker', type=str, default='SPY', help='Stock ticker symbol for benchmark (default: SPY)')
parser.add_argument('--company', type=str, default='Autan', help='Company name (default: ABC)')
args = parser.parse_args()

# load custom data
df = pd.read_csv('data/returns.csv')

# convert date column to datetime and sort by date
df[DATE_COL] = pd.to_datetime(df[DATE_COL])
df.sort_values(by = DATE_COL, inplace = True)
df.set_index(DATE_COL, inplace = True)

STOCK_TICKER = args.ticker
BENCHMARK_TICKER = args.ticker
COMPANY_NAME = args.company
STRATEGY_TITLE = f'{COMPANY_NAME[0]}SM'



# create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Read logo file and embed it in the report
logo_path = 'logo/logo.svg'
if os.path.exists(logo_path):
    with open(logo_path, 'r', encoding='utf-8') as f:
        logo_content = f.read()
    # Embed the SVG directly
    logo_html = f'<div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">{logo_content}</div>'
else:
    logo_html = '<div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; color: #888; font-size: 12px;">SVG LOGO</div>'

qs.reports.html(df[RETURNS_COL], STOCK_TICKER, output = "results/report.html", title = F"{COMPANY_NAME} Company", strategy_title = STRATEGY_TITLE, benchmark_title = STOCK_TICKER, company_name = COMPANY_NAME, logo = logo_html)