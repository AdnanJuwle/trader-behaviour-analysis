import matplotlib.pyplot as plt
import seaborn as sns

def plot_pnl_by_sentiment(df):
    plt.figure(figsize=(10,6))
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    sns.boxplot(x='classification', y='Closed PnL', data=df, order=[c for c in order if c in df['classification'].unique()])
    plt.title('Trader PnL Distribution by Market Sentiment')
    plt.xlabel('Market Sentiment')
    plt.ylabel('Closed PnL')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()  # Do NOT call here

def plot_trade_size_by_sentiment(df):
    plt.figure(figsize=(10,6))
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    sns.boxplot(x='classification', y='Size USD', data=df, order=[c for c in order if c in df['classification'].unique()])
    plt.title('Trade Size (USD) by Market Sentiment')
    plt.xlabel('Market Sentiment')
    plt.ylabel('Trade Size (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()

def plot_buy_ratio_by_sentiment(df):
    plt.figure(figsize=(10,6))
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    sns.boxplot(
        x='classification',
        y='buy_ratio',
        data=df,
        order=[c for c in order if c in df['classification'].unique()]
    )
    plt.title('Buy Ratio by Market Sentiment')
    plt.xlabel('Market Sentiment')
    plt.ylabel('Buy Ratio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()

