import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.data_processing import load_fear_greed_index, load_historical_data, merge_datasets
from src.feature_engineering import calculate_daily_performance, categorize_performance
from src.analysis import analyze_performance_by_sentiment, correlation_analysis
from src.visualization import plot_pnl_by_sentiment, plot_trade_size_by_sentiment, plot_buy_ratio_by_sentiment
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    fear_greed_df = load_fear_greed_index('data/fear_greed_index.csv')
    trader_df = load_historical_data('data/historical_data.csv')

    merged_df = merge_datasets(trader_df, fear_greed_df)

    daily_perf = calculate_daily_performance(merged_df)
    daily_perf = categorize_performance(daily_perf)

    anova_result = analyze_performance_by_sentiment(daily_perf)
    print(f"ANOVA test: F={anova_result.statistic:.3f}, p={anova_result.pvalue:.3f}")

    corr = correlation_analysis(daily_perf)
    print(f"Correlation between Fear Greed index and PnL: {corr:.3f}")

    plot_pnl_by_sentiment(daily_perf)
    plot_trade_size_by_sentiment(daily_perf)
    plot_buy_ratio_by_sentiment(daily_perf)
    #plot_leverage_vs_sentiment(daily_perf)
    plt.show()


if __name__ == "__main__":
    main()

