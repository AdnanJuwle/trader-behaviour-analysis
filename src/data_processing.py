import pandas as pd

def load_fear_greed_index(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df[['date', 'value', 'classification']]

def load_historical_data(filepath):
    df = pd.read_csv(filepath)
    # Convert timestamp column to datetime
    if 'Timestamp IST' in df.columns:
        df['timestamp'] = pd.to_datetime(df['Timestamp IST'], format='%d-%m-%Y %H:%M')
    elif 'time' in df.columns:
        df['timestamp'] = pd.to_datetime(df['time'])
    else:
        raise ValueError("No valid timestamp column found")
    return df

def merge_datasets(trader_df, sentiment_df):
    trader_df['date'] = trader_df['timestamp'].dt.date
    sentiment_df['date'] = sentiment_df['date'].dt.date
    merged = pd.merge(trader_df, sentiment_df, on='date', how='left')
    return merged

