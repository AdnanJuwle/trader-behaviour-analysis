import pandas as pd

def calculate_daily_performance(df):
    grouped = df.groupby(['Account', 'date', 'classification', 'value']).agg({
        'Closed PnL': 'sum',
        'Size USD': 'sum',
        'Side': lambda x: (x == 'BUY').sum() / len(x)
    }).reset_index()
    grouped.rename(columns={'Side': 'buy_ratio'}, inplace=True)
    return grouped

def categorize_performance(df):
    df['performance_category'] = pd.cut(
        df['Closed PnL'],
        bins=[-float('inf'), 0, float('inf')],
        labels=['Loss', 'Profit']
    )
    df['performance_category'] = df['performance_category'].astype('category')
    if 'Break-even' not in df['performance_category'].cat.categories:
        df['performance_category'] = df['performance_category'].cat.add_categories(['Break-even'])
    df.loc[df['Closed PnL'] == 0, 'performance_category'] = 'Break-even'
    return df
