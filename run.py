# import libraries
import quantstats as qs
import pandas as pd


# define column names
DATE_COL = 'Date'
RETURNS_COL = 'return'

# load custom data
df = pd.read_csv('data/returns.csv')

# convert date column to datetime and sort by date
df[DATE_COL] = pd.to_datetime(df[DATE_COL])
df.sort_values(by = DATE_COL, inplace = True)
df.set_index(DATE_COL, inplace = True)

STOCK_TICKER = 'SPY'
BENCHMARK_TICKER = 'SPY'
COMPANY_NAME = 'ABC'
STRATEGY_TITLE = f'{COMPANY_NAME} Systematic Macro ASM'







qs.reports.html(df[RETURNS_COL], STOCK_TICKER, output = "report.html", title = F"{COMPANY_NAME} Company", strategy_title = STRATEGY_TITLE, benchmark_title = STOCK_TICKER)